import streamlit as st
from database import cursor
import plotly.express as px
import pandas as pd

st.title("Analisis Produktivitas")

st.markdown("""
Analisis performa dan produktivitas belajar pengguna
""")

cursor.execute("""
SELECT status
FROM tugas
WHERE user=?
""", (st.session_state.username,))

data = cursor.fetchall()

status_list = []

for d in data:
    status_list.append(d[0])

selesai = status_list.count("Selesai")
belum = status_list.count("Belum")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Tugas Selesai",
        selesai
    )

with col2:
    st.metric(
        "Tugas Belum",
        belum
    )

with col3:

    total = selesai + belum

    if total > 0:

        progress = int(
            (selesai / total) * 100
        )

    else:

        progress = 0

    st.metric(
        "Produktivitas",
        f"{progress}%"
    )

st.markdown("---")

chart_data = pd.DataFrame({

    "Status": [
        "Selesai",
        "Belum"
    ],

    "Jumlah": [
        selesai,
        belum
    ]
})

fig = px.pie(
    chart_data,
    names="Status",
    values="Jumlah",
    hole=0.5,
    title="Persentase Penyelesaian Tugas"
)

fig.update_layout(
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    font_color="white",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.subheader("AI Productivity Insight")

if total == 0:

    st.info("""
    Sistem belum menemukan data tugas.

    Rekomendasi:
    Mulailah menambahkan jadwal dan tugas
    agar sistem dapat menganalisis produktivitas anda.
    """)

elif selesai == total:

    st.success("""
    Produktivitas Sangat Tinggi

    Analisis AI:
    Semua tugas berhasil diselesaikan.

    Rekomendasi:
    - Pertahankan konsistensi belajar
    - Mulai fokus pada pengembangan skill baru
    - Tambahkan challenge belajar mingguan
    """)

elif progress >= 75:

    st.success("""
    Produktivitas Tinggi

    Analisis AI:
    Sebagian besar tugas berhasil diselesaikan tepat waktu.

    Rekomendasi:
    - Pertahankan pola belajar sekarang
    - Kurangi penundaan tugas kecil
    - Fokus meningkatkan kualitas hasil tugas
    """)

elif progress >= 50:

    st.warning("""
    Produktivitas Cukup Stabil

    Analisis AI:
    Masih ada beberapa tugas yang belum selesai.

    Rekomendasi:
    - Buat prioritas tugas harian
    - Gunakan reminder lebih rutin
    - Hindari multitasking berlebihan
    """)

elif progress >= 25:

    st.error("""
    Produktivitas Mulai Menurun

    Analisis AI:
    Banyak tugas belum terselesaikan.

    Rekomendasi:
    - Kurangi distraksi saat belajar
    - Fokus 1 tugas hingga selesai
    - Gunakan teknik pomodoro
    - Mulai dari tugas prioritas tinggi
    """)

else:

    st.error("""
    Produktivitas Sangat Rendah

    Analisis AI:
    Sebagian besar tugas belum diselesaikan.

    Rekomendasi:
    - Susun ulang jadwal belajar
    - Bagi tugas besar menjadi kecil
    - Tetapkan target harian
    - Gunakan kalender dan reminder secara aktif
    """)

st.markdown("---")

st.subheader("Analisis Prioritas")

cursor.execute("""
SELECT prioritas
FROM tugas
WHERE user=?
""", (st.session_state.username,))

prioritas_data = cursor.fetchall()

tinggi = 0
sedang = 0
rendah = 0

for p in prioritas_data:

    if p[0] == "Tinggi":
        tinggi += 1

    elif p[0] == "Sedang":
        sedang += 1

    else:
        rendah += 1

priority_df = pd.DataFrame({

    "Prioritas": [
        "Tinggi",
        "Sedang",
        "Rendah"
    ],

    "Jumlah": [
        tinggi,
        sedang,
        rendah
    ]
})

bar_fig = px.bar(
    priority_df,
    x="Prioritas",
    y="Jumlah",
    title="Distribusi Prioritas Tugas",
    text_auto=True
)

bar_fig.update_layout(
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    font_color="white",
    height=500
)

st.plotly_chart(
    bar_fig,
    use_container_width=True
)

st.markdown("---")

st.subheader("Smart AI Recommendation")

if tinggi >= 5:

    st.warning("""
    Deteksi AI:
    Terlalu banyak tugas prioritas tinggi.

    Saran:
    - Segera kerjakan tugas dengan deadline terdekat
    - Hindari menambah tugas baru sebelum menyelesaikan yang lama
    - Gunakan sistem belajar bertahap
    """)

elif sedang >= 5:

    st.info("""
    Deteksi AI:
    Beban tugas sedang cukup stabil.

    Saran:
    - Mulai cicil tugas sedikit demi sedikit
    - Fokus menjaga konsistensi belajar
    """)

elif rendah >= 5:

    st.success("""
    Deteksi AI:
    Beban tugas masih ringan.

    Saran:
    - Manfaatkan waktu untuk belajar skill tambahan
    - Tingkatkan kualitas hasil tugas
    """)

else:

    st.info("""
    Analisis AI:
    Pola tugas masih normal dan terkendali.
    """)