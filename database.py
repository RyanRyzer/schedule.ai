import sqlite3

conn = sqlite3.connect("planner.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tugas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    judul TEXT,
    matkul TEXT,
    deadline TEXT,
    prioritas TEXT,
    status TEXT
)
""")

conn.commit()

try:
    cursor.execute("ALTER TABLE tugas ADD COLUMN user TEXT")
except:
    pass

cursor.execute("""
UPDATE tugas
SET user = (
    SELECT username
    FROM users
    WHERE users.id = tugas.user_id
)
WHERE user IS NULL
""")

conn.commit()


def tambah_tugas(user_id, judul, matkul, deadline, prioritas, status):
    cursor.execute("""
        INSERT INTO tugas
        (user_id, judul, matkul, deadline, prioritas, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, judul, matkul, deadline, prioritas, status))

    conn.commit()


def get_all_tugas(user_id):
    cursor.execute("""
        SELECT *
        FROM tugas
        WHERE user_id=?
        ORDER BY id DESC
    """, (user_id,))

    return cursor.fetchall()


def update_tugas_data(
    tugas_id,
    judul,
    matkul,
    deadline,
    prioritas,
    status
):
    cursor.execute("""
        UPDATE tugas
        SET
        judul=?,
        matkul=?,
        deadline=?,
        prioritas=?,
        status=?
        WHERE id=?
    """, (
        judul,
        matkul,
        deadline,
        prioritas,
        status,
        tugas_id
    ))

    conn.commit()


def hapus_tugas(tugas_id):
    cursor.execute("""
        DELETE FROM tugas
        WHERE id=?
    """, (tugas_id,))

    conn.commit()