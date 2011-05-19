#! /usr/bin/env python

from setuptools import setup, find_packages


requirements = [
    "Django >= 1.3",
]


setup(
    name = "django_jquery",   
    version              = version,
    description          = "Django library to static inlcude jquery",
    long_description     = None,
    classifiers          = [],
    keywords             = 'django, jquery',
    author               = 'Allan Davis',
    author_email         = 'cajun.code@gmail.com',
    url                  = 'http://github.com/cajun-code/django_jquery',
    license              = 'BSD',
    packages             = find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data = True,
    scripts              = ['bin/jquery_update'],
    zip_safe             = False,
    install_requires     = requirements,
)