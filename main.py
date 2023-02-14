import os
import sys

from tts.SuTTS import SuTTS

# moegoe_module = os.path.join(os.path.abspath(os.path.dirname(__file__)), "moegoe")
# print("moegoe_module", moegoe_module)
# sys.path.append(moegoe_module)
#
# from tts.SuTTS import SuTTS
# CACHE_MODE = False
# 2792 佐倉杏子
# 2842 美樹さやか
佐倉杏子 = 2792
美樹さやか = 2842

"""
ギットハブ アクションのビルドが達成されました。
ギットハブアクションのビルドが完了しました！！！
"""
text = """
    ギットハブ アクションのビルドが成功しました！
    """

if __name__ == '__main__':
    su_tts = SuTTS()
    su_tts.speak(text, 美樹さやか)
    # audio, sampling_rate = suTTS.text_to_speech(佐倉杏子, text)
    # sd.play(audio, sampling_rate, blocking=True)
