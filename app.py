import streamlit as st
from streamlit_option_menu import option_menu
from auth import login, register

st.set_page_config(
    page_title="Smart Study Planner",
    layout="wide",
    initial_sidebar_state="collapsed"
)

with open("style.css", encoding="utf-8") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown("""
<style>

[data-testid="stSidebarNav"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

html, body, [class*="css"]{
    background:#020617;
    color:white;
}

</style>
""", unsafe_allow_html=True)

if "login" not in st.session_state:
    st.session_state.login = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "role" not in st.session_state:
    st.session_state.role = ""

if "user_id" not in st.session_state:
    st.session_state.user_id = 0

if not st.session_state.login:

    st.markdown("""
    <div style='text-align:center; margin-top:70px;'>

    <h1 style='font-size:55px; color:white; font-weight:bold;'>
    SMART STUDY PLANNER
    </h1>

    <p style='color:#94a3b8; font-size:18px;'>
    Sistem Cerdas Pengatur Jadwal dan Produktivitas Mahasiswa
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        menu = option_menu(
            None,
            ["Login", "Register"],
            icons=["box-arrow-in-right", "person-plus"],
            orientation="horizontal"
        )

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        if menu == "Login":

            st.subheader("Login")

            username = st.text_input(
                "Username"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            if st.button("Login"):

                user = login(
                    username,
                    password
                )

                if user:

                    st.session_state.login = True
                    st.session_state.user_id = user[0]
                    st.session_state.username = user[1]
                    st.session_state.role = user[3]

                    st.rerun()

                else:

                    st.error(
                        "Username atau password salah"
                    )

        else:

            st.subheader("Register")

            reg_user = st.text_input(
                "Buat Username"
            )

            reg_pass = st.text_input(
                "Buat Password",
                type="password"
            )

            confirm_pass = st.text_input(
                "Konfirmasi Password",
                type="password"
            )

            if st.button("Register"):

                if (
                    reg_user == ""
                    or reg_pass == ""
                ):

                    st.warning(
                        "Semua field wajib diisi"
                    )

                elif (
                    reg_pass != confirm_pass
                ):

                    st.error(
                        "Konfirmasi password tidak cocok"
                    )

                else:

                    success = register(
                        reg_user,
                        reg_pass
                    )

                    if success:

                        st.session_state.login = True
                        st.session_state.username = reg_user
                        st.session_state.role = "user"

                        st.success(
                            "Register berhasil"
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Username sudah dipakai"
                        )

        st.markdown("</div>", unsafe_allow_html=True)

else:

    with st.sidebar:

        selected = option_menu(
            menu_title="Smart Planner",

            options=[
                "Dashboard",
                "Tambah Tugas",
                "Daftar Tugas",
                "Update Tugas",
                "Kalender",
                "Reminder",
                "Analisis",
                "Statistik",
                "Profil",
                "Logout"
            ],

            icons=[
                "house",
                "plus-circle",
                "clipboard-data",
                "pencil-square",
                "calendar-event",
                "bell",
                "bar-chart",
                "graph-up",
                "person-circle",
                "box-arrow-right"
            ],

            menu_icon="mortarboard-fill",
            default_index=0,

            styles={

                "container": {
                    "padding": "10px",
                    "background-color": "#0f172a",
                },

                "icon": {
                    "color": "white",
                    "font-size": "18px"
                },

                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin":"5px",
                    "--hover-color": "#1e293b",
                    "border-radius": "10px",
                },

                "nav-link-selected": {
                    "background":
                    "linear-gradient(90deg,#2563eb,#7c3aed)",
                },
            }
        )

    if selected == "Dashboard":

        exec(open(
            "pages/dashboard_user.py",
            encoding="utf-8"
        ).read())

    elif selected == "Tambah Tugas":

        exec(open(
            "pages/tambah_tugas.py",
            encoding="utf-8"
        ).read())

    elif selected == "Daftar Tugas":

        exec(open(
            "pages/daftar_tugas.py",
            encoding="utf-8"
        ).read())

    elif selected == "Update Tugas":

        exec(open(
            "pages/update_tugas.py",
            encoding="utf-8"
        ).read())

    elif selected == "Kalender":

        exec(open(
            "pages/kalender.py",
            encoding="utf-8"
        ).read())

    elif selected == "Reminder":

        exec(open(
            "pages/reminder.py",
            encoding="utf-8"
        ).read())

    elif selected == "Analisis":

        exec(open(
            "pages/analisis_produktivitas.py",
            encoding="utf-8"
        ).read())

    elif selected == "Statistik":

        exec(open(
            "pages/statistik.py",
            encoding="utf-8"
        ).read())

    elif selected == "Profil":

        exec(open(
            "pages/profil.py",
            encoding="utf-8"
        ).read())

    elif selected == "Logout":

        st.session_state.login = False
        st.session_state.username = ""
        st.session_state.role = ""

        st.rerun()