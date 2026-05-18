import streamlit as st

st.title("🏫 Study Room")

users = [
    "Ryan",
    "Kevin",
    "Nanda",
    "Alicia"
]

st.subheader("User Online")

for user in users:

    st.write(f"🟢 {user}")