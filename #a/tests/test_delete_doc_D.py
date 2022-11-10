
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
    ("2207 876234", {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}, True, True),
    ("10006", {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}, True, True)
]

FIXTURES2 = [
    ("5455 028765", False, True)
]

FIXTURES3 = [
    ("221", True, True),
    ("1555", True, True)
]

class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_delete_doc1(self, doc_num, entry, removed_from_docs, removed_from_dirs):
        current_doc = DocData(documents, directories)
        result = current_doc.delete_doc(doc_num)
        self.assertNotIn(entry, documents)
        self.assertNotIn(doc_num, directories.values())
        self.assertEqual(removed_from_docs, result[0])
        self.assertEqual(removed_from_dirs, result[1])

    @parameterized.expand(FIXTURES2)
    def test_delete_doc2(self, doc_num, removed_from_docs, removed_from_dirs):
        current_doc = DocData(documents, directories)
        result = current_doc.delete_doc(doc_num)
        self.assertEqual(removed_from_docs, result[0])
        self.assertEqual(removed_from_dirs, result[1])
        self.assertNotIn(doc_num, directories.values())


    @parameterized.expand(FIXTURES3)
    def test_delete_doc3(self, doc_num, removed_from_docs, removed_from_dirs):
        current_doc = DocData(documents, directories)
        result = current_doc.delete_doc(doc_num)
        self.assertNotEqual(removed_from_docs, result[0])
        self.assertNotEqual(removed_from_dirs, result[1])
