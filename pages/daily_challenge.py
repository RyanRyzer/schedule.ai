import streamlit as st

st.title("🔥 Daily Challenge")

challenge = [
    "Selesaikan 3 tugas",
    "Belajar 2 jam",
    "Login hari ini",
    "Focus mode 25 menit"
]

for c in challenge:

    st.checkbox(c)