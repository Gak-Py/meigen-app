import streamlit as st
import requests
from translate import Translator

st.title("今日の一言名言")

if st.button("名言を表示"):
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()[0]
            quote = data["q"]
            author = data["a"]
            text = data["h"]

            # 英語から日本語に
            translator = Translator(to_lang="ja")
            quote_j = translator.translate(text)
            st.markdown(text, unsafe_allow_html=True)
            st.markdown(quote_j, unsafe_allow_html=True)
        else:
            st.error("名言の取得に失敗しました。")
    except Exception as e:
        st.error(f"エラーが発生しました。 {e}")

