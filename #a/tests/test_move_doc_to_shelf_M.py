
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
    ("2207 876234", "44", False, True),
    ("10006", "90", False, True),
    ("54", "3", True, False),
    ("155555", "85", True, True),
    ("11-2", "2", False, False)
]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_move_doc_to_shelf(self, doc_num, shelf_num, no_such_doc, no_such_shelf):
        current_doc = DocData(documents, directories)
        result = current_doc.move_doc_to_shelf(doc_num, shelf_num)
        self.assertEqual(no_such_doc, result[0])
        self.assertEqual(no_such_shelf, result[1])
