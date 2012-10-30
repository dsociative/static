# coding: utf8


class StaticModel(object):

    def __init__(self, data, id=None):
        self.id = id
        self.data = self.process(data)
        self.store = {}
        self.get = self.data.get

    def __contains__(self, name):
        return name in self.data

    def __iter__(self):
        return self.data.iteritems()

    def assign(self, key, value):
        if type(key) in (str, unicode):
            setattr(self, key, value)

    def process_key(self, key):
        return key if not key.isdigit() else int(key)

    def process_item(self, key, value):
        return self.process_key(key), self.process_value(value)

    def process(self, data):
        rt = {}
        for key, value in data.iteritems():
            key, value = self.process_item(key, value)
            rt[key] = value
            self.assign(key, value)
        return rt

    def process_value(self, value):
        if type(value) is dict:
            return StaticModel(value)
        elif type(value) is list:
            rt = []
            for item in value:
                rt.append(self.process_value(item))
            return rt
        else:
            return value
