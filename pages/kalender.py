import streamlit as st
from streamlit_calendar import calendar
from database import cursor

st.title("Kalender Tugas")

st.markdown("""
<p style='color:#94a3b8;'>
Kelola jadwal dan deadline tugas anda
</p>
""", unsafe_allow_html=True)

cursor.execute("""
SELECT judul, deadline, prioritas
FROM tugas
WHERE user=?
""", (st.session_state.username,))

data = cursor.fetchall()

events = []

for d in data:

    color = "#22c55e"

    if d[2] == "Sedang":
        color = "#eab308"

    elif d[2] == "Tinggi":
        color = "#ef4444"

    events.append({

        "title": d[0],

        "start": d[1],

        "end": d[1],

        "color": color
    })

calendar_options = {
    "initialView": "dayGridMonth",
    "height": 700,
    "editable": True,
    "selectable": True
}

state = calendar(
    events=events,
    options=calendar_options
)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Keterangan Warna")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("Prioritas Rendah")

with col2:
    st.warning("Prioritas Sedang")

with col3:
    st.error("Prioritas Tinggi")

st.markdown("<br>", unsafe_allow_html=True)

cursor.execute("""
SELECT COUNT(*)
FROM tugas
WHERE status='Belum'
AND user=?
""", (st.session_state.username,))

belum = cursor.fetchone()[0]

if belum >= 5:

    st.warning("""
    AI Suggestion:
    Anda memiliki banyak tugas yang belum selesai.
    Disarankan mulai mengerjakan lebih awal.
    """)

elif belum == 0:

    st.success("""
    AI Suggestion:
    Semua tugas selesai.
    Produktivitas sangat baik
    """)

else:

    st.info("""
    AI Suggestion:
    Produktivitas masih stabil.
    Tetap konsisten mengerjakan tugas.
    """)