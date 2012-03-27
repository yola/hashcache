from django.core.cache import cache as cache_impl
from django.utils.encoding import smart_str

import hashlib

class Hashcache(object):
    """
    Wrapper for django.core.cache.cache that hashes the keys to avoid key
    length errors. Maybe eventually it will do other cool things.
    
    You can optionally pass your own cache module to the initializer as long
    as it conforms to the get/set interface of the django cache module.
    
    >>> from yolango.util.hashcache import Hashcache
    >>> cache = Hashcache()
    >>> cache.set('my_key', 'hello, world!', 30)
    >>> cache.get('my_key')
    'hello, world!'
    """
    
    def __init__(self, cache = cache_impl):
        assert cache
        self.cache = cache
    
    def get(self, key):
        """Hash the key and retrieve it from the cache"""
        return self.cache.get(self._hashed(key))
    
    def set(self, key, *args):
        """Hash the key and set it in the cache"""
        return self.cache.set(self._hashed(key), *args)
    
    def _hashed(self, key):
        return hashlib.new("md5", smart_str(key)).hexdigest()
