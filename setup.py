#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {# pkglts, pysetup.kwds
# format setup arguments

from os import walk
from os.path import abspath, normpath, splitext
from os.path import join as pj

from setuptools import setup, find_packages


short_descr = "Default template for openalea packages."
readme = open('README.rst').read()
history = open('HISTORY.rst').read()


# find version number in src/oapkg/version.py
version = {}
with open("src/oapkg/version.py") as fp:
    exec(fp.read(), version)

# find packages
pkgs = find_packages('src')

pkg_data = {}

nb = len(normpath(abspath("src/oapkg"))) + 1
data_rel_pth = lambda pth: normpath(abspath(pth))[nb:]

data_files = []
for root, dnames, fnames in walk("src/oapkg"):
    for name in fnames:
        if splitext(name)[-1] in ['.csv', '.ini', '.json', '.rst', '.tpl', '.txt', '.yml']:
            data_files.append(data_rel_pth(pj(root, name)))


pkg_data['oapkg'] = data_files

setup_kwds = dict(
    name='oapkg',
    version=version["__version__"],
    description=short_descr,
    long_description=readme + '\n\n' + history,
    author="revesansparole",
    author_email="revesansparole@gmail.com",
    url='https://github.com/revesansparole/oapkg',
    license='CeCILL-C',
    zip_safe=False,

    packages=pkgs,
    package_dir={'': 'src'},
    
    
    package_data=pkg_data,
    setup_requires=[
        "pytest-runner",
        ],
    install_requires=[
        "pkglts",
        ],
    tests_require=[
        "coverage",
        "pytest",
        "pytest-cov",
        "pytest-mock",
        "sphinx",
        "sphinx_rtd_theme",
        "twine",
        ],
    entry_points={},
    keywords='openalea',
    
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    )
# #}
# change setup_kwds below before the next pkglts tag

setup_kwds['entry_points']['pkglts'] = [
    'oapkg.root = oapkg',
    'oapkg.update_parameters = oapkg.config:update_parameters',
    'oapkg.check = oapkg.config:check',
    'oapkg.require = oapkg.config:require',
    'oapkg.environment_extensions = oapkg.handlers:environment_extensions',
]

# do not change things below
# {# pkglts, pysetup.call
setup(**setup_kwds)
# #}
