# -*- coding: utf-8 -*-
from static_loader.model import StaticModel

from static_loader.tests.base_case import BaseCase


class StaticTest(BaseCase):

    def test_collections(self):
        self.assertEqual(list(self.static.collections()),
                         ['tables', 'user'])

    def test_split_id_digit(self):
        self.assertEqual(self.static.split_id('1.json'), 1)

    def test_split_id_string(self):
        self.assertEqual(self.static.split_id('single.json'),
                         'single')


class TablesStatic(StaticModel):
    pass


class StaticFillTest(BaseCase):

    def setUp(self):
        super(StaticFillTest, self).setUp()
        self.static.fill()

    def test_load_single(self):
        single = self.static.user.get('single')
        self.assertEqual(single.field, 'this is test field')

    def test_load_custom_class(self):
        self.static.mapper['tables'] = TablesStatic
        self.static.fill()
        self.assertIsInstance(self.static.tables[1], TablesStatic)