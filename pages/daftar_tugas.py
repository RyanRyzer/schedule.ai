import streamlit as st
import sqlite3
from database import get_all_tugas

if not st.session_state.login:
    st.switch_page("app.py")

conn = sqlite3.connect(
    "planner.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
SELECT id
FROM users
WHERE username=?
""", (
    st.session_state.username,
))

user = cursor.fetchone()

user_id = user[0]

tasks = get_all_tugas(user_id)

st.title("Daftar Tugas")

if len(tasks) == 0:

    st.info("Belum ada tugas.")

else:

    for task in tasks:

        warna_prioritas = {
            "Rendah": "#22c55e",
            "Sedang": "#facc15",
            "Tinggi": "#ef4444"
        }

        warna_status = {
            "Belum": "#ef4444",
            "Progress": "#3b82f6",
            "Selesai": "#22c55e"
        }

        html_card = f"""
<div style="
background:#111827;
padding:25px;
border-radius:18px;
margin-bottom:20px;
border:1px solid #1f2937;
box-shadow:0 0 15px rgba(0,0,0,0.25);
">

<h2 style="
color:white;
margin-bottom:20px;
">
{task[2]}
</h2>

<p style="color:white;">
📚 Mata Kuliah :
<b>{task[3]}</b>
</p>

<p style="color:white;">
📅 Deadline :
<b>{task[4]}</b>
</p>

<div style="
display:inline-block;
background:{warna_prioritas[task[5]]};
color:white;
padding:10px 18px;
border-radius:999px;
font-weight:700;
margin-top:10px;
margin-right:10px;
">
Prioritas {task[5]}
</div>

<div style="
display:inline-block;
background:{warna_status[task[6]]};
color:white;
padding:10px 18px;
border-radius:999px;
font-weight:700;
margin-top:10px;
">
{task[6]}
</div>

</div>
"""

        st.markdown(html_card, unsafe_allow_html=True)
