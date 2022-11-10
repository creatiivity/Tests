
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
    [{'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'}], [{'Геннадий Покемонов', 'Аристарх Павлов', 'Василий Гупкин'}]
]

FIXTURES2 = [
    [{'Аристарх Павлов', 'Алексей Иванов', 'Геннадий Покемонов', 'Василий Гупкин'}], [{'Аристарх Павлов', 'Геннадий Покемонов'}]
]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_get_all_doc_owners_names1(self, names):
        current_doc = DocData(documents, directories)
        result = current_doc.get_all_doc_owners_names()
        self.assertEqual(names, result)

    @parameterized.expand(FIXTURES2)
    def test_get_all_doc_owners_names2(self, names):
        current_doc = DocData(documents, directories)
        result = current_doc.get_all_doc_owners_names()
        self.assertNotEqual(names, result)
