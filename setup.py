#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    author="Alexander Lewzey",
    author_email='a.lewzey@hotmail.co.uk',
    python_requires='>=3.5',
    description="A collection of general purpose helper modules",
    entry_points={
        'console_scripts': [
            'imgtk=imgtk.cli:main',
        ],
    },
    install_requires=[
        'Pillow',
        'matplotlib',
    ],
    license="BSD license",
    keywords='imgtk',
    name='imgtk',
    packages=find_packages(include=['imgtk', 'imgtk.*']),
    test_suite='tests',
    url='https://github.com/alexlewzey/my_helpers',
    version='0.1.0',
)
