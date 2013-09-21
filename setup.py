#!/usr/bin/python

from setuptools import setup

setup(
    name = 'quantile',
    version = '0.0.1',
    author = 'Matt T. Proud',
    author_email = 'matt.proud@gmail.com',
    description = ("Python Implementation of Graham Cormode and S. "
                   "Muthukrishnan's Effective Computation of Biased "
                   "Quantiles over Data Streams in ICDE'05"),
    license = 'Apache License 2.0',
    url = 'https://github.com/matttproud/python_quantile_estimation',
    packages = ['com', 'com/matttproud', 'com/matttproud/quantile'],
    platforms = 'Platform Independent',
    classifiers = ['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Topic :: Scientific/Engineering :: Mathematics'])
