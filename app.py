from google import genai
import streamlit as st

# 1. Configuration (Directly passing the key)
# Yahan apni asli key dalo
MY_API_KEY = "AIzaSyCrWKr0mY_jraEOGY_zMGba29ljSgCbtAU" 

client = genai.Client(api_key=MY_API_KEY)

# 2. UI Layout
st.title("🚀 AI Resume Ranker Pro")
st.markdown("---")

jd = st.text_area("Job Description (JD) paste karein:", height=150)
resume = st.text_area("Resume Text paste karein:", height=150)

if st.button("Analyze Now"):
    if jd and resume:
        try:
            # New SDK syntax: models.generate_content
            response = client.models.generate_content(
                model="gemini-1.5-flash", 
                contents=f"Compare this JD and Resume. Give Match % and missing skills.\nJD: {jd}\nResume: {resume}"
            )
            st.success("Analysis Done!")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Bhai, dono fields bharna zaroori hai.")