import streamlit as st
import random

st.title("💬 AI Chat Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

greetings = [
    "Halo juga 👋",
    "Haiii 😭",
    "Yo wassup 🔥",
    "Hai, gimana harimu?",
    "Hello there 😎",
    "Welcome back 🚀",
    "Hai manusia produktif 👀",
    "Ada cerita apa hari ini?",
    "Hai, semoga harimu lancar ya.",
    "Hello hello 🔥"
]

motivation = [
    "Semangat terus ya 🚀",
    "Pelan-pelan aja gapapa.",
    "Kamu udah hebat sejauh ini.",
    "Progress kecil tetap berarti.",
    "Jangan menyerah sekarang 😭",
    "Tetap lanjut walau pelan.",
    "Konsisten lebih penting.",
    "Hari buruk bukan berarti hidup buruk.",
    "Aku yakin kamu bisa lewatin ini.",
    "Tetap kuat 🔥"
]

relationship = [
    "Percintaan memang kadang ribet 😭",
    "Komunikasi itu penting banget.",
    "Jangan terlalu memendam semuanya sendiri.",
    "Kadang kita cuma butuh didengar.",
    "Cinta memang random 😭",
    "Jangan lupa jaga diri sendiri juga.",
    "Semoga semuanya membaik ya.",
    "Mungkin kalian cuma butuh waktu.",
    "Overthinking hubungan capek juga 😭",
    "Yang penting tetap saling menghargai."
]

daily_life = [
    "Hari ini sibuk apa?",
    "Jangan lupa makan ya 😭",
    "Istirahat juga penting.",
    "Kadang rebahan itu healing 😭",
    "Tidur cukup jangan lupa.",
    "Minum air dulu 👀",
    "Semoga harimu menyenangkan.",
    "Kehidupan emang kadang chaos 😭",
    "Yang penting tetap jalanin pelan-pelan.",
    "Semoga besok lebih baik."
]

work = [
    "Kerjaan numpuk memang bikin stress 😭",
    "Coba fokus satu pekerjaan dulu.",
    "Multitasking kadang bikin makin capek.",
    "Jangan lupa istirahat bentar.",
    "Kerja terus juga burnout 😭",
    "Semoga kerjaannya lancar ya.",
    "Produktif bukan berarti nonstop.",
    "Pelan-pelan aja.",
    "Konsisten lebih penting.",
    "Tetap semangat kerja 🔥"
]

study = [
    "Belajar sedikit tapi konsisten lebih bagus.",
    "Jangan tunggu mood buat belajar 😭",
    "Mulai dari materi yang paling gampang.",
    "Belajar sambil praktik biasanya lebih cepat paham.",
    "Pomodoro bisa bantu fokus.",
    "Kurangi distraksi saat belajar.",
    "Review materi sebelum tidur.",
    "Semangat belajar 🚀",
    "Belajar marathon bikin cepat capek 😭",
    "Pelan-pelan yang penting ngerti."
]

coding = [
    "Debugging adalah jalan hidup programmer 😭",
    "Typo kecil bisa bikin sejam debugging.",
    "Backup project sebelum revisi besar.",
    "Coding sambil ngantuk bahaya 😭",
    "Refactor code bikin hidup lebih damai.",
    "Pisahkan logic biar rapih.",
    "Baca error message baik-baik.",
    "Semangat ngoding 🔥",
    "Ngoding itu seni kesabaran 😭",
    "Jangan lupa commit project."
]

sad = [
    "Aku ngerti itu pasti berat 😭",
    "Pelan-pelan aja gapapa.",
    "Semua orang juga pernah ngerasa begitu.",
    "Jangan terlalu keras sama diri sendiri.",
    "Kamu udah berusaha sejauh ini.",
    "Istirahat bentar juga gapapa.",
    "Semoga semuanya segera membaik.",
    "Aku di sini nemenin kok 👀",
    "Tetap kuat ya.",
    "Hari buruk pasti lewat."
]

funny = [
    "WKWKWK 😭",
    "Itu lucu juga jir 😭",
    "Aku jadi ikut ketawa 😭",
    "Anjir random banget 😭",
    "Kadang hidup emang meme 😭",
    "Waduh chaos 😭",
    "Plot twist banget 😭",
    "Buset 😭",
    "Kocak jir 😭",
    "Itu unexpected banget 😭"
]

default_responses = [

    "Menarik juga 🤔",
    "Coba ceritain lebih detail.",
    "Aku siap nemenin ngobrol 👀",
    "Wah relatable banget 😭",
    "Tetap semangat ya 🚀",
    "Aku ngerti maksudmu.",
    "Kadang hidup memang random 😭",
    "Yang penting jangan menyerah.",
    "Pelan-pelan aja.",
    "Mungkin semuanya akan membaik."
]

keyword_groups = {

    "halo": greetings,
    "hai": greetings,
    "hello": greetings,
    "pagi": greetings,
    "siang": greetings,
    "malam": greetings,

    "sedih": sad,
    "capek": sad,
    "cape": sad,
    "stress": sad,
    "burnout": sad,
    "bingung": sad,
    "galau": sad,
    "kecewa": sad,
    "sendiri": sad,

    "pacar": relationship,
    "cinta": relationship,
    "hubungan": relationship,
    "selingkuh": relationship,
    "mantan": relationship,
    "crush": relationship,

    "kerja": work,
    "kantor": work,
    "bos": work,
    "deadline": work,
    "meeting": work,

    "belajar": study,
    "kuliah": study,
    "ujian": study,
    "sekolah": study,
    "tugas": study,

    "ngoding": coding,
    "coding": coding,
    "bug": coding,
    "error": coding,
    "streamlit": coding,
    "python": coding,

    "wkwk": funny,
    "haha": funny,
    "lucu": funny,
    "meme": funny,

    "hidup": daily_life,
    "capek hidup": daily_life,
    "hari ini": daily_life,
    "makan": daily_life,
    "tidur": daily_life
}

for role, message in st.session_state.chat_history:

    if role == "user":

        left, right = st.columns([
            2,
            1
        ])

        with right:

            with st.container(border=True):

                st.caption("🧑 You")

                st.write(message)

    else:

        left, right = st.columns([
            1,
            2
        ])

        with left:

            with st.container(border=True):

                st.caption("🤖 Assistant")

                st.write(message)

msg = st.chat_input(
    "Tanya atau cerita apa aja..."
)

if msg:

    st.session_state.chat_history.append(
        ("user", msg)
    )

    msg_lower = msg.lower()

    matched_responses = []

    for keyword, responses in keyword_groups.items():

        if keyword in msg_lower:

            matched_responses.extend(responses)

    if len(matched_responses) > 0:

        response = random.choice(
            matched_responses
        )

    else:

        response = random.choice(
            default_responses
        )

    st.session_state.chat_history.append(
        ("assistant", response)
    )

    st.rerun()
