import streamlit as st

st.title("🔔 Notification Center")

notif = [
    "Deadline tugas AI besok",
    "Achievement baru terbuka",
    "XP bertambah +20",
    "Streak hampir hilang"
]

for n in notif:

    st.info(n)