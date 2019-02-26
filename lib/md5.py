import hashlib
import os


class CalculateMD5(object):
    def __init__(self, storge_path):
        self.path = storge_path
        self.nums = 0
        self.file_dict = {}

    def calculate(self):
        for hierarchy in os.walk(self.path):
            if hierarchy[-1]:
                for filename in hierarchy[-1]:
                    self.nums += 1
                    file = os.path.join(hierarchy[0], filename)
                    m = hashlib.md5()
                    with open(file, 'rb') as fp:
                        while True:
                            data = fp.read(1024)
                            if not data:
                                break
                            m.update(data)
                    self.file_dict[m.hexdigest()] = file
