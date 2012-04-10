#!/usr/bin/env python

from setuptools import setup

setup(
    name="hashcache",
    version="0.0.1",
    description="Wrapper for the django cache api to gracefully handle long or non-ascii keys",
    license="MIT",
    author="Yola, Inc.",
    author_email="justin@yola.com",
    url="http://github.com/yola/hashcache",
    packages = ("hashcache",),
    keywords= "django cache library",
    zip_safe = False,
)
