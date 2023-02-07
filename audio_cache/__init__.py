# from audio_cache.nosql import CacheTinyDB
from audio_cache.sqlite import CacheSqlite


def getCache():
    # sqlite = CacheSqlite()
    # return sqlite
    # return CacheTinyDB()
    return CacheSqlite()
