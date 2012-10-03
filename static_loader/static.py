# coding: utf8
import json
import os
import sys
import traceback

from static_loader.model import StaticModel


def trace():
    traceback.print_exc(file=sys.stderr)


class Static(object):

    def __init__(self, path, mapper={}):
        self.path = os.path.abspath(path)
        self.mapper = mapper

    def fill(self):
        for collection in self.collections():
            setattr(self, collection, self.models(collection))

    def collections(self):
        for d in os.listdir(self.path):
            if not d.startswith('.'):
                yield d

    def join(self, *items):
        return os.path.join(self.path, *items)

    def files(self, collection):
        path = self.join(collection)
        for filename in os.listdir(path):
            if filename.endswith('.json'):
                yield filename

    def split_id(self, file):
        name = os.path.splitext(file)[0]
        if name.isdigit():
            return int(name)
        else:
            return name

    def load(self, collection, file):
        assign_model = self.mapper.get(collection, StaticModel)
        path = self.join(collection, file)

        try:
            data = json.loads(open(path).read())
        except:
            trace()
            raise Exception('Error in static file %s' % path)

        return assign_model(data, id=self.split_id(file))

    def models(self, collection):
        result = {}

        for file in self.files(collection):
            model = self.load(collection, file)
            result[model.id] = model

        return result
