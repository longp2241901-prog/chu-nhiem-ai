import streamlit as st
from google import genai

st.set_page_config(page_title="Gemini Test")

st.title("🤖 Test Gemini API")

api_key = st.text_input(
    "Nhập Gemini API Key",
    type="password"
)

if st.button("Gọi Gemini"):

    if not api_key:
        st.warning("Hãy nhập API Key.")
        st.stop()

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Hãy giới thiệu bản thân trong đúng 1 câu."
        )

        st.success("Gọi thành công!")
        st.write(response.text)

    except Exception as e:
        st.exception(e)
