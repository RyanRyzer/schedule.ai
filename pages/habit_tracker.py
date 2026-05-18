import streamlit as st

st.title("📈 Habit Tracker")

habits = [
    "Belajar",
    "Olahraga",
    "Membaca",
    "Ngoding"
]

for habit in habits:

    st.checkbox(habit)