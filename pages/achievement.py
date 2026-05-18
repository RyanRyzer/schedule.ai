import streamlit as st

st.title("🏅 Achievement")

achievements = [
    "First Task",
    "7 Days Streak",
    "100 XP",
    "Task Master",
    "Focus Legend"
]

for badge in achievements:

    with st.container(border=True):

        st.write(f"🏆 {badge}")