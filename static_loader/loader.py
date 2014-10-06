# coding: utf8
import json
import os
import sys
import traceback

from static_loader.model import StaticModel


def trace():
    traceback.print_exc(file=sys.stderr)


class Loader(object):

    def __init__(self, path, mapper={}):
        self.path = os.path.abspath(path)
        self.mapper = mapper

    def items(self):
        for d in os.listdir(self.path):
            if not d.startswith('.'):
                yield d

    def load_file(self, collection, file):
        path = self.join(collection, file)

        try:
            return json.loads(open(path).read())
        except:
            trace()
            raise Exception('Error in static file %s' % path)

    def load(self, collection, file):
        return self.load_file(collection, file)

    def load_dir(self, name):
        path = self.join(name)
        for filename in os.listdir(path):
            if filename.endswith('.json'):
                yield self.split_id(filename), self.load(name, filename)

    def fill_gen(self):
        for item in self.items():
            yield item, dict(self.load_dir(item))

    def fill(self):
        return StaticModel(dict(self.fill_gen()))

    def join(self, *items):
        return os.path.join(self.path, *items)

    def split_id(self, file):
        return os.path.splitext(file)[0]
