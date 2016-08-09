#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


NAME = 'django-queries-test'
URL = 'https://github.com/AndreaCrotti/django-queries-test'
DESCRIPTION = "Mixin for Django TestCase to do more assertions on the queries executed"
AUTHOR = "Andrea Crotti"
AUTHOR_EMAIL = "andrea.crotti.0@gmail.com"

setup(
    name=NAME,
    version='0.1',
    url=URL,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=['django_queries_test'],
    install_requires=['django>=1.7,<=1.10'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
