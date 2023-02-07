import os
import sys

from torch import LongTensor, no_grad

from moegoe.MoeGoe import get_label_value, get_label, get_text
from moegoe.models import SynthesizerTrn
from moegoe.utils import load_checkpoint, get_hparams_from_file


class SuTTS:
    model: str
    config: str
    speakers: list

    def __init__(self, model, config):
        self.model = model
        self.config = config
        self.init()

    def init(self):
        sys.argv[0] = os.path.abspath(sys.argv[0])
        hps_ms = get_hparams_from_file(self.config)
        n_speakers = hps_ms.data.n_speakers if 'n_speakers' in hps_ms.data.keys() else 0
        n_symbols = len(hps_ms.symbols) if 'symbols' in hps_ms.keys() else 0
        self.speakers = hps_ms.speakers if 'speakers' in hps_ms.keys() else ['0']
        use_f0 = hps_ms.data.use_f0 if 'use_f0' in hps_ms.data.keys() else False
        emotion_embedding = hps_ms.data.emotion_embedding if 'emotion_embedding' in hps_ms.data.keys() else False
        self.sampling_rate = hps_ms.data.sampling_rate

        net_g_ms = SynthesizerTrn(
            n_symbols,
            hps_ms.data.filter_length // 2 + 1,
            hps_ms.train.segment_size // hps_ms.data.hop_length,
            n_speakers=n_speakers,
            emotion_embedding=emotion_embedding,
            **hps_ms.model)
        _ = net_g_ms.eval()
        load_checkpoint(self.model, net_g_ms)

        self.hps_ms = hps_ms
        self.net_g_ms = net_g_ms
        self.n_symbols = n_symbols
        self.emotion_embedding = emotion_embedding

    def text_prepare(self, text: str):
        text = text.replace('\n', '')
        if not text.startswith("[JA]"):
            text = "[JA]" + text + "[JA]"
        return text

    def text_to_speech(self, text: str, speaker_id: int):
        net_g_ms = self.net_g_ms
        n_symbols = self.n_symbols
        emotion_embedding = self.emotion_embedding
        sampling_rate = self.sampling_rate

        text = self.text_prepare(text)
        if n_symbols != 0:
            if not emotion_embedding:
                length_scale, text = get_label_value(
                    text, 'LENGTH', 1, 'length scale')
                noise_scale, text = get_label_value(
                    text, 'NOISE', 0.667, 'noise scale')
                noise_scale_w, text = get_label_value(
                    text, 'NOISEW', 0.8, 'deviation of noise')
                cleaned, text = get_label(text, 'CLEANED')

                stn_tst = get_text(text, self.hps_ms, cleaned=cleaned)

                # 2792
                print(self.speakers[speaker_id])
                # speaker_id = speaker_ids  # get_speaker_id('Speaker ID: ')
                # out_path = "a.wav"  # input('Path to save: ')

                with no_grad():
                    x_tst = stn_tst.unsqueeze(0)
                    x_tst_lengths = LongTensor([stn_tst.size(0)])
                    sid = LongTensor([speaker_id])
                    audio = net_g_ms.infer(x_tst, x_tst_lengths, sid=sid, noise_scale=noise_scale,
                                           noise_scale_w=noise_scale_w, length_scale=length_scale)[0][
                        0, 0].data.cpu().float().numpy()
                # print(out_path, sampling_rate, audio)
                return audio, sampling_rate
                # sd.play(audio, sampling_rate, blocking=True)

                # write(out_path, hps_ms.data.sampling_rate, audio)
                # print('Successfully saved!')
