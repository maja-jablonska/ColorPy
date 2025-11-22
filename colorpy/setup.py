#!/usr/bin/env python
'''
setup.py - Setup script to install the ColorPy package.

To install the ColorPy package:
From the directory in which the ColorPy distribution was unpacked, run:

python -m pip install .

You should now be able to say 'import colorpy' in your programs and use the package.
'''

from pathlib import Path

from setuptools import setup

data_files = [
    'README.txt',
    'COPYING.txt',
    'COPYING.LESSER.txt',
    'license.txt',
    'ColorPy.html',
]

long_description = (Path(__file__).parent / 'README.txt').read_text(encoding='utf-8')

setup (
    name='colorpy',
    version='0.1.2',
    description='Color calculations with physical descriptions of light spectra',
    long_description=long_description,
    long_description_content_type='text/plain',
    author='Mark Kness',
    author_email='mkness@alumni.utexas.net',
    url='http://markkness.net/colorpy/',
    license='GNU Lesser GPL Version 3',
    package_dir={'colorpy': ''},
    packages=['colorpy'],
    package_data={'colorpy': data_files},
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
