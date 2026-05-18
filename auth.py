from database import cursor

def login(username, password):

    cursor.execute("""
    SELECT *
    FROM users
    WHERE username=?
    AND password=?
    """, (
        username,
        password
    ))

    return cursor.fetchone()

def register(username, password):

    cursor.execute("""
    SELECT *
    FROM users
    WHERE username=?
    """, (username,))

    check = cursor.fetchone()

    if check:

        return False

    cursor.execute("""
    INSERT INTO users(
        username,
        password,
        role
    )
    VALUES(?,?,?)
    """, (
        username,
        password,
        "user"
    ))

    from database import conn

    conn.commit()

    return True
