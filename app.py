import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Hardware AI | Expert PC Assistant",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ---------- App background ---------- */
    .stApp {
        background: radial-gradient(circle at 15% 0%, #1b2040 0%, #0d0f1c 45%, #060710 100%);
        color: #E8EAF2;
    }

    /* ---------- Hide default header/footer ---------- */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ---------- Hero Banner ---------- */
    .hero-wrap {
        padding: 2.2rem 2.4rem;
        border-radius: 20px;
        margin-bottom: 1.6rem;
        background: linear-gradient(120deg, rgba(99,102,241,0.18), rgba(56,189,248,0.10) 60%, rgba(236,72,153,0.14));
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 8px 40px rgba(80,70,229,0.15);
        position: relative;
        overflow: hidden;
    }
    .hero-wrap::before {
        content: "";
        position: absolute;
        top: -60px; right: -60px;
        width: 220px; height: 220px;
        background: radial-gradient(circle, rgba(56,189,248,0.35), transparent 70%);
        border-radius: 50%;
    }
    .hero-title {
        font-family: 'Sora', sans-serif;
        font-weight: 800;
        font-size: 2.5rem;
        background: linear-gradient(90deg, #818CF8, #38BDF8 45%, #F472B6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        letter-spacing: -0.5px;
    }
    .hero-sub {
        color: #A9AFC3;
        font-size: 1.02rem;
        max-width: 640px;
    }
    .badge-row { margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap; }
    .badge {
        display: inline-block;
        padding: 0.35rem 0.85rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 600;
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        color: #C7CBE0;
    }

    /* ---------- Glass Cards (feature grid) ---------- */
    .feature-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.1rem 1.2rem;
        transition: all 0.25s ease;
        height: 100%;
    }
    .feature-card:hover {
        transform: translateY(-4px);
        border-color: rgba(129,140,248,0.55);
        box-shadow: 0 10px 30px rgba(99,102,241,0.25);
        background: rgba(255,255,255,0.07);
    }
    .feature-icon { font-size: 1.6rem; margin-bottom: 0.4rem; }
    .feature-title { font-weight: 700; font-size: 0.98rem; color: #F1F2F8; margin-bottom: 0.15rem; }
    .feature-desc { font-size: 0.82rem; color: #9AA0B8; line-height: 1.35; }

    /* ---------- Section label ---------- */
    .section-label {
        font-family: 'Sora', sans-serif;
        font-weight: 700;
        font-size: 1.05rem;
        color: #E8EAF2;
        margin: 1.6rem 0 0.8rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .section-label .bar {
        width: 5px; height: 20px;
        border-radius: 4px;
        background: linear-gradient(180deg, #818CF8, #38BDF8);
        display: inline-block;
    }

    /* ---------- Input area ---------- */
    div[data-testid="stTextArea"] textarea {
        background: rgba(255,255,255,0.045) !important;
        border: 1.5px solid rgba(255,255,255,0.12) !important;
        border-radius: 14px !important;
        color: #F1F2F8 !important;
        font-size: 0.98rem !important;
        padding: 0.9rem 1rem !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="stTextArea"] textarea:focus {
        border-color: #818CF8 !important;
        box-shadow: 0 0 0 3px rgba(129,140,248,0.20) !important;
    }
    div[data-testid="stTextArea"] textarea::placeholder { color: #6C7290 !important; }

    /* ---------- Ask button ---------- */
    div.stButton > button {
        background: linear-gradient(90deg, #6366F1, #38BDF8);
        color: white;
        font-weight: 700;
        font-size: 1rem;
        border: none;
        border-radius: 14px;
        padding: 0.7rem 1rem;
        transition: all 0.2s ease;
        box-shadow: 0 6px 22px rgba(99,102,241,0.35);
    }
    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.01);
        box-shadow: 0 10px 30px rgba(56,189,248,0.45);
        filter: brightness(1.06);
    }
    div.stButton > button:active { transform: translateY(0px) scale(0.99); }

    /* ---------- Response card ---------- */
    .response-card {
        background: linear-gradient(145deg, rgba(99,102,241,0.10), rgba(56,189,248,0.06));
        border: 1px solid rgba(129,140,248,0.35);
        border-radius: 18px;
        padding: 1.6rem 1.8rem;
        margin-top: 0.6rem;
        animation: fadeInUp 0.5s ease;
        box-shadow: 0 10px 40px rgba(56,189,248,0.10);
    }
    .response-header {
        display: flex;
        align-items: center;
        gap: 0.55rem;
        font-family: 'Sora', sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        color: #F1F2F8;
        margin-bottom: 0.8rem;
    }
    .response-header .dot {
        width: 10px; height: 10px; border-radius: 50%;
        background: #34D399;
        box-shadow: 0 0 10px #34D399;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(14px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0E1226 0%, #090B18 100%);
        border-right: 1px solid rgba(255,255,255,0.06);
    }
    .sidebar-title {
        font-family: 'Sora', sans-serif;
        font-weight: 800;
        font-size: 1.4rem;
        background: linear-gradient(90deg, #818CF8, #38BDF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .topic-chip {
        display: inline-block;
        padding: 0.32rem 0.7rem;
        margin: 0.18rem 0.18rem 0.18rem 0;
        border-radius: 10px;
        font-size: 0.82rem;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.09);
        color: #C7CBE0;
    }

    /* Divider styling */
    hr { border-color: rgba(255,255,255,0.08) !important; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================
if "history" not in st.session_state:
    st.session_state.history = []


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown('<div class="sidebar-title">🖥️ Hardware AI</div>', unsafe_allow_html=True)
    st.caption("Your expert PC hardware companion")
    st.markdown("---")

    st.markdown("**📌 Supported Topics**")
    topics = [
        "CPU", "GPU", "RAM", "Motherboard", "SSD / HDD / NVMe",
        "PSU", "PC Building", "Cooling Systems", "Troubleshooting",
    ]
    chips_html = "".join(f'<span class="topic-chip">{t}</span>' for t in topics)
    st.markdown(chips_html, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**⚙️ Model Settings**")
    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.3, 0.05)
    model_name = st.selectbox(
        "Model",
        ["llama-3.1-8b-instant"],
        index=0,
    )

    st.markdown("---")
    if st.session_state.history:
        st.markdown(f"**🗂️ Session Q&A:** {len(st.session_state.history)}")
        if st.button("🧹 Clear History", use_container_width=True):
            st.session_state.history = []
            st.rerun()

    st.markdown("---")
    st.info("💡 Ask only computer hardware related questions.")


# ============================================================
# HERO SECTION
# ============================================================
st.markdown(
    """
    <div class="hero-wrap">
        <div class="hero-title">🖥️ Computer Hardware AI Assistant</div>
        <div class="hero-sub">
            Get instant, expert-level guidance on processors, graphics cards, storage,
            cooling, compatibility, and troubleshooting — explained clearly, step by step.
        </div>
        <div class="badge-row">
            <span class="badge">⚡ Powered by Groq</span>
            <span class="badge">🎯 Hardware-only Focus</span>
            <span class="badge">🧩 Compatibility Checks</span>
            <span class="badge">🛠️ Troubleshooting Ready</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FEATURE GRID
# ============================================================
st.markdown('<div class="section-label"><span class="bar"></span>What You Can Ask</div>', unsafe_allow_html=True)

features = [
    ("🧠", "Processor Advice", "CPU picks, comparisons & bottleneck checks."),
    ("🎮", "GPU Guidance", "Graphics card comparisons for gaming & work."),
    ("💾", "RAM & Storage", "SSD vs HDD vs NVMe, capacity planning."),
    ("🧩", "Compatibility", "Motherboard, CPU & PSU compatibility checks."),
    ("❄️", "Cooling Systems", "Air vs liquid cooling recommendations."),
    ("🛠️", "Troubleshooting", "Diagnose boot issues, crashes & more."),
]

cols = st.columns(3)
for i, (icon, title, desc) in enumerate(features):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-desc">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# QUESTION INPUT
# ============================================================
st.markdown('<div class="section-label"><span class="bar"></span>Ask Your Question</div>', unsafe_allow_html=True)

question = st.text_area(
    "🔍 Enter Your Hardware Question",
    height=160,
    placeholder="Example: Is 16GB RAM enough for gaming in 2026?",
    label_visibility="collapsed",
)

col1, col2 = st.columns([1, 5])
with col1:
    ask = st.button("🚀 Ask AI", use_container_width=True)


# ============================================================
# PROMPT TEMPLATE
# ============================================================
PROMPT_TEMPLATE = ChatPromptTemplate.from_template(
    """
    You are a Computer Hardware Expert.
    Your job is to answer ONLY computer hardware-related questions.

    Topics include:
    - CPU (Processor)
    - GPU (Graphics Card)
    - RAM
    - Motherboard
    - Storage (HDD, SSD, NVMe)
    - Power Supply (PSU)
    - Computer Cabinets
    - Cooling Systems
    - Monitors
    - Keyboards and Mice
    - Compatibility of Components
    - Hardware Installation
    - Hardware Troubleshooting
    - Upgrading PC Components
    - Computer Peripherals

    If the user asks anything outside computer hardware,
    reply:

    "Sorry, I only answer computer hardware-related questions."

    Question:
    {question}

    Provide:
    1. Simple Explanation
    2. Step-by-step guidance
    3. Best Practices
    4. Precautions if needed
    """
)


# ============================================================
# HANDLE ASK
# ============================================================
if ask:
    if not question.strip():
        st.warning("⚠️ Please enter a question before asking.")
    else:
        llm = ChatGroq(
            model=model_name,
            temperature=temperature,
        )

        chain = PROMPT_TEMPLATE | llm

        with st.spinner("🤖 Thinking through your hardware question..."):
            response = chain.invoke({"question": question})

        st.session_state.history.insert(0, {"q": question, "a": response.content})

        st.markdown(
            f"""
            <div class="response-card">
                <div class="response-header"><span class="dot"></span> AI Response</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(response.content)


# ============================================================
# HISTORY
# ============================================================
if st.session_state.history:
    st.markdown('<div class="section-label"><span class="bar"></span>Previous Questions</div>', unsafe_allow_html=True)
    for item in st.session_state.history[1:] if ask else st.session_state.history:
        with st.expander(f"💬 {item['q'][:80]}"):
            st.markdown(item["a"])

st.markdown("<br><br>", unsafe_allow_html=True)