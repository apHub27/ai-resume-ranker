import streamlit as st
from groq import Groq
from PyPDF2 import PdfReader

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    st.error("API Key nahi mili! Streamlit Cloud ke 'Secrets' mein key dalo.")

#helper function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    st.error(f"Groq setup error: {e}")

# 2. UI
st.title("⚡ Groq AI Resume Ranker")    

jd = st.text_area("JD Paste Karo:")
resume = st.file_uploader("Upload Your Resume:", type="pdf")

if st.button("Analyze Now"):
    if jd and resume:
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(resume)
        try:
            # Naya aur Super Fast Model
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant", 
                messages=[
                    {"role": "system", "content": "Tum ek expert HR manager ho. Match % aur missing skills batao."},
                    {"role": "user", "content": f"JD: {jd}\n\nResume: {resume}"}
                ],
                temperature=0.0
            )
            st.success("Analysis Done! Result niche hai:")
            st.write(completion.choices[0].message.content)
        except Exception as e:
            st.error(f"Ab kya hua bhai?: {e}")