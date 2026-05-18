import streamlit as st
from database import cursor
import pandas as pd

st.title("Dashboard Admin")

st.subheader(
    f"Welcome Admin, {st.session_state.username}"
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

cursor.execute("""
SELECT COUNT(*)
FROM users
""")
total_user = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM tugas
""")
total_tugas = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM tugas
WHERE status='Selesai'
""")
tugas_selesai = cursor.fetchone()[0]

with col1:

    st.metric(
        "Total User",
        total_user
    )

with col2:

    st.metric(
        "Total Tugas",
        total_tugas
    )

with col3:

    st.metric(
        "Tugas Selesai",
        tugas_selesai
    )

st.markdown("---")

st.subheader("Data User")

cursor.execute("""
SELECT username, role
FROM users
""")

users = cursor.fetchall()

if users:

    df_user = pd.DataFrame(
        users,
        columns=[
            "Username",
            "Role"
        ]
    )

    st.dataframe(
        df_user,
        use_container_width=True
    )

else:

    st.warning("Belum ada user")

st.markdown("---")

st.subheader("Aktivitas Tugas Terbaru")

cursor.execute("""
SELECT judul, matkul, status
FROM tugas
ORDER BY id DESC
LIMIT 5
""")

tugas = cursor.fetchall()

if not tugas:

    st.info("Belum ada tugas")

else:

    for t in tugas:

        with st.container(border=True):

            st.markdown(
                f"### {t[0]}"
            )

            st.write(
                f"Mata Kuliah : {t[1]}"
            )

            st.write(
                f"Status : {t[2]}"
            )
