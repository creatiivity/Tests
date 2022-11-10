
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
    ('55', 'passport', 'Alex Ivanov', '3', False),
    ('150', 'ticket', 'Ivan Ivanov', '2', False)
]

FIXTURES2 = [
    ('11-2', 'invoice', 'Геннадий Покемонов', '3', True),
    ('10006', 'insurance', 'Аристарх Павлов', '2', True)
]

FIXTURES3 = [
    ('100', 'passport', 'Геннадий Покемонов', '3', True),
    ('15', 'insurance', 'Alex Petrov', '2', True)
]

FIXTURES4 = [
    ('100', 'passport', 'Геннадий Покемонов', '5', False),
    ('151', 'insurance', 'Alex Petrov', '7', False)
]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_add_new_doc_documents1(self, new_doc_n, new_doc_t, new_doc_own, new_doc_sh, doc_already_exists):
        current_doc = DocData(documents, directories)
        result = current_doc.add_new_doc(new_doc_n, new_doc_t, new_doc_own, new_doc_sh)
        self.assertIn({"type": new_doc_t, "number": new_doc_n, "name": new_doc_own}, documents)
        self.assertEqual(doc_already_exists, result[0])


    @parameterized.expand(FIXTURES2)
    def test_add_new_doc_documents2(self, new_doc_n, new_doc_t, new_doc_own, new_doc_sh, doc_already_exists):
        current_doc = DocData(documents, directories)
        result = current_doc.add_new_doc(new_doc_n, new_doc_t, new_doc_own, new_doc_sh)
        self.assertEqual(doc_already_exists, result[0])

    @parameterized.expand(FIXTURES3)
    def test_add_new_doc_documents3(self, new_doc_n, new_doc_t, new_doc_own, new_doc_sh, doc_must_be_shelved):
        current_doc = DocData(documents, directories)
        result = current_doc.add_new_doc(new_doc_n, new_doc_t, new_doc_own, new_doc_sh)
        self.assertEqual(doc_must_be_shelved, result[1])

    @parameterized.expand(FIXTURES4)
    def test_add_new_doc_documents4(self, new_doc_n, new_doc_t, new_doc_own, new_doc_sh, doc_must_be_shelved):
        current_doc = DocData(documents, directories)
        result = current_doc.add_new_doc(new_doc_n, new_doc_t, new_doc_own, new_doc_sh)
        self.assertNotIn(new_doc_sh, directories.keys())
        self.assertEqual(doc_must_be_shelved, result[1])

