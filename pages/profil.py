import streamlit as st
from database import cursor, conn

st.title("Profil User")

st.markdown("---")

col1, col2 = st.columns([1,2])

with col1:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=150
    )

    st.markdown(f"""
    ### {st.session_state.username}
    
    Smart Study Planner User
    """)

with col2:

    st.subheader("Edit Profil")

    new_username = st.text_input(
        "Username Baru",
        value=st.session_state.username
    )

    new_password = st.text_input(
        "Password Baru",
        type="password"
    )

    confirm_password = st.text_input(
        "Konfirmasi Password",
        type="password"
    )

    if st.button("Simpan Perubahan"):

        if new_username == "":

            st.warning(
                "Username tidak boleh kosong"
            )

        elif (
            new_password != confirm_password
            and new_password != ""
        ):

            st.error(
                "Konfirmasi password tidak cocok"
            )

        else:

            cursor.execute("""
            SELECT *
            FROM users
            WHERE username=?
            """, (new_username,))

            check_user = cursor.fetchone()

            if (
                check_user
                and new_username
                != st.session_state.username
            ):

                st.error(
                    "Username sudah digunakan"
                )

            else:

                if new_password == "":

                    cursor.execute("""
                    UPDATE users
                    SET username=?
                    WHERE username=?
                    """, (
                        new_username,
                        st.session_state.username
                    ))

                else:

                    cursor.execute("""
                    UPDATE users
                    SET username=?, password=?
                    WHERE username=?
                    """, (
                        new_username,
                        new_password,
                        st.session_state.username
                    ))

                conn.commit()

                st.session_state.username = (
                    new_username
                )

                st.success(
                    "Profil berhasil diperbarui"
                )

st.markdown("---")

st.subheader("Statistik Akun")

col3, col4, col5 = st.columns(3)

cursor.execute("""
SELECT COUNT(*)
FROM tugas
WHERE user=?
""", (st.session_state.username,))

total = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM tugas
WHERE status='Selesai'
AND user=?
""", (st.session_state.username,))

selesai = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM tugas
WHERE prioritas='Tinggi'
AND user=?
""", (st.session_state.username,))

prioritas = cursor.fetchone()[0]

with col3:

    st.metric(
        "Total Tugas",
        total
    )

with col4:

    st.metric(
        "Tugas Selesai",
        selesai
    )

with col5:

    st.metric(
        "Prioritas Tinggi",
        prioritas
    )