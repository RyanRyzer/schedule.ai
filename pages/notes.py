import streamlit as st
import sqlite3

if not st.session_state.login:
    st.switch_page("app.py")

conn = sqlite3.connect(
    "planner.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    note TEXT
)
""")

conn.commit()

st.title("📝 Notes")

new_note = st.text_area(
    "Tulis Catatan",
    height=180
)

if st.button(
    "💾 Simpan Catatan",
    use_container_width=True
):

    if new_note.strip() != "":

        cursor.execute("""
        INSERT INTO notes (
            user_id,
            note
        )
        VALUES (?, ?)
        """, (
            st.session_state.user_id,
            new_note
        ))

        conn.commit()

        st.success(
            "✅ Catatan berhasil disimpan."
        )

        st.rerun()

st.divider()

st.subheader("📚 Daftar Catatan")

cursor.execute("""
SELECT id, note
FROM notes
WHERE user_id=?
ORDER BY id DESC
""", (
    st.session_state.user_id,
))

notes = cursor.fetchall()

if len(notes) == 0:

    st.info(
        "Belum ada catatan."
    )

else:

    for note in notes:

        note_id = note[0]
        note_text = note[1]

        with st.container(border=True):

            st.write(note_text)

            col1, col2 = st.columns(2)

            with col1:

                edit_key = f"edit_{note_id}"

                if edit_key not in st.session_state:
                    st.session_state[edit_key] = False

                if not st.session_state[edit_key]:

                    if st.button(
                        "✏️ Edit",
                        key=f"edit_btn_{note_id}",
                        use_container_width=True
                    ):

                        st.session_state[edit_key] = True
                        st.rerun()

                else:

                    edited_note = st.text_area(
                        "Edit Catatan",
                        value=note_text,
                        key=f"edit_area_{note_id}"
                    )

                    save_col1, save_col2 = st.columns(2)

                    with save_col1:

                        if st.button(
                            "✅ Simpan",
                            key=f"save_{note_id}",
                            use_container_width=True
                        ):

                            cursor.execute("""
                            UPDATE notes
                            SET note=?
                            WHERE id=?
                            """, (
                                edited_note,
                                note_id
                            ))

                            conn.commit()

                            st.session_state[edit_key] = False

                            st.success(
                                "Catatan berhasil diupdate."
                            )

                            st.rerun()

                    with save_col2:

                        if st.button(
                            "❌ Batal",
                            key=f"cancel_{note_id}",
                            use_container_width=True
                        ):

                            st.session_state[edit_key] = False
                            st.rerun()

            with col2:

                @st.dialog("Konfirmasi Hapus")
                def popup_delete(note_id):

                    st.error(
                        "Yakin ingin menghapus catatan ini?"
                    )

                    yes_col, no_col = st.columns(2)

                    with yes_col:

                        if st.button(
                            "🔥 Ya, Hapus",
                            key=f"yes_delete_{note_id}",
                            use_container_width=True
                        ):

                            cursor.execute("""
                            DELETE FROM notes
                            WHERE id=?
                            """, (
                                note_id,
                            ))

                            conn.commit()

                            st.success(
                                "🗑️ Catatan berhasil dihapus."
                            )

                            st.rerun()

                    with no_col:

                        if st.button(
                            "❌ Batal",
                            key=f"no_delete_{note_id}",
                            use_container_width=True
                        ):

                            st.rerun()

                if st.button(
                    "🗑️ Hapus",
                    key=f"delete_btn_{note_id}",
                    use_container_width=True
                ):

                    popup_delete(note_id)