
import os
import json
import unittest
from parameterized import parameterized
from documents_app.docs_app import DocData


with open(os.path.join(os.getcwd(), "tests", "data", "docs_in_tests.json"), 'rb') as fp:
    documents = json.load(fp)

with open(os.path.join(os.getcwd(), "tests", "data", "dirs_in_tests.json"), 'rb') as fp2:
    directories = json.load(fp2)


FIXTURES1 = [
    ("2207 876234", "1"),
    ("10006", "2"),
    ("5455 028765", "1")
]

FIXTURES2 = [
    ("10006", "3"),
    ("1", "2207 876234"),
    ("5455 028765", "2")
]

FIXTURES3 = [
    ("99", None),
    ("110", None)
]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_get_doc_shelf1(self, number, exp_result):
        current_doc = DocData(documents, directories)
        result = current_doc.get_doc_shelf(number)
        self.assertEqual(exp_result, result)

    @parameterized.expand(FIXTURES2)
    def test_get_doc_shelf2(self, number, exp_result):
        current_doc = DocData(documents, directories)
        result = current_doc.get_doc_shelf(number)
        self.assertNotEqual(exp_result, result)


    @parameterized.expand(FIXTURES3)
    def test_get_doc_shelf3(self, number, exp_result):
        current_doc = DocData(documents, directories)
        result = current_doc.get_doc_shelf(number)
        self.assertEqual(exp_result, result)
