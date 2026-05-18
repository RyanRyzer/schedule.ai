import streamlit as st
import pandas as pd
from database import cursor, conn

st.title("Manajemen User")

cursor.execute("SELECT id, username, role FROM users")

data = cursor.fetchall()

df = pd.DataFrame(
    data,
    columns=["ID", "Username", "Role"]
)

st.dataframe(df)

hapus = st.number_input("ID User", step=1)

if st.button("Hapus User"):

    cursor.execute(
        "DELETE FROM users WHERE id=?",
        (hapus,)
    )

    conn.commit()

    st.success("User berhasil dihapus")
