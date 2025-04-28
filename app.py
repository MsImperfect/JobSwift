import os
import streamlit as st
from google import generativeai as palm


palm.configure(api_key="YOUR GEMINI API KEY")

model_name = 'models/gemini-1.5-flash'
model = palm.GenerativeModel('gemini-1.5-flash')

def generate_resume(name, experience, skills, projects, education, awards):
    prompt = f"My name is {name}. I have {experience} years of experience in {skills}."
    prompt += f"\n\nProjects:\n{projects}\n\nEducation:\n{education}\n\nAwards and Recognition:\n{awards}"
    response = model.generate_content(prompt)
    return response.text


def generate_cover_letter(company_name, job_title):
    prompt = f"Dear Hiring Manager, \n\nI am writing to express my interest in the {job_title} position at {company_name}."
    response = model.generate_content(prompt)
    return response.text


def generate_interview_questions (skills):
    prompt = f"Interview Preparation Questions Based on Skills: {skills}"
    response = model.generate_content(prompt)
    return response.text


def main():
    st.title("JobSwift: Accelerating Careers With AI-Powered Applications")  
    option = st.sidebar.selectbox("Select Option", ["Generate Resume", "Generate Cover Letter", "Generate Interview Questions"]) 
    if option == "Generate Resume":
        st.subheader("Generate Resume")
        name = st.text_input("Enter your name")
        experience = st.number_input("Enter your years of experience", min_value=0, step=1)
        skills = st.text_area("Enter your skills")
        projects = st.text_area("Enter your projects")
        education = st.text_area("Enter your education")
        awards = st.text_area("Enter your awards and recognition")
        if st.button("Generate"): 
                if name and experience and skills and projects and education and awards:
                    resume = generate_resume(name, experience, skills, projects, education, awards)
                    st.write(resume)
                else:
                    st.warning("Please fill in all the fields.")
    elif option == "Generate Cover Letter":  
        st.subheader("Generate Cover Letter")
        company_name = st.text_input("Enter the company name")
        job_title = st.text_input("Enter the job title")
        if st.button("Generate"):
            if company_name and job_title:
                cover_letter = generate_cover_letter(company_name, job_title) 
                st.write(cover_letter)
            else:
                st.warning("Please fill in all the fields.")
    elif option == "Generate Interview Questions":  
        st.subheader("Generate Interview Questions")
        skills = st.text_area("Enter your skills")
        if st.button("Generate"):
            if skills:
                interview_questions = generate_interview_questions(skills)
                st.write(interview_questions)
            else:
                st.warning("Please enter your skills.")



if __name__ == "__main__":  
    main()
