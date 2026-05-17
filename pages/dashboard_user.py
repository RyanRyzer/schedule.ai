import streamlit as st
import sqlite3
from database import get_all_tugas
from datetime import datetime
import random

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

st.title("Dashboard User")

st.markdown(f"""
<h3 style="
color:white;
margin-bottom:30px;
">
Welcome Back, {st.session_state.username}
</h3>
""", unsafe_allow_html=True)

total_tugas = len(tasks)

selesai = len([
    t for t in tasks
    if t[6] == "Selesai"
])

progress = 0

if total_tugas > 0:
    progress = int((selesai / total_tugas) * 100)

prioritas_tinggi = len([
    t for t in tasks
    if t[5] == "Tinggi"
])

deadline_warning = []

today = datetime.now().date()

for t in tasks:

    try:

        dl = datetime.strptime(
            t[4],
            "%Y-%m-%d"
        ).date()

        sisa = (dl - today).days

        if sisa <= 2 and t[6] != "Selesai":
            deadline_warning.append(t)

    except:
        pass

ai_messages = []

if total_tugas == 0:

    ai_messages.append(
        "🧠 AI mendeteksi belum ada tugas. Saatnya mulai produktif."
    )

if progress >= 70:

    ai_messages.append(
        "🔥 Produktivitas kamu sangat bagus minggu ini."
    )

if progress < 40 and total_tugas > 0:

    ai_messages.append(
        "⚠️ Banyak tugas belum selesai. Fokus pada prioritas utama."
    )

if prioritas_tinggi >= 3:

    ai_messages.append(
        "🚨 Kamu memiliki banyak tugas prioritas tinggi."
    )

if len(deadline_warning) > 0:

    ai_messages.append(
        "⏰ Ada deadline yang mendekat."
    )

if len(ai_messages) == 0:

    ai_messages.append(
        "✅ Semua sistem produktivitas terlihat stabil."
    )

focus_task = None
highest_score = -1

for t in tasks:

    score = 0

    if t[5] == "Tinggi":
        score += 50

    if t[5] == "Sedang":
        score += 25

    if t[6] == "Belum":
        score += 20

    try:

        dl = datetime.strptime(
            t[4],
            "%Y-%m-%d"
        ).date()

        sisa = (dl - today).days

        if sisa <= 2:
            score += 50

        elif sisa <= 5:
            score += 20

    except:
        pass

    if score > highest_score:

        highest_score = score
        focus_task = t

rank = "Beginner"

if progress >= 80:
    rank = "Productivity Master"

elif progress >= 60:
    rank = "Focus Expert"

elif progress >= 40:
    rank = "Active Student"

xp = progress * 10

quotes = [
    "AI memprediksi performa belajar meningkat minggu ini.",
    "Pola tugas menunjukkan kamu lebih produktif malam hari.",
    "AI menyarankan fokus pada 1 tugas utama hari ini.",
    "Kamu memiliki konsistensi belajar yang bagus.",
    "AI mendeteksi progress meningkat dibanding sebelumnya.",
    "Deadline terdekat sebaiknya diselesaikan hari ini.",
    "Prioritas tinggi perlu perhatian lebih cepat.",
]

random_quote = random.choice(quotes)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(f"""
    <div style="
    background:#111827;
    padding:25px;
    border-radius:20px;
    border:1px solid #1f2937;
    ">
    <p style="color:#9ca3af;">Total Tugas</p>
    <h1 style="color:white;">{total_tugas}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div style="
    background:#111827;
    padding:25px;
    border-radius:20px;
    border:1px solid #1f2937;
    ">
    <p style="color:#9ca3af;">Tugas Selesai</p>
    <h1 style="color:white;">{selesai}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div style="
    background:#111827;
    padding:25px;
    border-radius:20px;
    border:1px solid #1f2937;
    ">
    <p style="color:#9ca3af;">Prioritas Tinggi</p>
    <h1 style="color:white;">{prioritas_tinggi}</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns([2, 1])

with left:

    st.markdown("""
    <h2 style="color:white;">
    🧠 AI Assistant Online
    </h2>
    """, unsafe_allow_html=True)

    for msg in ai_messages:

        st.markdown(f"""
        <div style="
        background:#111827;
        padding:18px;
        border-radius:16px;
        margin-bottom:15px;
        border-left:4px solid #7c3aed;
        color:white;
        font-weight:600;
        ">
        {msg}
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    padding:25px;
    border-radius:20px;
    margin-top:20px;
    color:white;
    ">
    <h2>🎯 Focus Mode</h2>
    <p style="font-size:20px;font-weight:700;">
    {focus_task[2] if focus_task else "Tidak ada tugas"}
    </p>
    <p>
    AI merekomendasikan tugas ini untuk dikerjakan terlebih dahulu.
    </p>
    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown(f"""
    <div style="
    background:#111827;
    padding:25px;
    border-radius:20px;
    text-align:center;
    border:1px solid #1f2937;
    ">
    <h3 style="color:white;">🏆 Rank</h3>
    <h2 style="color:#60a5fa;">
    {rank}
    </h2>
    <p style="color:#9ca3af;">
    XP : {xp}
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
    background:#111827;
    padding:25px;
    border-radius:20px;
    border:1px solid #1f2937;
    ">
    <h3 style="color:white;">
    📈 Productivity Score
    </h3>
    <h1 style="
    color:#22c55e;
    ">
    {progress}%
    </h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="color:white;">
📅 Deadline Terdekat
</h2>
""", unsafe_allow_html=True)

sorted_tasks = sorted(
    tasks,
    key=lambda x: x[4]
)

if len(sorted_tasks) == 0:

    st.info("Belum ada tugas.")

else:

    for t in sorted_tasks[:3]:

        warna = "#22c55e"

        if t[5] == "Sedang":
            warna = "#eab308"

        if t[5] == "Tinggi":
            warna = "#ef4444"

        st.markdown(f"""
        <div style="
        background:#0f172a;
        padding:25px;
        border-radius:20px;
        margin-bottom:20px;
        border:1px solid #1f2937;
        ">
        <h2 style="color:white;">
        {t[2]}
        </h2>

        <p style="color:white;">
        📚 Mata Kuliah :
        <b>{t[3]}</b>
        </p>

        <p style="color:white;">
        📅 Deadline :
        <b>{t[4]}</b>
        </p>

        <div style="
        display:inline-block;
        background:{warna};
        color:white;
        padding:10px 18px;
        border-radius:999px;
        font-weight:700;
        margin-top:10px;
        margin-right:10px;
        ">
        Prioritas {t[5]}
        </div>

        <div style="
        display:inline-block;
        background:#2563eb;
        color:white;
        padding:10px 18px;
        border-radius:999px;
        font-weight:700;
        margin-top:10px;
        ">
        {t[6]}
        </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="color:white;">
🚀 Progress Produktivitas
</h2>
""", unsafe_allow_html=True)

st.progress(progress / 100)

st.markdown(f"""
<p style="
color:white;
margin-top:10px;
font-weight:600;
">
{progress}% tugas selesai
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(f"""
<div style="
background:linear-gradient(135deg,#111827,#1e293b);
padding:25px;
border-radius:20px;
border:1px solid #1f2937;
color:white;
">
<h2>
💡 AI Weekly Insight
</h2>

<p style="
font-size:18px;
margin-top:15px;
">
{random_quote}
</p>
</div>
""", unsafe_allow_html=True)
