# from audio_cache.nosql import CacheTinyDB
import os

from cache.sqlite import CacheSqlite


class CacheConfig:
    USE_CACHE = bool(os.environ.get("USE_CACHE", True))
    USE_CACHE_INFERENCE_AUDIO = bool(os.environ.get("USE_CACHE_INFERENCE_AUDIO", True))



connect_cache = {}


def newCache():
    print("USE_CACHE", CacheConfig.USE_CACHE)
    print("USE_CACHE_INFERENCE_AUDIO", CacheConfig.USE_CACHE_INFERENCE_AUDIO)
    # sqlite = CacheSqlite()
    # return sqlite
    # return CacheTinyDB()
    if CacheConfig.USE_CACHE_INFERENCE_AUDIO:
        cache = connect_cache.setdefault("sqlite", CacheSqlite())
        return cache
    else:
        return NoCache()


class NoCache:
    def get(self, text, speaker):
        return None

    def save(self, text, speaker, sampling_rate, data):
        pass
