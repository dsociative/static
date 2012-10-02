# -*- coding: utf-8 -*-
from unittest import TestCase

from static_loader.static import Static


class BaseCase(TestCase):

    def setUp(self):
        self.static = Static('data')
