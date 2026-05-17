import streamlit as st
from database import get_all_tugas
import sqlite3

if not st.session_state.login:
    st.switch_page("app.py")

conn = sqlite3.connect(
    "planner.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
SELECT * FROM users
WHERE username=?
""", (
    st.session_state.username,
))

user = cursor.fetchone()

tasks = get_all_tugas(user[0])

st.title("Daftar Tugas")

if len(tasks) == 0:

    st.info("Belum ada tugas")

else:

    for task in tasks:

        priority_color = "#22c55e"

        if task[5] == "Sedang":
            priority_color = "#f59e0b"

        elif task[5] == "Tinggi":
            priority_color = "#ef4444"

        st.markdown(f"""
        <div style="
            background:linear-gradient(
                145deg,
                #111827,
                #1e293b
            );
            padding:30px;
            border-radius:24px;
            margin-bottom:25px;
            border:1px solid rgba(255,255,255,0.06);
            box-shadow:0 0 25px rgba(0,0,0,0.4);
        ">

            <h2 style="
                color:white;
                margin-bottom:20px;
            ">
                {task[2]}
            </h2>

            <p style="color:white;">
                📚 Mata Kuliah :
                {task[3]}
            </p>

            <p style="color:white;">
                📅 Deadline :
                {task[4]}
            </p>

            <div style="
                display:inline-block;
                background:{priority_color};
                color:white;
                padding:10px 18px;
                border-radius:999px;
                font-weight:700;
                margin-top:10px;
            ">
                Prioritas {task[5]}
            </div>

            <div style="
                margin-top:20px;
                background:#0f2747;
                padding:15px;
                border-radius:12px;
                color:#60a5fa;
            ">
                Status : {task[6]}
            </div>

        </div>
        """, unsafe_allow_html=True)