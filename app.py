import streamlit as st
import openai
import os
from dotenv import load_dotenv
from datetime import datetime

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="PeaceBoard – Soul-Aligned Productivity", layout="centered")

st.title("🕊️ PeaceBoard – Soul-Aligned AI Guidance")
st.markdown("**🕰️ Your time is divine. Let’s use it wisely.**")

# Time-based reflection
now = datetime.now()
st.markdown(f"**🗓️ Today:** {now.strftime('%A, %B %d, %Y')}")

# User Inputs
with st.form("input_form"):
    st.subheader("🌱 Set Today’s Intentions")
    spiritual = st.text_input("📖 Torah Learning / Reflection")
    kindness = st.text_input("❤️ Act of Kindness")
    mission = st.text_input("🎯 Core Mission Task")
    submitted = st.form_submit_button("Save and Reflect")

if submitted:
    prompt = f"""
    I'm creating a daily soul-aligned dashboard. Based on these entries:
    - Torah: {spiritual}
    - Kindness: {kindness}
    - Mission: {mission}
    Provide a 3-line reflection that aligns with timeless Torah values.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a wise Torah-aligned AI reflecting on purpose and meaning."},
                {"role": "user", "content": prompt}
            ]
        )
        reflection = response.choices[0].message.content.strip()
        st.markdown("### ✨ Torah-Aligned Insight")
        st.success(reflection)
    except Exception as e:
        st.error("❌ Error generating insight. Please check your API key or try again later.")
