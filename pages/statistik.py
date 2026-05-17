import streamlit as st
from database import cursor
import pandas as pd
import plotly.express as px

st.title("Smart Insights")

st.markdown("""
Analisis cerdas terhadap pola belajar dan produktivitas pengguna
""")

cursor.execute("""
SELECT matkul, status, prioritas
FROM tugas
WHERE user=?
""", (st.session_state.username,))

data = cursor.fetchall()

if not data:

    st.warning(
        "Belum ada data tugas"
    )

else:

    df = pd.DataFrame(
        data,
        columns=[
            "Matkul",
            "Status",
            "Prioritas"
        ]
    )

    st.markdown("---")

    st.subheader("Distribusi Status Tugas")

    status_count = (
        df["Status"]
        .value_counts()
        .reset_index()
    )

    status_count.columns = [
        "Status",
        "Jumlah"
    ]

    fig1 = px.pie(
        status_count,
        names="Status",
        values="Jumlah",
        hole=0.5
    )

    fig1.update_layout(
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=450
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Mata Kuliah Paling Sibuk")

    matkul_count = (
        df["Matkul"]
        .value_counts()
        .reset_index()
    )

    matkul_count.columns = [
        "Matkul",
        "Jumlah"
    ]

    fig2 = px.bar(
        matkul_count,
        x="Matkul",
        y="Jumlah",
        text_auto=True
    )

    fig2.update_layout(
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=500
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("AI Productivity Score")

    total = len(df)

    selesai = len(
        df[df["Status"] == "Selesai"]
    )

    tinggi = len(
        df[df["Prioritas"] == "Tinggi"]
    )

    score = (
        (selesai * 20)
        + ((total - tinggi) * 10)
    )

    if score > 100:
        score = 100

    st.progress(score / 100)

    st.write(
        f"Score Produktivitas : {score}/100"
    )

    st.markdown("---")

    st.subheader("AI Smart Recommendation")

    if score >= 80:

        st.success("""
        Performa belajar sangat baik.

        Rekomendasi:
        - Pertahankan konsistensi
        - Mulai eksplor skill baru
        - Tingkatkan kualitas belajar
        """)

    elif score >= 60:

        st.info("""
        Produktivitas cukup stabil.

        Rekomendasi:
        - Fokus pada tugas prioritas tinggi
        - Kurangi penundaan kecil
        - Tingkatkan manajemen waktu
        """)

    elif score >= 40:

        st.warning("""
        Produktivitas mulai menurun.

        Rekomendasi:
        - Gunakan reminder lebih aktif
        - Fokus satu tugas per sesi
        - Buat target harian
        """)

    else:

        st.error("""
        Produktivitas rendah.

        Rekomendasi:
        - Susun ulang jadwal belajar
        - Hindari multitasking
        - Gunakan kalender secara rutin
        - Kurangi distraksi
        """)

    st.markdown("---")

    st.subheader("AI Burnout Detection")

    if tinggi >= 5:

        st.error("""
        Sistem mendeteksi potensi burnout.

        Penyebab:
        - terlalu banyak tugas prioritas tinggi

        Solusi:
        - istirahat teratur
        - cicil tugas bertahap
        - jangan mengerjakan semua sekaligus
        """)

    else:

        st.success("""
        Kondisi belajar masih stabil.
        Tidak ada indikasi burnout tinggi.
        """)