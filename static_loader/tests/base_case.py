# -*- coding: utf-8 -*-
from ztest import ZTest

from static_loader.static import Static


class BaseCase(ZTest):

    def setUp(self):
        self.static = Static('data')
