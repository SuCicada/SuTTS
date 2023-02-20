import sounddevice

from sutts.inference.so_vits_svc import SoVitsSvcTTS

text = """
大丈夫です、深呼吸をして、リラックスしてください。
自分自身に優しく接して、ストレスを減らすためにできることを考えましょう
"""

import unittest
class TestSoVitsSvc(unittest.TestCase):
    def test_get_audio(self):
        text = """
        大丈夫です、深呼吸をして、リラックスしてください。
        自分自身に優しく接して、ストレスを減らすためにできることを考えましょう
        """
        so_vits_svc = SoVitsSvcTTS()
        sampling_rate, audio = so_vits_svc.get_audio(text)
        self.assertTrue(len(audio) > 0)
        self.assertTrue(sampling_rate > 0)
        sounddevice.play(audio, sampling_rate, blocking=True)
