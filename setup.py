#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import re
import sys

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    readme = ''


package = 'contentful_management'
requirements = [
    'requests>=2.20.0,<3.0',
    'python-dateutil',
    'importlib-metadata==4.13.0',
]
test_requirements = [
    'vcrpy',
    'tox',
    'coverage'
]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


def get_author(package):
    """
    Return package author as listed in `__author__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__author__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


def get_email(package):
    """
    Return package email as listed in `__email__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__email__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


# python setup.py publish
if sys.argv[-1] == 'publish':
    os.system("python3 -m pip install --upgrade build")
    os.system("python3 -m build")
    os.system("python3 -m pip install --upgrade twine")
    os.system("python3 -m twine upload dist/*")
    args = {'version': get_version(package)}
    print("Pushing tags to GitHub:")
    os.system("git tag -a %(version)s -m 'version %(version)s'" % args)
    os.system("git push --tags")
    os.system("git push")
    sys.exit()


setup(
    name='contentful_management',
    version=get_version(package),
    description='Contentful Management API Client',
    long_description=readme,
    author=get_author(package),
    author_email=get_email(package),
    url='https://github.com/contentful/contentful-management.py',
    packages=[
        'contentful_management',
    ],
    package_dir={'contentful_management': 'contentful_management'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='contentful management cma cms content',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

    ],
    test_suite='tests',
    tests_require=test_requirements
)
