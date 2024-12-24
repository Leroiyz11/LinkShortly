import streamlit as st

# Redirect to YouTube
youtube_url = "https://www.youtube.com/your_channel"  # Ganti dengan URL YouTube Anda

st.markdown(f"""
    <meta http-equiv="refresh" content="0; url={youtube_url}">
    <p>Redirecting to <a href="{youtube_url}">YouTube</a>...</p>
""", unsafe_allow_html=True)
