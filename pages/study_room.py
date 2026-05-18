import streamlit as st
import sqlite3
from datetime import datetime, timedelta

if not st.session_state.login:
    st.switch_page("app.py")

conn = sqlite3.connect(
    "planner.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS online_users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    last_active TEXT
)
""")

conn.commit()

now = datetime.now()

cursor.execute("""
INSERT OR REPLACE INTO online_users (
    username,
    last_active
)
VALUES (?, ?)
""", (
    st.session_state.username,
    now.strftime("%Y-%m-%d %H:%M:%S")
))

conn.commit()

online_limit = now - timedelta(seconds=60)

cursor.execute("""
SELECT username, last_active
FROM online_users
""")

all_users = cursor.fetchall()

online_users = []

for user in all_users:

    username = user[0]

    last_active = datetime.strptime(
        user[1],
        "%Y-%m-%d %H:%M:%S"
    )

    if last_active >= online_limit:

        online_users.append(username)

st.title("🏫 Study Room")

st.caption(
    "Realtime active users in community."
)

st.divider()

if len(online_users) == 0:

    st.info(
        "Belum ada user online."
    )

else:

    cols = st.columns(4)

    for index, user in enumerate(online_users):

        with cols[index % 4]:

            st.markdown(f"""
<div style="
background:#0f172a;
padding:18px;
border-radius:18px;
text-align:center;
border:1px solid rgba(255,255,255,0.06);
margin-bottom:15px;
">

<div style="
font-size:40px;
margin-bottom:10px;
">
🟢
</div>

<div style="
font-size:16px;
font-weight:600;
color:white;
">
{user}
</div>

<div style="
font-size:12px;
color:#22c55e;
margin-top:6px;
">
ONLINE
</div>

</div>
""", unsafe_allow_html=True)
