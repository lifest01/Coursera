import os
import tempfile

class File:

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        if os.path.exists(path_to_file):
            self.path_to_file = path_to_file
        else:
            file = open(path_to_file, 'w+')

    def read(self):
        file = open(self.path_to_file)
        return file.read()

    def write(self,value):
        with open (self.path_to_file, 'w') as f:
            f.write(value)
            return (len(value))

    def __add__(self, other):
        new_file = File(os.path.join(tempfile.gettempdir(), tempfile.NamedTemporaryFile(suffix='.txt').name))
        new_file.write(self.read() + other.read())
        return new_file

    def __str__(self):
        return self.path_to_file

    def __iter__(self):
        self.count = 0
        with open(self.path_to_file) as fd:
            self.lines = fd.readlines()
        return self


    def __next__(self):
        try:
            line = self.lines[self.count]
            self.count += 1
            return line
        except IndexError:
            raise StopIteration


# file1 = File('text.txt' + '_1')
# file2 = File('text.txt' + '_2')
# print(file1.write('line 1\n'))
# print(file2.write('line 2\n'))
# new_obj = file1 + file2
# print(isinstance(new_obj,File))
# print(new_obj.read())
# print(new_obj)
# for line in new_obj:
#     print(ascii(line))