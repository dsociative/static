# -*- coding: utf-8 -*-
from static_loader.model import StaticModel

from static_loader.tests.base_case import BaseCase


class StaticTest(BaseCase):
    def test_collections(self):
        self.items_eq(self.loader.items(), ['user', 'tables'])

    def test_split_id_digit(self):
        self.eq(self.loader.split_id('1.json'), '1')

    def test_split_id_string(self):
        self.eq(self.loader.split_id('single.json'), 'single')


class TablesStatic(StaticModel):
    pass


class StaticFillTest(BaseCase):
    def setUp(self):
        super(StaticFillTest, self).setUp()
        self.static = self.loader.fill()

    def test_items(self):
        self.items_eq(self.loader.items(), ['tables', 'user'])

    def test_load_dir(self):
        self.eq(
            dict(self.loader.load_dir('tables')),
            {
                '1': {
                    u'name': u'test_table',
                    u'nested': {u'inner': u'data', u'list': [1, 2, 3]}
                },
                '2': {'1': 1, '2': u'something', '3': u'else'}
            }
        )

    def test_load_single(self):
        single = self.static.user.get('single')
        self.eq(self.static.user, self.static['user'])
        self.eq(single.field, 'this is test field')