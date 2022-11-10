
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
    (['passport - 2207 876234 - Василий Гупкин', 'invoice - 11-2 - Геннадий Покемонов', 'insurance - 10006 - Аристарх Павлов'],)
]

FIXTURES2 = [
    (['invoice - 2207 876234 - Василий Гупкин', 'passport - 11-2 - Геннадий Покемонов', 'insurance - 10006 - Аристарх Павлов'],), (['passport - 2207 876234 - Василий Иванов', 'invoice - 11-2 - Геннадий Покемонов', 'insurance - 10006 - Аристарх Павлов'],)
]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_show_all_docs_info1(self, name_l):
        current_doc = DocData(documents, directories)
        result = current_doc.show_all_docs_info()
        self.assertEqual(name_l, result)

    @parameterized.expand(FIXTURES2)
    def test_show_all_docs_info2(self, name_l):
        current_doc = DocData(documents, directories)
        result = current_doc.show_all_docs_info()
        self.assertNotEqual(name_l, result)
