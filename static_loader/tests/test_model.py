# -*- coding: utf-8 -*-

from static_loader.tests.base_case import BaseCase


class ModelTest(BaseCase):

    def setUp(self):
        super(ModelTest, self).setUp()
        self.static.fill()
        self.model = self.static.user.get('single')

    def test_id(self):
        self.assertEqual(self.model.id, 'single')
        self.assertEqual(self.model.data.get('id'), None)

    def test_get(self):
        self.assertEqual(self.model.get('field'), 'this is test field')

    def test_contains(self):
        self.assertTrue('field' in self.model)

    def test_iteration(self):
        fields = []
        for field, value in self.model:
            fields.append(field)

        self.assertEqual(fields, ['field'])
        