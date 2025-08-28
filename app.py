import streamlit as st
from gtts import gTTS
from utils import pitch_shift
import os
from datetime import datetime

st.title("🎛️ 声質変換付き 音声生成アプリ")

text = st.text_area("話したい内容を入力してください", height=150)
voice_type = st.selectbox("声質を選んでください", ["通常", "高め（妖精風）", "低め（ロボット風）"])
lang = st.selectbox("言語", ["日本語", "英語"])
lang_code = "ja" if lang == "日本語" else "en"

if st.button("音声を生成"):
    if text.strip():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"voice_{timessstamp}.mp3"
        tts = gTTS(text=text, lang=lang_code)
        tts.save(base_filename)

        # 声質変換
        if voice_type == "高め（妖精風）":
            final_path = pitch_shift(base_filename, semitones=5)
        elif voice_type == "低め（ロボット風）":
            final_path = pitch_shift(base_filename, semitones=-5)
        else:
            final_path = base_filename

        # 再生とダウンロード
        with open(final_path, "rb") as f:
            st.audio(f.read(), format="audio/mp3")
            st.download_button("音声ファイルをダウンロード", f, file_name=final_path, mime="audio/mp3")
    else:
        st.warning("テキストを入力してください。")
