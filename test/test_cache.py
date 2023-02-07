import unittest

import audio_cache


class TestSum(unittest.TestCase):
    def test_cache(self):
        cache = audio_cache.getCache()
        # cache.save("test", 1, b"test")



if __name__ == '__main__':
    unittest.main()
