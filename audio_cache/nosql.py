# import numpy
# from tinydb import TinyDB, Query
#
#
# class CacheTinyDB:
#     def __init__(self):
#         self.db = TinyDB('db.json')
#         self.query = Query()
#
#     def get(self, text: str, speaker: int):
#         res = self.db.search(
#             self.query.text == text and
#             self.query.speaker == speaker
#         )
#         return res
#
#     def save(self, text: str, speaker: int, sampling_rate: int, data:numpy.ndarray):
#         return self.db.insert(
#             {"text": text, "speaker": speaker,
#              "sampling_rate": sampling_rate, "data": data.tolist()}
#         )
