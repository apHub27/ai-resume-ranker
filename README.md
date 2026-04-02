# ⚡ AI Resume Ranker (Groq + Llama-3.1)

A high-performance AI application that ranks resumes against Job Descriptions (JD) using the **Llama-3.1-8b** model on **Groq Cloud**. It extracts text from PDF resumes, analyzes the match percentage, and identifies missing skills in seconds.

## 🌐 Live Demo
Check out the live application here: 
👉 [AI Resume Ranker Live](https://aphub27-ai-resume-ranker-groq-app-eju76y.streamlit.app/)

---

## 🚀 Features
* **Instant PDF Parsing:** Extracts clean text from uploaded resumes using `PyPDF2`.
* **Llama-3.1 Powered:** Uses the world's fastest inference engine (Groq) for near-instant analysis.
* **Match Percentage:** Provides a realistic score based on JD requirements.
* **Gap Analysis:** Highlights specific missing skills to help candidates improve.
* **Security First:** Implemented **Streamlit Secrets** management to keep API keys hidden and secure.

---

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **AI Model:** Llama-3.1-8b-instant (via Groq Cloud)
* **Language:** Python 3.x
* **PDF Processing:** PyPDF2

---

## ⚙️ Local Setup
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/apHub27/ai-resume-ranker.git](https://github.com/apHub27/ai-resume-ranker.git)
   cd ai-resume-ranker

   Install dependencies:

Bash
pip install -r requirements.txt
Setup Secrets:
Create a folder .streamlit/ and a file secrets.toml inside it:

Ini, TOML
# .streamlit/secrets.toml
GROQ_API_KEY = "your_actual_groq_api_key_here"
Run the app:

Bash
streamlit run Groq_app.py
🛡️ Security Note
This project follows best practices for API security. The .gitignore file ensures that local secret files are never pushed to the public repository. Deployment uses environment variables via the Streamlit Cloud dashboard.

👨‍💻 Developed by
apHub27 - Aspiring AI Engineer
