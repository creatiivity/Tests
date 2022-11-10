from documents_app.launcher import secretary_program_start
from docs_data.documents_db import documents, directories


if __name__ == '__main__':
    secretary_program_start(documents, directories)

