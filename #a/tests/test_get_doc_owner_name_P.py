
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
    ("11-2", "Геннадий Покемонов"),
    ("2207 876234", "Василий Гупкин")
]

FIXTURES2 = [
    ("11-5", "Геннадий Покемонов"),
    ("10006", "Василий Гупкин"),
    ("1556", "Василий Гупкин")
]

FIXTURES3 = [
    ("1885", None),
    ("996", None)
]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_get_doc_owner_name1(self, number, name):
        current_doc = DocData(documents, directories)
        result = current_doc.get_doc_owner_name(number)
        self.assertEqual(name, result)

    @parameterized.expand(FIXTURES2)
    def test_get_doc_owner_name2(self, number, name):
        current_doc = DocData(documents, directories)
        result = current_doc.get_doc_owner_name(number)
        self.assertNotEqual(name, result)

    @parameterized.expand(FIXTURES3)
    def test_get_doc_owner_name3(self, number, no_name):
        current_doc = DocData(documents, directories)
        result = current_doc.get_doc_owner_name(number)
        self.assertEqual(no_name, result)
