#!/usr/bin/env python
"""
Copyright 2012 DISQUS
Copyright 2013 Parse.ly, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys

from setuptools import setup, find_packages

from kafka import __version__

try:
    import multiprocessing
except ImportError:
    pass

install_requires = [
]

lint_requires = [
    'pep8',
    'pyflakes'
]

tests_require = ['kazoo', 'mock', 'nose', 'unittest2', 'python-snappy']
dependency_links = []
setup_requires = []
if 'nosetests' in sys.argv[1:]:
    setup_requires.append('nose')

setup(
    name='kafka',
    version=__version__,
    author='Keith Bourgoin',
    author_email='pykafka-user@googlegroups.com',
    url='https://github.com/Parsely/pykafka',
    description='Featureful Kafka client.',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
    extras_require={
        'test': tests_require,
        'all': install_requires + tests_require,
        'docs': ['sphinx'] + tests_require,
        'lint': lint_requires
    },
    dependency_links=dependency_links,
    zip_safe=False,
    test_suite='nose.collector',
    include_package_data=True,
)
