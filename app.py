import streamlit as st
import openai
import pyperclip
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="PeaceBoard AI", layout="centered")

st.title("🕊️ PeaceBoard – Spiritual-Productivity Dashboard")

st.markdown("**Daily Focus** – _Enter 1–3 key goals_")
work = st.text_input("📈 Work Goal")
torah = st.text_input("📖 Torah Study Goal")
kindness = st.text_input("💖 Kindness / Service Goal")

st.markdown("---")
st.markdown("**Business KPIs**")
leads = st.number_input("📊 Leads", min_value=0)
sales = st.number_input("💵 Sales", min_value=0)
progress = st.slider("📈 Weekly Progress (%)", 0, 100)

st.markdown("---")
st.markdown("**Spiritual Check-In**")
tefilah = st.checkbox("🕯️ Tefilah Today")
gratitude = st.checkbox("🙏 Practiced Gratitude")
integrity = st.slider("🤝 Integrity (1–10)", 1, 10)

st.markdown("---")
if st.button("📜 Generate Torah-Aligned Reflection"):
    prompt = f"Give a short Torah-based reflection based on the following:\nWork: {work}\nTorah: {torah}\nKindness: {kindness}\nLeads: {leads}\nSales: {sales}\nProgress: {progress}%\nTefilah: {tefilah}\nGratitude: {gratitude}\nIntegrity: {integrity}/10\n"
    with st.spinner("Asking the Sages..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": "You are a wise Torah mentor helping align spiritual and business goals."},
                          {"role": "user", "content": prompt}]
            )
            output = response.choices[0].message["content"]
            st.text_area("📖 Torah Reflection", output, height=200)
            if st.button("📋 Copy to Clipboard"):
                pyperclip.copy(output)
                st.success("Copied!")
        except Exception as e:
            st.error("Error generating response.")
            st.error(str(e))

st.markdown("---")
st.markdown("🌊 _Crafted by PacificTasks – Calm. Fast. Free._")
