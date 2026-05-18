import streamlit as st
import sqlite3
from datetime import datetime

if not st.session_state.login:
    st.switch_page("app.py")

conn = sqlite3.connect(
    "planner.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS discussions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    title TEXT,
    content TEXT,
    category TEXT,
    created_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS discussion_comments (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discussion_id INTEGER,
    username TEXT,
    comment TEXT,
    created_at TEXT
)
""")

conn.commit()

st.title("🌎 Community Hub")

tab1, tab2 = st.tabs([
    "🔥 Semua Diskusi",
    "➕ Buat Topik"
])

with tab2:

    st.subheader("Buat Topik Baru")

    title = st.text_input(
        "Judul Topik"
    )

    category = st.selectbox(
        "Kategori",
        [
            "Santai",
            "Kuliah",
            "Ngoding",
            "Gaming",
            "Teknologi",
            "Random"
        ]
    )

    content = st.text_area(
        "Isi Diskusi",
        height=200
    )

    if st.button(
        "🚀 Publish Topik",
        use_container_width=True
    ):

        if title.strip() != "" and content.strip() != "":

            cursor.execute("""
            INSERT INTO discussions (
                username,
                title,
                content,
                category,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """, (
                st.session_state.username,
                title,
                content,
                category,
                datetime.now().strftime("%Y-%m-%d %H:%M")
            ))

            conn.commit()

            st.success(
                "Topik berhasil dipublish 🔥"
            )

            st.rerun()

with tab1:

    st.subheader("🔥 Community Discussion")

    cursor.execute("""
    SELECT *
    FROM discussions
    ORDER BY id DESC
    """)

    discussions = cursor.fetchall()

    if len(discussions) == 0:

        st.info(
            "Belum ada diskusi."
        )

    else:

        for discussion in discussions:

            discussion_id = discussion[0]
            username = discussion[1]
            title = discussion[2]
            content = discussion[3]
            category = discussion[4]
            created_at = discussion[5]

            cursor.execute("""
            SELECT COUNT(*)
            FROM discussion_comments
            WHERE discussion_id=?
            """, (
                discussion_id,
            ))

            total_comments = cursor.fetchone()[0]

            with st.container(border=True):

                st.subheader(title)

                info1, info2, info3 = st.columns([
                    2,
                    2,
                    2
                ])

                with info1:

                    st.caption(
                        f"👤 {username}"
                    )

                with info2:

                    st.caption(
                        f"🏷️ {category}"
                    )

                with info3:

                    st.caption(
                        f"🕒 {created_at}"
                    )

                st.write(content)

                st.info(
                    f"💬 {total_comments} Komentar"
                )

                comment = st.text_input(
                    "Tulis komentar",
                    key=f"comment_{discussion_id}"
                )

                col1, col2 = st.columns(2)

                with col1:

                    if st.button(
                        "💬 Kirim Komentar",
                        key=f"send_{discussion_id}",
                        use_container_width=True
                    ):

                        if comment.strip() != "":

                            cursor.execute("""
                            INSERT INTO discussion_comments (
                                discussion_id,
                                username,
                                comment,
                                created_at
                            )
                            VALUES (?, ?, ?, ?)
                            """, (
                                discussion_id,
                                st.session_state.username,
                                comment,
                                datetime.now().strftime("%Y-%m-%d %H:%M")
                            ))

                            conn.commit()

                            st.success(
                                "Komentar berhasil dikirim."
                            )

                            st.rerun()

                with col2:

                    if username == st.session_state.username:

                        @st.dialog("Konfirmasi Hapus")
                        def popup_delete():

                            st.error(
                                "Yakin ingin menghapus topik ini?"
                            )

                            yes, no = st.columns(2)

                            with yes:

                                if st.button(
                                    "🔥 Hapus",
                                    key=f"hapus_{discussion_id}",
                                    use_container_width=True
                                ):

                                    cursor.execute("""
                                    DELETE FROM discussions
                                    WHERE id=?
                                    """, (
                                        discussion_id,
                                    ))

                                    cursor.execute("""
                                    DELETE FROM discussion_comments
                                    WHERE discussion_id=?
                                    """, (
                                        discussion_id,
                                    ))

                                    conn.commit()

                                    st.success(
                                        "Diskusi berhasil dihapus."
                                    )

                                    st.rerun()

                            with no:

                                if st.button(
                                    "❌ Batal",
                                    key=f"batal_{discussion_id}",
                                    use_container_width=True
                                ):

                                    st.rerun()

                        if st.button(
                            "🗑️ Hapus Topik",
                            key=f"delete_{discussion_id}",
                            use_container_width=True
                        ):

                            popup_delete()

                st.divider()

                cursor.execute("""
                SELECT username, comment, created_at
                FROM discussion_comments
                WHERE discussion_id=?
                ORDER BY id DESC
                """, (
                    discussion_id,
                ))

                comments = cursor.fetchall()

                if len(comments) == 0:

                    st.caption(
                        "Belum ada komentar."
                    )

                else:

                    for c in comments:

                        with st.container():

                            top1, top2 = st.columns([
                                5,
                                1
                            ])

                            with top1:

                                st.markdown(
                                    f"🔵 **{c[0]}**"
                                )

                            with top2:

                                st.caption(
                                    f"{c[2]}"
                                )

                            st.write(
                                c[1]
                            )

                            st.divider()
