# coding: utf8
import json


def islist(key):
    return ',' in key


class StaticModel(dict):

    def __init__(self, data, id=None):
        self.id = id
        super(StaticModel, self).__init__(self.process(data))

    def json(self):
        return json.dumps(self)

    def assign(self, key, value):
        self.__dict__[key] = value

    def process_key(self, key):
        if key.isdigit():
            return int(key)
        elif islist(key):
            return tuple(map(self.process_key, key.split(',')))
        else:
            return key

    def process_item(self, key, value):
        return self.process_key(key), self.process_value(key, value)

    def process(self, data):
        for key, value in data.iteritems():
            key, value = self.process_item(key, value)
            self.assign(key, value)
            yield key, value

    def process_list(self, key, value):
        for item in value:
            yield self.process_value(key, item)

    def process_value(self, key, value):
        if type(value) is dict:
            return StaticModel(value, key)
        elif type(value) is list:
            return list(self.process_list(key, value))
        else:
            return value
