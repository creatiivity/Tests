
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
    ("1", False),
    ("2", False),
    ("3", False),
    ("5", True),
    ("99", True)
]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_add_new_shelf(self, shelf_num, shelf_must_be_added):
        current_doc = DocData(documents, directories)
        result = current_doc.add_new_shelf(shelf_num)
        self.assertEqual(shelf_must_be_added, result)
