⚡ JobSwift – Accelerating Careers with AI-Powered Applications
JobSwift is an AI-powered Streamlit web app designed to help job seekers generate professional resumes, cover letters, and interview questions — all in just a few clicks.
Built with Python, Google Gemini AI (via GenerativeModel), and Streamlit, JobSwift simplifies the career-building process using prompt-based generative intelligence.

🎯 Features
📝 Resume Generator
Instantly generate a personalized resume based on your experience, skills, education, and achievements.
💌 Cover Letter Generator
Create a customized, professional cover letter for any job title and company in seconds.
❓ Interview Prep
Generate tailored interview questions based on your skills for better preparation and confidence.

🧪 How to Run Locally

1. Clone the repository

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Add your Gemini API Key
Edit this line in the script:
```python
palm.configure(api_key="YOUR GEMINI API KEY")
```

4. Run the Streamlit app
```bash
streamlit run app.py
```