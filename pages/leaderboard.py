import streamlit as st

st.title("🏆 Leaderboard")

data = [
    ("Ryan", 1520, "Schedule King"),
    ("Alicia", 1280, "Time Wizard"),
    ("Kevin", 990, "Focus Master"),
    ("Nanda", 740, "Focus Master"),
    ("Dion", 510, "Productive")
]

st.subheader("Top Productivity Users")

for i, user in enumerate(data, start=1):

    with st.container(border=True):

        st.write(f"#{i} - {user[0]}")
        st.write(f"⭐ XP : {user[1]}")
        st.write(f"👑 Rank : {user[2]}")