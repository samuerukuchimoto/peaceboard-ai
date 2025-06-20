import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="PeaceBoard AI", layout="centered")
st.title("🕊️ PeaceBoard – Spiritual-Productivity Dashboard")

st.markdown("**🔁 Daily Focus** – _Enter 1–3 key goals_")
work = st.text_input("📌 Work Goal")
torah = st.text_input("📖 Torah Study Goal")
kindness = st.text_input("❤️ Kindness / Service Goal")

st.markdown("---")
st.markdown("**📊 Business KPIs**")
leads = st.number_input("📈 Leads", min_value=0)
sales = st.number_input("💰 Sales", min_value=0)

st.markdown("---")
if st.button("✨ Generate Torah-Aligned Reflection"):
    prompt = f"""As a Torah-based productivity guide, reflect on this user's day:
    - Work: {work}
    - Torah: {torah}
    - Kindness: {kindness}
    - Business KPIs: Leads: {leads}, Sales: {sales}
    Return a brief, motivating reflection using Torah concepts (e.g., chesed, emunah, bitachon, Avot)."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Torah-aligned spiritual mentor."},
                {"role": "user", "content": prompt}
            ]
        )
        result = response.choices[0].message.content
        st.success(result)
    except Exception as e:
        st.error(f"Error: {str(e)}")
