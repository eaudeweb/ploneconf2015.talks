# -*- coding: utf-8 -*-
"""Installer for the ploneconf2015.talks package."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='ploneconf2015.talks',
    version='1.0',
    description="Talks for Plone Conference 2015",
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3.4",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='talks ploneconf 2015',
    author='Razvan Chitu',
    author_email='razvan.ch95@gmail.com',
    url='https://github.com/eaudeweb/ploneconf2015.talks',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['ploneconf2015'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
        'plone.api',
        'setuptools',
        'z3c.jbot',
        'plone.app.dexterity',
        'plone.app.relationfield',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
