#!/usr/bin/env python

from distutils.core import setup

setup(name='static loader',
      description='loader for json static data',
      author='dsociative',
      author_email='admin@geektech.ru',
      packages=['static'],
      package_dir={'static': 'static'},
     )
