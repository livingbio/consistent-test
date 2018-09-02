import io
import os
from os.path import dirname, exists, join

# follow the django storage API,
# therefore, we can use django storage as backend as well
# ref: https://docs.djangoproject.com/en/1.11/ref/files/storage/


class TestCaseStroage(object):
    def __init__(self, path):
        self.TEST_ROOT = path

    def save(self, name, value):
        path = self.path(name)

        if not exists(dirname(path)):
            os.makedirs(dirname(path))

        with io.open(path, 'w', encoding='utf8') as ofile:
            ofile.write(value)

    def open(self, name):
        with io.open(self.path(name), encoding="utf8") as ifile:
            return ifile.read()

    def path(self, name):
        name = join(self.TEST_ROOT, name)
        return name

    def delete(self, name):
        path = self.path(name)
        os.remove(path)

    def exists(self, name):
        path = self.path(name)
        return os.path.exists(path)

    def listdir(self, name):
        path = self.path(name)
        return os.listdir(path)
