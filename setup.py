#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="hashcache",
    version="0.0.1",
    description="Wrapper for the django cache api to gracefully handle long or non-ascii keys",
    license="MIT",
    author="Yola, Inc.",
    author_email="justin@yola.com",
    url="http://github.com/yola/hashcache",
    packages = find_packages(exclude=["tests.*",]),
    keywords= "django cache library",
    zip_safe = False,
)
