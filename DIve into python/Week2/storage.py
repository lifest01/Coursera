import argparse
import json
import os
import tempfile

STORAGE_FILE = os.path.join(tempfile.gettempdir(), 'storage.data')


class Storage:
    def __init__(self):
        if not os.path.isfile(STORAGE_FILE): 
            self.storage = dict()
        else:
            with open(STORAGE_FILE) as f:
                self.storage = json.load(f)

    def save(self):
        with open(STORAGE_FILE, 'w') as f:
            json.dump(self.storage, f)

    def add(self, key, value):
        if key not in self.storage:
            self.storage[key] = list()
        self.storage[key].append(value)

    def get(self, key):
        if not os.path.exists(STORAGE_FILE):
            return None
        if key in self.storage:
            return self.storage[key]


def main():
    argparser = argparse.ArgumentParser(description='')
    argparser.add_argument('-k', '--key', help='key', action='store', dest='key', required=True)
    argparser.add_argument('-v', '--value', help='value', action='store', dest='value')
    args = argparser.parse_args()
    storage = Storage()
    if args.value is None:
        a = storage.get(args.key)
        if a is not None:
            print(*a,sep=', ')
        else:
            print(a)
    else:
        storage.add(args.key, args.value)
        storage.save()


if __name__ == "__main__":
    main()
