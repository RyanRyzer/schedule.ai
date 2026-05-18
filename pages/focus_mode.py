import streamlit as st
import time

st.title("🎯 Focus Mode")

minutes = st.slider("Durasi Focus", 1, 60, 25)

if st.button("Mulai Focus Session"):

    placeholder = st.empty()

    for i in range(minutes * 60, -1, -1):

        mins = i // 60
        secs = i % 60

        placeholder.metric(
            "Sisa Waktu",
            f"{mins:02}:{secs:02}"
        )

        time.sleep(1)

    st.success("Focus session selesai 🔥")