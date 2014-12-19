#!/usr/bin/env python
"""
Track Bugz
-----------

A project management ticketing system.


"""
from setuptools import setup, find_packages

import track_bugz

setup(
    name='trapeze',
    version=track_bugz.__version__,
    description=track_bugz.__doc__,
    long_description=open('README.md').read(),
    packages=find_packages(),
    author='radlws',
    author_email='radzhome@gmail.com',
    url='htt://github.com/radlws/',
    download_url='',
    include_package_data=True,
    install_requires=['django >= 1.7', ],
    platforms='any',
    classifiers=[
        #'Development Status :: 5 - Production/Stable',
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
)
