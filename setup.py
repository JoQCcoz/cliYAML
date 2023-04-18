#! /usr/env/bin python
from setuptools import setup

setup(
    name='cliYAML',
    version='0.1',
    description='Create a multi-level CLI using a YAML file',
    author='Jonathan Bouvette',
    author_email='jonathan.bouvette@gmail.com',
    packages=['cliyaml'],  # same as name
    install_requires=['pyyaml'],  # external packages as dependencies
)
