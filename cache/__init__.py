# from audio_cache.nosql import CacheTinyDB
from cache.sqlite import CacheSqlite

USE_CACHE = True
USE_CACHE_INFERENCE_AUDIO = True

connect_cache = {}

def newCache():
    # sqlite = CacheSqlite()
    # return sqlite
    # return CacheTinyDB()
    if USE_CACHE_INFERENCE_AUDIO:
        cache = connect_cache.setdefault("sqlite", CacheSqlite())
        return cache
    else:
        return NoCache()


class NoCache:
    def get(self, text, speaker):
        return None

    def save(self, text, speaker, sampling_rate, data):
        pass
