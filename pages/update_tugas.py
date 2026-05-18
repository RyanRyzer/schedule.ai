import streamlit as st
import sqlite3
from datetime import datetime
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
SELECT id
FROM users
WHERE username=?
""", (
    st.session_state.username,
))

user = cursor.fetchone()

user_id = user[0]

tasks = get_all_tugas(user_id)

st.title("✏️ Update Tugas")

if len(tasks) == 0:

    st.info("Belum ada tugas.")

else:

    pilihan = {
        f"{t[2]} - {t[4]}": t
        for t in tasks
    }

    selected = st.selectbox(
        "📌 Pilih Tugas",
        list(pilihan.keys())
    )

    task = pilihan[selected]

    with st.container(border=True):

        st.subheader(f"📌 {task[2]}")

        st.write(f"📚 Mata Kuliah : {task[3]}")
        st.write(f"📅 Deadline Saat Ini : {task[4]}")
        st.write(f"🔥 Prioritas : {task[5]}")
        st.write(f"📊 Status : {task[6]}")

    st.divider()

    st.subheader("🛠️ Form Update")

    deadline = st.date_input(
        "Ubah Deadline",
        value=datetime.strptime(task[4], "%Y-%m-%d")
    )

    status = st.selectbox(
        "Ubah Status",
        ["Belum", "Progress", "Selesai"],
        index=["Belum", "Progress", "Selesai"].index(task[6])
    )

    st.divider()

    st.subheader("👀 Preview Perubahan")

    with st.container(border=True):

        st.write(f"📌 Judul Tugas : {task[2]}")
        st.write(f"📅 Deadline Baru : {deadline}")
        st.write(f"📊 Status Baru : {status}")

    @st.dialog("Konfirmasi Update")
    def popup_update():

        st.write(
            "Yakin ingin menyimpan perubahan?"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "✅ Ya, Simpan",
                use_container_width=True
            ):

                update_tugas_data(
                    task[0],
                    task[2],
                    task[3],
                    str(deadline),
                    task[5],
                    status
                )

                st.success(
                    "✅ Tugas berhasil diperbarui."
                )

                st.balloons()
                st.rerun()

        with col2:

            if st.button(
                "❌ Batal",
                use_container_width=True
            ):

                st.rerun()

    @st.dialog("Konfirmasi Hapus")
    def popup_hapus():

        st.error(
            "Data akan dihapus permanen."
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🔥 Ya, Hapus",
                use_container_width=True
            ):

                hapus_tugas(task[0])

                st.success(
                    "🗑️ Tugas berhasil dihapus."
                )

                st.rerun()

        with col2:

            if st.button(
                "❌ Tidak Jadi",
                use_container_width=True
            ):

                st.rerun()

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💾 Simpan Perubahan",
            use_container_width=True
        ):

            popup_update()

    with col2:

        if st.button(
            "🗑️ Hapus Tugas",
            use_container_width=True
        ):

            popup_hapus()