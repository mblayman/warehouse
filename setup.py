#!/usr/bin/env python
# Copyright 2013 Donald Stufft
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, division, print_function

import fnmatch
import os

from setuptools import setup, find_packages


about = {}
with open("warehouse/__about__.py") as fp:
    exec(fp.read(), about)


def recursive_glob(path, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches


setup(
    name=about["__title__"],
    version=about["__version__"],

    description=about["__summary__"],
    long_description=open("README.rst").read(),
    license=about["__license__"],
    url=about["__uri__"],

    author=about["__author__"],
    author_email=about["__email__"],

    classifiers=[
        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],

    packages=find_packages(),
    package_data={
        "warehouse": ["*.yml"] + recursive_glob("static", "*.*"),
        "warehouse.legacy": ["templates/*/*.html"],
        "warehouse.migrations": ["*.mako", "versions/*.py"],
    },

    install_requires=[
        "alembic",
        "babel",
        "enum34",
        "Jinja2",
        "psycopg2cffi-compat>=1.1",
        "PyYAML",
        "recliner>=0.3.1",
        "redis",
        "six",
        "SQLAlchemy",
        "sqlalchemy-citext>=1.2.0",
        "webassets-py3k==0.9.dev",
        "Werkzeug",
    ],

    entry_points={
        "console_scripts": [
            "warehouse = warehouse.__main__:main",
        ],
    },

    zip_safe=False,
)