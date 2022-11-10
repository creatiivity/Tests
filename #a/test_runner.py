
import os
import json
import unittest
from docs_data.documents_db import documents, directories


if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), "tests", "data", "docs_in_tests.json"), "w", encoding='utf8') as fp:
        json.dump(documents, fp, ensure_ascii=False)
    with open(os.path.join(os.getcwd(),"tests", "data", "dirs_in_tests.json"), "w", encoding='utf8') as fp2:
        json.dump(directories, fp2, ensure_ascii=False)

    loader = unittest.TestLoader()
    start_dir = 'tests/'
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)
    