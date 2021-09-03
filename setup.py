#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup


def check_setuptools_features():
    import pkg_resources
    try:
        list(pkg_resources.parse_requirements('foo~=1.0'))
    except ValueError:
        exit('Your Python distribution comes with an incompatible version '
             'of `setuptools`. Please run:\n'
             ' sudo pip install --upgrade setuptools\n'
             'and then run this command again')


def read_file(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as r:
        return r.read()


# check if setuptools is up to date
check_setuptools_features()

README = read_file("README.rst")

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []
test_deps = [
    "pytest>=3.1",
    "pytest-cov",
    "pytest-timeout"
]

setup(
    name="luma.examples",
    author="Richard Hull",
    author_email="richard.hull@destructuring-bind.org",
    description="Examples for the luma libraries.",
    long_description=README,
    license="MIT",
    keywords="raspberry orange banana pi rpi opi sbc oled lcd led display screen spi i2c",
    url="https://github.com/rm-hull/luma.examples",
    python_requires='>=3.6, <4',
    install_requires=[
        "luma.core>=1.17.1",
        "luma.emulator>=1.3.0",
        "luma.oled>=3.6.0",
        "luma.lcd>=2.5.0",
        "luma.led_matrix>=1.5.0",
        "argcomplete"
    ],
    setup_requires=pytest_runner,
    tests_require=test_deps,
    extras_require={
        'docs': [
            'sphinx >= 1.5.1'
        ],
        'qa': [
            'rstcheck',
            'flake8'
        ],
        'test': test_deps
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: System :: Hardware",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]
)
