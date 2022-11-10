
class DocData:
    def __init__(self, documents, directories):
        self.documents = documents
        self.directories = directories

    # command 'p'
    def get_doc_owner_name(self, user_doc_number):
        for doc in self.documents:
            if user_doc_number == doc['number']:
                return doc['name']
        return None

    # command 'ap'
    def get_all_doc_owners_names(self):
        users_list = []
        for doc in self.documents:
            users_list.append(doc.get('name'))
        return set(users_list)

    # command 'l'
    def show_all_docs_info(self):
        doc_detailed_info = []
        for doc in self.documents:
            doc_type = doc['type']
            doc_number = doc['number']
            doc_owner_name = doc['name']
            doc_detailed_info.append(f'{doc_type} - {doc_number} - {doc_owner_name}')
        return doc_detailed_info

    # command 's'
    def get_doc_shelf(self, user_doc_number):
        for k, v in self.directories.items():
            if user_doc_number in v:
                return k
        return None

    # command 'a'
    def add_new_doc(self, new_doc_n, new_doc_t, new_doc_own, new_doc_sh):
        doc_already_exists = False
        doc_must_be_shelved = False
        for doc in self.documents:
            if new_doc_n == doc['number'] and new_doc_t == doc['type'] and new_doc_own == doc['name']:
                    doc_already_exists = True
        if not doc_already_exists:
            self.documents.append({"type": new_doc_t, "number": new_doc_n, "name": new_doc_own})

        for k, v in self.directories.items():
            if str(new_doc_sh) == k:
                doc_must_be_shelved = True
        if doc_must_be_shelved:
            self.directories[new_doc_sh].append(new_doc_n)

        return [doc_already_exists, doc_must_be_shelved]

    # command 'd'
    def delete_doc(self, delete_document):
        removed_from_docs = False
        removed_from_dirs = False
        for doc in self.documents:
            if delete_document == doc['number']:
                self.documents.remove(doc)
                removed_from_docs = True

        for k, v in self.directories.items():
            if delete_document in v:
                v.remove(delete_document)
                removed_from_dirs = True

        return removed_from_docs, removed_from_dirs

    # command 'm'
    def move_doc_to_shelf(self, move_doc, move_shelf):
        no_such_doc = True
        no_such_shelf = True
        for k, v in self.directories.items():
            if move_doc in v:
                no_such_doc = False
                prev_shelf = k
            if str(move_shelf) == k:
                no_such_shelf = False
        if no_such_doc or no_such_shelf:
            return no_such_doc, no_such_shelf
        else:
            self.directories[prev_shelf].remove(move_doc)
            self.directories[move_shelf].append(move_doc)
            return no_such_doc, no_such_shelf

    # command 'as'
    def add_new_shelf(self, new_shelf):
        shelf_must_be_added = True
        for k, v in self.directories.items():
            if str(new_shelf) == k:
                shelf_must_be_added = False
                return shelf_must_be_added
        self.directories[new_shelf] = []
        return shelf_must_be_added
