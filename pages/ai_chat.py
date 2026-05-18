import streamlit as st

st.title("💬 AI Chat Assistant")

msg = st.chat_input("Tanya sesuatu...")

if msg:

    with st.chat_message("user"):

        st.write(msg)

    with st.chat_message("assistant"):

        st.write(
            "Coba prioritaskan tugas dengan deadline tercepat."
        )