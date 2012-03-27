from testify import *
from flexmock import flexmock
from hashcache import Hashcache

class TestHashcache(TestCase):
    """Test the Hashcache class"""
    
    # MD5 hashes used in these examples:
    # 'my_key1': 'aaf08daa8898fe4fecaec3e586748f1f',
    # 'my_key2': '6a3d7f4295a5cd351d746fad80bb6c90',
    # u'\xed': '9defdf606bd9e5ba7861b78c0b50ecb2'
    
    @setup
    def stub_cache(self):
        self.cache = flexmock(
            get=lambda key: None,
            set=lambda key, *args: True)
        self.hashcache = Hashcache(self.cache)
    
    def test_raises_if_no_cache(self):
        assert_raises(AssertionError, Hashcache, None)
    
    def test_gets_from_cache_using_hashed_key(self):
        self.cache.should_receive('get').with_args('aaf08daa8898fe4fecaec3e586748f1f').once.and_return('val1').ordered
        self.cache.should_receive('get').with_args('6a3d7f4295a5cd351d746fad80bb6c90').once.and_return('val2').ordered
        assert self.hashcache.get('my_key1') == 'val1'
        assert self.hashcache.get('my_key2') == 'val2'
    
    def test_sets_cache_using_hashed_key(self):
        self.cache.should_receive('set').with_args('aaf08daa8898fe4fecaec3e586748f1f', 'val1').once
        self.hashcache.set('my_key1', 'val1')
    
    def test_sets_cache_using_hashed_key_with_expiration(self):
        self.cache.should_receive('set').with_args('6a3d7f4295a5cd351d746fad80bb6c90', 'val2', 30).once
        self.hashcache.set('my_key2', 'val2', 30)
    
    def test_handles_non_ascii_keys(self):
        self.cache.should_receive('set').with_args('9defdf606bd9e5ba7861b78c0b50ecb2', 'val').once
        self.hashcache.set(u'\xed', 'val')
