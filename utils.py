# 音声加工関数

from pydub import AudioSegment
from scipy.signal import resample
import numpy as np

def pitch_shift(audio_path, semitones):
    audio = AudioSegment.from_file(audio_path)
    samples = np.array(audio.get_array_of_samples())
    factor = 2 ** (semitones / 12)
    new_length = int(len(samples) / factor)
    new_samples = resample(samples, new_length)
    new_audio = audio._spawn(new_samples.astype(np.int16))
    new_audio = new_audio.set_frame_rate(int(audio.frame_rate * factor))
    output_path = f"shifted_{semitones}.mp3"
    new_audio.export(output_path, format="mp3")
    return output_path
