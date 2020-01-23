import os


class NameDatabase:
    def __init__(self):
        self.database = {}
        self.database_keys = []

    def set(self, key, value):
        if key not in self.database_keys:
            self.database_keys.append(key)

        self.database[key] = value

    def add(self, old, new):
        self.database[old] = new

    def del_value(self, key):
        self.database.pop(key, None)

    def get(self, key):
        return self.database[key]

    def update(self):
        # removes same key value and set keys from instance database
        updated_database = {}
        if self.database:
            for k, v in self.database.items():
                if k != v and k not in self.database_keys:
                    updated_database[k] = v

        self.database = updated_database

    def print_database(self, instance=None):
        if self.database:
            for k, v in self.database.items():
                k = os.path.basename(k)
                v = os.path.basename(v)

                instance.text_browser_print(f'\t{k} --> {v}')
        else:
            instance.text_browser_print('\tNo Files to rename.')


class NoNameError(Exception):
    pass
