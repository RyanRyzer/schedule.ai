import streamlit as st
from database import tambah_tugas
import random

st.title("Tambah Tugas")

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
            st.session_state.user["id"],
            judul,
            matkul,
            str(deadline),
            prioritas,
            status
        )

        st.success("Tugas berhasil ditambahkan.")