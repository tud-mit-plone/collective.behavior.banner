# -*- coding: utf-8 -*-
"""Installer for the collective.behavior.banner package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='collective.behavior.banner',
    version='0.1',
    description="A behavior to create sliders with banners",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone, Dexterity, behavior',
    author='Philip Bauer',
    author_email='bauer@starzel.de',
    url='http://pypi.python.org/pypi/collective.behavior.banner',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.behavior'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone',
        'setuptools',
        'plone.app.dexterity [relations]',
        'plone.directives.form',
        'plone.formwidget.contenttree',
        'plone.app.relationfield',
        'z3c.relationfield'
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
