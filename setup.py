# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip.req import parse_requirements
import pip.download

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

requirements = list(parse_requirements('requirements.txt',
                                       session=pip.download.PipSession()))

install_requires = [str(r.req) for r in requirements]

setup(
    name="cirrus-email",
    version="0.0.5",
    description="AWS SES Email helpers for Project Cirrus",
    license="MIT",
    author="pebble {code}",
    packages=find_packages(),
    install_requires=install_requires,
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
