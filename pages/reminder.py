import streamlit as st
from database import cursor, conn
from datetime import datetime

st.title("Smart Reminder")

st.markdown("""
<p style='color:#94a3b8;'>
Pengingat tugas dan deadline otomatis
</p>
""", unsafe_allow_html=True)

cursor.execute("""
SELECT id, judul, deadline, prioritas, status
FROM tugas
WHERE user=?
AND status='Belum'
ORDER BY deadline ASC
""", (st.session_state.username,))

tugas = cursor.fetchall()

if not tugas:

    st.success(
        "Tidak ada reminder aktif"
    )

else:

    today = datetime.today()

    st.subheader("Reminder Aktif")

    for t in tugas:

        deadline = datetime.strptime(
            t[2],
            "%Y-%m-%d"
        )

        sisa_hari = (
            deadline - today
        ).days

        color = "#22c55e"
        status_text = "Masih Aman"

        if sisa_hari <= 7:
            color = "#eab308"
            status_text = "Deadline Dekat"

        if sisa_hari <= 3:
            color = "#ef4444"
            status_text = "Deadline Mendesak"

        st.markdown(f"""
        <div style="
            background:{color};
            padding:25px;
            border-radius:18px;
            margin-bottom:20px;
            box-shadow:0 4px 20px rgba(0,0,0,0.3);
        ">

        <h3 style='color:white;'>
        {t[1]}
        </h3>

        <p style='color:white; font-size:16px;'>
        Deadline : {t[2]}
        </p>

        <p style='color:white; font-size:16px;'>
        Prioritas : {t[3]}
        </p>

        <p style='color:white; font-size:16px;'>
        Status Reminder : {status_text}
        </p>

        <p style='color:white; font-size:16px;'>
        Sisa Hari : {sisa_hari} hari
        </p>

        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button(
                f"Tandai Selesai #{t[0]}"
            ):

                cursor.execute("""
                UPDATE tugas
                SET status='Selesai'
                WHERE id=?
                """, (t[0],))

                conn.commit()

                st.success(
                    "Tugas ditandai selesai"
                )

                st.rerun()

        with col2:

            if st.button(
                f"Hapus Reminder #{t[0]}"
            ):

                cursor.execute("""
                DELETE FROM tugas
                WHERE id=?
                """, (t[0],))

                conn.commit()

                st.warning(
                    "Reminder berhasil dihapus"
                )

                st.rerun()

        with col3:

            if sisa_hari <= 3:

                st.error(
                    "Segera kerjakan!"
                )

            elif sisa_hari <= 7:

                st.warning(
                    "Jangan ditunda"
                )

            else:

                st.success(
                    "Masih santai"
                )

st.markdown("---")

st.subheader("AI Reminder Insight")

cursor.execute("""
SELECT COUNT(*)
FROM tugas
WHERE status='Belum'
AND user=?
""", (st.session_state.username,))

belum = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM tugas
WHERE prioritas='Tinggi'
AND status='Belum'
AND user=?
""", (st.session_state.username,))

tinggi = cursor.fetchone()[0]

if belum == 0:

    st.success("""
    Semua tugas selesai.

    AI Insight:
    Produktivitas sangat baik dan tidak ada deadline aktif.
    """)

elif tinggi >= 5:

    st.error("""
    AI Warning:
    Terlalu banyak tugas prioritas tinggi.

    Rekomendasi:
    - Fokus pada deadline terdekat
    - Kerjakan tugas prioritas tinggi terlebih dahulu
    - Hindari menambah tugas baru
    """)

elif belum >= 10:

    st.warning("""
    AI Detection:
    Jumlah tugas belum selesai cukup banyak.

    Rekomendasi:
    - Gunakan teknik pomodoro
    - Buat target harian
    - Gunakan kalender secara rutin
    """)

else:

    st.info("""
    AI Analysis:
    Deadline masih dalam kondisi terkendali.

    Rekomendasi:
    Tetap konsisten mengerjakan tugas sedikit demi sedikit.
    """)