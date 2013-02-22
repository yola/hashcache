# Hashcache

A wrapper for [django's low-level cache api][1] that cleans and hashes the
keys to get around encoding and key length issues when using picky cache
stores (like memcached...).

## Normal Usage

    >>> from hashcache import hashcache
    >>> hashcache.set('my_key', 'hello, world!', 30)
    >>> hashcache.get('my_key')
    'hello, world!'

## Advanced usage

If you want to get crazy, you can pass in your own cache module that conforms
to django's cache api:

    >>> from hashcache import Hashcache
    >>> cache = Hashcache(my_special_cache)
    >>> cache.set('my_key', 'hello, world!', 30)
    >>> cache.get('my_key')
    'hello, world!'

## Tests

Tests are written using the [Testify][2] testing framework. To run them,
from the root of the project, install the development dependencies:

    pip install -r dev_requirements.txt

and run:

    testify tests

[1]:https://docs.djangoproject.com/en/dev/topics/cache/?from=olddocs#the-low-level-cache-api
[2]:https://github.com/Yelp/Testify
[3]:https://www.yola.com/

## Everything else

Written and used by the folks at Yola. Check out our [free website][3] builder today.
