# coding: utf8


class StaticModel(object):

    def __init__(self, data):
        self.data = data
        self.process(data)

    def assign(self, key, value):
        setattr(self, key, value)

    def process_item(self, key, value):
        return self.assign(key, self.process_value(value))

    def process(self, data):
        for key, value in data.iteritems():
            self.process_item(key, value)

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
