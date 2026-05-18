import streamlit as st
import sqlite3
from database import tambah_tugas
import random
import time

if not st.session_state.login:
    st.switch_page("app.py")

st.title("Tambah Tugas")

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

ai_quotes = [
    "Fokus pada 1 tugas utama agar hasil lebih maksimal.",
    "Deadline dekat? Prioritaskan tugas paling penting.",
    "Multitasking berlebihan bisa menurunkan produktivitas.",
    "AI mendeteksi pola tugas menumpuk di akhir minggu.",
    "Kerjakan tugas sulit saat energi masih penuh.",
    "Gunakan reminder untuk menghindari lupa deadline.",
    "Progress kecil tetap lebih baik daripada tidak mulai.",
    "Prioritas tinggi sebaiknya selesai maksimal H-2 deadline."
]

success_quotes = [
    "Tugas berhasil ditambahkan ke planner.",
    "Nice! Deadline berhasil disimpan.",
    "AI Planner berhasil mengatur tugas baru kamu.",
    "Tugas masuk ke sistem dan siap dipantau.",
    "Produktivitas +1 🚀",
    "Reminder tugas berhasil dibuat.",
    "Tugas tersimpan dengan aman.",
    "Semangat! Tugas baru berhasil ditambahkan."
]

random_tip = random.choice(ai_quotes)

left, right = st.columns([2.2, 1])

with left:

    judul = st.text_input(
        "Judul Tugas",
        placeholder="Contoh : Final Project Sistem Cerdas"
    )

    matkul = st.text_input(
        "Mata Kuliah",
        placeholder="Contoh : Sistem Cerdas"
    )

    deadline = st.date_input("Deadline")

    prioritas = st.selectbox(
        "Prioritas",
        [
            "Rendah",
            "Sedang",
            "Tinggi"
        ]
    )

    status = st.selectbox(
        "Status",
        [
            "Belum",
            "Progress",
            "Selesai"
        ]
    )

with right:

    st.markdown("## AI Planner")

    st.info("AI membantu mengatur deadline dan prioritas tugas.")

    st.success("Produktivitas meningkat ketika tugas tersusun rapi.")

    st.warning("Hindari menumpuk tugas dalam satu hari.")

st.markdown(f"""
<div style="
background:#111827;
padding:18px;
border-radius:16px;
margin-top:20px;
border-left:4px solid #7c3aed;
font-weight:600;
">
AI Suggestion : {random_tip}
</div>
""", unsafe_allow_html=True)

if st.button("Tambah Tugas", use_container_width=True):

    if judul == "" or matkul == "":
        st.error("Isi semua form terlebih dahulu.")

    else:

        tambah_tugas(
            user_id,
            judul,
            matkul,
            str(deadline),
            prioritas,
            status
        )

        random_success = random.choice(success_quotes)

        st.balloons()

        st.markdown(f"""
        <div style="
        margin-top:20px;
        background:linear-gradient(90deg,#2563eb,#7c3aed);
        padding:18px;
        border-radius:16px;
        color:white;
        font-size:18px;
        font-weight:700;
        text-align:center;
        box-shadow:0 0 20px rgba(124,58,237,0.5);
        ">
        ✅ {random_success}
        </div>
        """, unsafe_allow_html=True)

        time.sleep(1.5)

        st.rerun()
