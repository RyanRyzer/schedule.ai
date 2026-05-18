import streamlit as st
from auth import login, register

st.set_page_config(
    page_title="Smart Study Planner",
    layout="wide",
    initial_sidebar_state="expanded"
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

section[data-testid="stSidebar"]{
    background:#0f172a;
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

if "selected_menu" not in st.session_state:
    st.session_state.selected_menu = "Dashboard"

if not st.session_state.login:

    st.title("🎓 SMART STUDY PLANNER")

    tab1, tab2 = st.tabs([
        "Login",
        "Register"
    ])

    with tab1:

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

    with tab2:

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

            if reg_pass != confirm_pass:

                st.error(
                    "Konfirmasi password tidak cocok"
                )

            else:

                success = register(
                    reg_user,
                    reg_pass
                )

                if success:

                    st.success(
                        "Register berhasil"
                    )

                else:

                    st.error(
                        "Username sudah dipakai"
                    )

else:

    with st.sidebar:

        st.title("🎓 Smart Planner")

        with st.expander(
            "📚 Productivity",
            expanded=True
        ):

            if st.button(
                "🏠 Dashboard",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Dashboard"

            if st.button(
                "➕ Tambah Tugas",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Tambah Tugas"

            if st.button(
                "📋 Daftar Tugas",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Daftar Tugas"

            if st.button(
                "✏️ Update Tugas",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Update Tugas"

            if st.button(
                "📅 Kalender",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Kalender"

            if st.button(
                "🔔 Reminder",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Reminder"

            if st.button(
                "📝 Notes",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Notes"

        with st.expander(
            "🤖 Smart Features",
            expanded=False
        ):

            if st.button(
                "📊 Analisis",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Analisis"

            if st.button(
                "📈 Statistik",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Statistik"

            if st.button(
                "🏆 Leaderboard",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Leaderboard"

            if st.button(
                "🏅 Achievement",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Achievement"

            if st.button(
                "🎯 Focus Mode",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Focus Mode"

            if st.button(
                "🏫 Study Room",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Study Room"

            if st.button(
                "💬 AI Assistant",
                use_container_width=True
            ):
                st.session_state.selected_menu = "AI Assistant"

        with st.expander(
            "👤 Account",
            expanded=False
        ):

            if st.button(
                "👤 Profil",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Profil"

            if st.button(
                "🚪 Logout",
                use_container_width=True
            ):
                st.session_state.selected_menu = "Logout"

    selected = st.session_state.selected_menu

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

    elif selected == "Notes":

        exec(open(
            "pages/notes.py",
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

    elif selected == "Leaderboard":

        exec(open(
            "pages/leaderboard.py",
            encoding="utf-8"
        ).read())

    elif selected == "Achievement":

        exec(open(
            "pages/achievement.py",
            encoding="utf-8"
        ).read())

    elif selected == "Focus Mode":

        exec(open(
            "pages/focus_mode.py",
            encoding="utf-8"
        ).read())

    elif selected == "Study Room":

        exec(open(
            "pages/study_room.py",
            encoding="utf-8"
        ).read())

    elif selected == "AI Assistant":

        exec(open(
            "pages/ai_chat.py",
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
        st.session_state.selected_menu = "Dashboard"

        st.rerun()
