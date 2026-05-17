import streamlit as st
from database import cursor

st.title("Dashboard User")

st.subheader(
    f"Welcome Back, {st.session_state.username} "
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

cursor.execute("""
SELECT COUNT(*)
FROM tugas
WHERE user=?
""", (st.session_state.username,))

total_tugas = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM tugas
WHERE status='Selesai'
AND user=?
""", (st.session_state.username,))

tugas_selesai = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM tugas
WHERE prioritas='Tinggi'
AND user=?
""", (st.session_state.username,))

prioritas_tinggi = cursor.fetchone()[0]

with col1:

    st.metric(
        "Total Tugas",
        total_tugas
    )

with col2:

    st.metric(
        "Tugas Selesai",
        tugas_selesai
    )

with col3:

    st.metric(
        "Prioritas Tinggi",
        prioritas_tinggi
    )

st.markdown("---")

st.subheader("Deadline Terdekat")

cursor.execute("""
SELECT judul, deadline, prioritas
FROM tugas
WHERE user=?
ORDER BY deadline ASC
LIMIT 5
""", (st.session_state.username,))

deadlines = cursor.fetchall()

if not deadlines:

    st.info("Belum ada tugas")

else:

    for tugas in deadlines:

        with st.container(border=True):

            st.markdown(
                f"### {tugas[0]}"
            )

            st.write(
                f"Deadline : {tugas[1]}"
            )

            st.write(
                f"Prioritas : {tugas[2]}"
            )

st.markdown("---")

st.subheader("Progress Produktivitas")

if total_tugas > 0:

    progress = (
        tugas_selesai / total_tugas
    )

    st.progress(progress)

    st.write(
        f"{int(progress * 100)}% tugas selesai"
    )

else:

    st.progress(0)

    st.write(
        "Belum ada progress"
    )