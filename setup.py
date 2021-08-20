# -*- coding: utf-8 -*-
"""
setup.py script
"""

import io
from collections import OrderedDict
from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    README = f.read()

setup(
    name='giovannicuriel.disguise',
    version='1.0.0',
    url='http://github.com/giovannicuriel/disguise',
    project_urls=OrderedDict((
        ('Code', 'https://github.com/giovannicuriel/disguise.git'),
        ('Issue tracker', 'https://github.com/giovannicuriel/disguise/issues'),
    )),
    license='BSD-3-Clause',
    author='Giovanni Curiel dos Santos',
    author_email='giovannicuriel@gmail.com',
    maintainer='Giovanni Curiel dos Santos',
    description='GUI for dis module (disassembler) from Python',
    long_description=README,
    packages=["giovannicuriel.disguise"],
    include_package_data=True,
    zip_safe=False,
    platforms=[any],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "PyQt5==5.15.0",
        "PyQt5-sip==12.8.0"
    ]
)
