# startup-research-ai

# 🚀 Startup Research AI Platform

A modern AI-powered SaaS-style web application that helps founders, entrepreneurs, and product teams **analyze startup ideas**, **generate investor-grade business reports**, **compare opportunities**, and **simulate monetization strategies** — all from one dashboard.

Built using **Streamlit + Groq AI (LLaMA 3.1 Instant)** with a clean, responsive, mobile-friendly interface.

---

# 🌟 Live Capabilities

This project demonstrates how production-grade AI tools can be combined with fast UI frameworks to build **real MVP SaaS platforms**.

### Core Highlights

- AI-powered startup research engine
- Deep business analysis mode
- Streaming AI output
- Startup evaluation scoring system
- Report comparison tool
- Usage analytics dashboard
- Monetization simulator
- Export tools (TXT + PDF)
- Mobile responsive UI

---

# 🧠 What This App Does

The platform allows users to:

1. Enter a startup idea
2. Generate AI-powered research reports
3. Evaluate startup potential using scores
4. Compare multiple ideas side-by-side
5. Track AI usage analytics
6. Simulate SaaS monetization revenue
7. Export reports for offline use

---

# 🏗 System Architecture Overview

User Input
↓
Streamlit UI
↓
Groq AI API (LLaMA 3.1)
↓
AI Report Generator
↓
Evaluation Engine + Analytics
↓
History Storage (Session)
↓
Export System (TXT / PDF)


---

# 🛠 Technology Stack

| Layer | Technology |
------|--------
Frontend UI | Streamlit
AI Backend | Groq API (LLaMA 3.1 Instant)
Visualization | Matplotlib
PDF Export | ReportLab
Config Management | python-dotenv
Language | Python 3.x

---

# 📂 Project Folder Structure

startup-research-ai/
│
├── app.py
│ Main Streamlit application
│ Contains UI, AI calls, analytics, exports and logic
│
├── requirements.txt
│ Python dependencies required to run the app
│
├── .gitignore
│ Prevents sensitive and unnecessary files from being uploaded
│
├── README.md
│ Project documentation (this file)
│
└── .env (LOCAL ONLY - Not uploaded)
Contains Groq API key


---

# ⚙️ Local Setup Guide

Follow these steps to run the project locally.

---

## 1️⃣ Clone Repository

bash
git clone https://github.com/Aryan-Bose/startup-research-ai.git
cd startup-research-ai

---

## 2️⃣ Create Virtual Environment (Recommended)
Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

---

## 3️⃣ Install Dependencies
pip install -r requirements.txt

---

## 4️⃣Create Environment File

Create .env file in root directory:

GROQ_API_KEY=your_groq_api_key_here

---

## 5️⃣ Run Application
streamlit run app.py

Application will open in browser:

http://localhost:8501

##Deployed at 
https://startup-research-ai-mq6rkfk7eghmtoihjppja8.streamlit.app

