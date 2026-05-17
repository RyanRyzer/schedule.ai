import streamlit as st
import sqlite3

from database import (
    get_all_tugas,
    update_tugas_data,
    hapus_tugas
)

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

st.title("Update Tugas")

if len(tasks) == 0:

    st.info("Belum ada tugas")

else:

    pilihan = {
        f"{t[2]} - {t[4]}": t
        for t in tasks
    }

    selected = st.selectbox(
        "Pilih Tugas",
        list(pilihan.keys())
    )

    task = pilihan[selected]

    judul = st.text_input(
        "Judul",
        value=task[2]
    )

    matkul = st.text_input(
        "Mata Kuliah",
        value=task[3]
    )

    deadline = st.text_input(
        "Deadline",
        value=task[4]
    )

    prioritas = st.selectbox(
        "Prioritas",
        ["Rendah", "Sedang", "Tinggi"],
        index=["Rendah", "Sedang", "Tinggi"].index(task[5])
    )

    status = st.selectbox(
        "Status",
        ["Belum", "Progress", "Selesai"],
        index=["Belum", "Progress", "Selesai"].index(task[6])
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Update Tugas",
            use_container_width=True
        ):

            update_tugas_data(
                task[0],
                judul,
                matkul,
                deadline,
                prioritas,
                status
            )

            st.success("Tugas berhasil diupdate")
            st.rerun()

    with col2:

        if st.button(
            "Hapus Tugas",
            use_container_width=True
        ):

            hapus_tugas(task[0])

            st.success("Tugas berhasil dihapus")
            st.rerun()