# -*- coding: utf-8 -*-
from ztest import ZTest

from static_loader.loader import Loader


class BaseCase(ZTest):

    def setUp(self):
        self.loader = Loader('data')
