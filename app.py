import streamlit as st
import os
from dotenv import load_dotenv
from datetime import datetime
import random
import time
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from groq import Groq   # ✅ Official Groq client

# ---------------- ENV ----------------

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "llama-3.1-8b-instant"

client = Groq(api_key=GROQ_API_KEY)

# ---------------- CONFIG ----------------

st.set_page_config(
    page_title="Startup Research AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION ----------------

if "history" not in st.session_state:
    st.session_state.history = []

if "daily_usage" not in st.session_state:
    st.session_state.daily_usage = 0

if "monthly_usage" not in st.session_state:
    st.session_state.monthly_usage = 0

if "show_app" not in st.session_state:
    st.session_state.show_app = False

if "token_usage" not in st.session_state:
    st.session_state.token_usage = 0

DAILY_LIMIT = 10
MONTHLY_LIMIT = 100

# ---------------- UI STYLES ----------------

st.markdown("""
<style>
.hero {
background: linear-gradient(135deg,#5f2cff,#0bbcd6);
padding:35px;
border-radius:18px;
color:white;
text-align:center;
margin-bottom:20px;
}
.card {
background:#0e1117;
padding:20px;
border-radius:14px;
border:1px solid #222;
}
button {border-radius:12px !important;}
textarea {font-size:16px !important;}
</style>
""", unsafe_allow_html=True)

# ---------------- LANDING ----------------

if not st.session_state.show_app:

    st.markdown("""
    <div class="hero">
    <h1>🚀 Startup Research AI</h1>
    <h3>Research • Analyze • Monetize</h3>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Launch Platform"):
        st.session_state.show_app = True
        st.rerun()

    st.stop()

# ---------------- DASHBOARD ----------------

st.markdown("""
<div class="hero">
<h2>Startup Research AI Dashboard</h2>
</div>
""", unsafe_allow_html=True)

tabs = st.tabs(["📄 Generate", "📊 Compare", "📈 Analytics", "💰 Monetization", "🕘 History"])

# ---------------- SIDEBAR ----------------

st.sidebar.markdown("## 🔑 API Status")

if GROQ_API_KEY:
    st.sidebar.success("Groq Connected")
else:
    st.sidebar.error("Missing API Key")

st.sidebar.markdown("## 📊 Usage")

st.sidebar.progress(st.session_state.daily_usage / DAILY_LIMIT)
st.sidebar.write("Daily:", st.session_state.daily_usage, "/", DAILY_LIMIT)

st.sidebar.progress(st.session_state.monthly_usage / MONTHLY_LIMIT)
st.sidebar.write("Monthly:", st.session_state.monthly_usage, "/", MONTHLY_LIMIT)

# ---------------- SCORE ENGINE ----------------

def generate_scores():
    innovation = random.randint(60, 95)
    market = random.randint(55, 95)
    monetization = random.randint(50, 90)
    execution = random.randint(55, 90)

    overall = int((innovation + market + monetization + execution) / 4)

    return innovation, market, monetization, execution, overall

# ---------------- MOCK ----------------

def mock_report(idea):

    return f"""
MARKET OVERVIEW
{idea} operates in a fast-growing AI SaaS market.

TARGET CUSTOMERS
Startups, SMEs, Enterprises

BUSINESS MODEL
Subscription, Enterprise licensing, API monetization

GO-TO-MARKET
SEO, Partnerships, Outbound sales

REVENUE
Year 1: $150k
Year 2: $750k

PITCH SUMMARY
High growth AI-first SaaS opportunity.
"""

# ---------------- GROQ ----------------

def groq_report(idea, depth):

    if depth == "Deep Research":
        max_tokens = 2500
        prompt = f"""
Think step-by-step and provide detailed business reasoning.

Generate startup research report:

Market Overview
Customers
Problem
Solution
Competition
Business Model
Pricing
Go-To-Market
Revenue
Risks
Investor Pitch Summary

Startup Idea:
{idea}
"""
    else:
        max_tokens = 1200
        prompt = f"""
Generate concise startup report:

Market Overview
Business Model
Revenue
Risks
Investor Pitch

Startup Idea:
{idea}
"""

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a startup analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=max_tokens
    )

    text = completion.choices[0].message.content

    token_estimate = int(len(text.split()) * 1.3)

    return text, token_estimate

# ---------------- PDF EXPORT ----------------

def export_pdf(text):

    filename = "startup_report.pdf"

    styles = getSampleStyleSheet()
    story = []

    for line in text.split("\n"):
        story.append(Paragraph(line, styles["BodyText"]))
        story.append(Spacer(1, 10))

    pdf = SimpleDocTemplate(filename)
    pdf.build(story)

    return filename

# ---------------- TAB 1 GENERATE ----------------

with tabs[0]:

    mode = st.radio("Mode", ["Mock Mode", "Groq AI"])

    if mode == "Groq AI":
        depth_mode = st.radio("Analysis Depth", ["Fast Analysis", "Deep Research"])

    idea = st.text_area("Enter Startup Idea", height=120)
    tags = st.text_input("Tags")

    if st.button("🚀 Generate Report"):

        with st.spinner("Analyzing startup idea..."):

            if mode == "Mock Mode":
                report = mock_report(idea)
                tokens_used = 0
            else:
                report, tokens_used = groq_report(idea, depth_mode)

        innovation, market, monetization, execution, overall = generate_scores()

        st.session_state.history.append({
            "idea": idea,
            "report": report,
            "tags": tags,
            "score": overall
        })

        st.session_state.daily_usage += 1
        st.session_state.monthly_usage += 1
        st.session_state.token_usage += tokens_used

        # Streaming effect
        placeholder = st.empty()
        live = ""

        for ch in report:
            live += ch
            placeholder.text(live)
            time.sleep(0.002)

        st.markdown("## 📊 Evaluation")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Innovation", f"{innovation}%")
        c2.metric("Market", f"{market}%")
        c3.metric("Monetization", f"{monetization}%")
        c4.metric("Execution", f"{execution}%")

        st.progress(overall / 100)
        st.success(f"Overall Score: {overall}%")

        if tokens_used > 0:
            st.info(f"Estimated Tokens Used: {tokens_used}")

        # Export
        st.markdown("## 📤 Export")

        st.download_button("⬇ TXT Export", report, file_name="startup_report.txt")

        pdf_file = export_pdf(report)

        with open(pdf_file, "rb") as f:
            st.download_button("⬇ PDF Export", f, file_name="startup_report.pdf")

# ---------------- TAB 2 COMPARE ----------------

with tabs[1]:

    if len(st.session_state.history) < 2:
        st.info("Generate at least 2 reports")
    else:

        options = [h["idea"] for h in st.session_state.history]

        a = st.selectbox("Report A", options)
        b = st.selectbox("Report B", options)

        A = next(h for h in st.session_state.history if h["idea"] == a)
        B = next(h for h in st.session_state.history if h["idea"] == b)

        c1, c2 = st.columns(2)

        with c1:
            st.markdown(f"### {a}")
            st.text(A["report"])
            st.metric("Score", f"{A['score']}%")

        with c2:
            st.markdown(f"### {b}")
            st.text(B["report"])
            st.metric("Score", f"{B['score']}%")

# ---------------- TAB 3 ANALYTICS ----------------

with tabs[2]:

    st.subheader("📈 Platform Analytics")

    labels = ["Daily Requests", "Monthly Requests", "Total Tokens"]
    values = [
        st.session_state.daily_usage,
        st.session_state.monthly_usage,
        st.session_state.token_usage
    ]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel("Usage")
    ax.set_title("System Usage Overview")

    st.pyplot(fig)

# ---------------- TAB 4 MONETIZATION PREP ----------------

with tabs[3]:

    st.subheader("💰 Monetization Simulator")

    tier = st.selectbox("Pricing Tier", ["Free", "Pro ($19)", "Business ($49)", "Enterprise ($199)"])

    users = st.slider("Active Users", 10, 5000, 500)

    prices = {
        "Free": 0,
        "Pro ($19)": 19,
        "Business ($49)": 49,
        "Enterprise ($199)": 199
    }

    revenue = users * prices[tier]

    st.success(f"Estimated Monthly Revenue: ${revenue:,}")

    st.info("Use this to test SaaS pricing strategy before adding real payments")

# ---------------- TAB 5 HISTORY ----------------

with tabs[4]:

    if len(st.session_state.history) == 0:
        st.info("No reports yet")
    else:
        for item in reversed(st.session_state.history):
            st.markdown(f"""
            <div class="card">
            <b>{item['idea']}</b><br>
            Tags: {item['tags']}<br>
            Score: {item['score']}%
            </div><br>
            """, unsafe_allow_html=True)
