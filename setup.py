#!/usr/bin/env python

from setuptools import setup


setup(name='static loader',
      description='loader for json static data',
      author='dsociative',
      author_email='admin@geektech.ru',
      packages=['static_loader'],
      dependency_links=[
          "http://github.com/dsociative/ztest/tarball/master#egg=ztest-0.0.0",
      ],
      install_requires=[
          'ztest'
      ],
      version='2.0'
)
