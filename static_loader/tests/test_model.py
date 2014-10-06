# -*- coding: utf-8 -*-

import json
from static_loader.model import StaticModel

from static_loader.tests.base_case import BaseCase


class ModelTest(BaseCase):
    def setUp(self):
        super(ModelTest, self).setUp()
        self.static = self.loader.fill()
        self.model = self.static.user.get('single')

    def test_process_key(self):
        self.eq(self.model.process_key('1'), 1)

    def test_process_key_range(self):
        self.eq(self.model.process_key('1,2'), (1, 2))
        self.eq(self.model.process_key('1,2,Name'), (1, 2, 'Name'))

    def test_process_value_dict(self):
        model = self.model.process_value('new_key', {'1': '2'})
        self.eq(model.id, 'new_key')
        self.isinstance(model, StaticModel)

    def test_json(self):
        self.static['name'] = u'Вася'
        self.eq(self.model.json(), json.dumps(self.model, ensure_ascii=False))
        self.eq(self.static.json(), json.dumps(self.static, ensure_ascii=False))

    def test_id(self):
        self.eq(self.model.id, 'single')
        self.eq(self.model.get('id'), None)

    def test_get(self):
        self.eq(self.model.get('field'), 'this is test field')
        self.eq(self.model.field, 'this is test field')

    def test_dict(self):
        self.eq(self.model, {'field': 'this is test field'})

    def test_contains(self):
        self.true('field' in self.model)

    def test_iteration(self):
        fields = []
        for field, value in self.model:
            fields.append(field)

        self.eq(fields, ['field'])

    def test_key(self):
        self.model = self.static.tables.get(2)
        self.eq(self.model, {1: 1, 2: 'something', 3: 'else'})
