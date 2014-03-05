#!/usr/bin/python3

"""
Setup file for Skeleton
"""
try:
  from setuptools import setup
except ImportError:
  from distutils.com import setup

config = {
  'description': 'My New Project',
  'author': 'Benjamin Lehman',
  'URL' : 'My URL',
  'download URL': 'where to get this',
  'author email': 'your email',
  'version': '0.1',
  'install requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'projectname'
  }

  setup(**config)
