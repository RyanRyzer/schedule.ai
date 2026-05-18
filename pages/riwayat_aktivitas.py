import streamlit as st
import pandas as pd
from database import cursor

st.title("Riwayat Aktivitas")

cursor.execute("SELECT * FROM aktivitas")

data = cursor.fetchall()

df = pd.DataFrame(
    data,
    columns=["ID", "Aktivitas", "Waktu"]
)

st.dataframe(df)