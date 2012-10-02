# -*- coding: utf-8 -*-

from static_loader.tests.base_case import BaseCase


class ModelTest(BaseCase):

    def setUp(self):
        super(ModelTest, self).setUp()
        self.static.fill()

    def test_contains(self):
        self.assertTrue('field' in self.static.user.get('single'))
        