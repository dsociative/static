# coding: utf8


def islist(key):
    return ',' in key


class StaticModel(dict):

    def __init__(self, data, id=None):
        self.id = id
        super(StaticModel, self).__init__(self.process(data))

    def __iter__(self):
        return self.iteritems()

    def assign(self, key, value):
        if type(key) in (str, unicode):
            setattr(self, key, value)

    def process_key(self, key):
        if key.isdigit():
            return int(key)
        elif islist(key):
            return tuple(map(self.process_key, key.split(',')))
        else:
            return key

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
