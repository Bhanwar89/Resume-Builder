import streamlit as st
from genResume import generate_pdf
import json
import pyperclip

sample_format = {
    "fields": {
        "Summary": "**Machine Learning and MLOps Engineer** with 1.5+ years of experience deploying and maintaining AI-driven solutions in production environments. Proficient in Python, TensorFlow, CI/CD, and cloud platforms (AWS, GCP) to enable scalable, reliable ML pipelines.",
        "Tech Skills": "- **Languages**: Python, R, Bash\n- **ML Frameworks**: TensorFlow, PyTorch, Scikit-learn, Keras\n- **DevOps & Cloud**: Docker, Kubernetes, Jenkins, GitHub, AWS, GCP, CI/CD (Airflow, MLflow, Kubeflow)\n- **Data Engineering & Databases**: MySQL, PostgreSQL, MongoDB, ETL, Data Pipelines\n- **Tools**: Tableau, Power BI, Hugging Face, Postman"
    },
    "workExp": {
        "companyName": "WIN Home Inspection",
        "location": "New Delhi, India",
        "jobTitle": "Data Engineer",
        "timeFrame": "Nov 2019 - Jan 2020",
        "workDescription": "- Led data collection and quality assurance, managing data curation and ETL pipelines across departments.\n- Developed BI dashboards, visualizations, and reports to support data-driven decision-making."
    },
    "projectExp": {
        "P1": {
            "name": "Neural Network from Scratch",
            "techStack": "**Python**, **TensorFlow**, Docker, Kubernetes, Jenkins",
            "projectDescription": "- Developed a neural network for deployment in a production environment, focusing on scalability and reliability.\n- Integrated CI/CD pipelines and automated deployment, enhancing operational efficiency and model monitoring capabilities."
        },
        "P2": {
            "name": "Interactive AI Chatbot with LLM Capabilities",
            "techStack": "**Transformer Models**, Hugging Face, FastAPI, Google Cloud",
            "projectDescription": "- Built and deployed a chatbot using **Large** Language Models (LLMs) for interactive customer support, integrating NLP and RAG techniques."
        },
        "P3": {
            "name": "End-to-End Text-to-Music Model",
            "techStack": "**TensorFlow**, Transformer Models, AWS S3, MLflow",
            "projectDescription": "- Created a model using Transformer technology to translate text descriptions into music, showcasing ML integration for creative AI solutions.\n- Designed and monitored model performance using MLflow to track experiments and enhance reproducibility."
        }
    }
}


st.title('Generate PDF from Data')
data = st.text_area("Add your JSON here")

if st.button("Generate PDF"):
    
    json_data = json.loads(data)

    pdf_buffer = generate_pdf(json_data)

    st.download_button(
            label="Download PDF",
            data=pdf_buffer,
            file_name="Generated_Resume.pdf",
            mime="application/pdf"
    )

st.write("Copy the Simple JSON from here")
st.json(sample_format, expanded=False)



custom_prompt = f"""
Your the hiring manager for the company and a person who's knows how the ATS system works. And your goal is to write a resume for me that make sures I will get an interview at the company.

There some Rules and restriction to follow and keep in mind :

1. All ways try using the word cloud of the Job Description.
2. Please write 3 relevant clear bullet points for workExp.
3. While writing points for workExp Keep in mind there are a few users so can use some user matrix if applicable.
4. Please write four relevant clear bullet points for projectExp. and make it around 1.5 lines per point
5. While wrting points for projectExp keep in mind there are no users for the Projects.
6. The points should have some components of Measurable and Quantifiable impact and should be in this format Accomplish X as measured by Y by Doing Z. Please make sure it must be realistic. 
7. For Project Bullet Points should change the projects that are more relevant to the Job Description and Keep the projects a bit more realistic in way that a single person can do it with in a week.
8. Bold the most relevant information from the Job description word cloud
9. Please add 3 Projects.
10. Add Relevant Skills to the skill section and take the info from the Job Description
11. For Summery Keep it Clean and relevant to the Job Description
12. While writing the Projects keep this in mind How write about the Projects :- (What you did and How you did it e.g. Framework, Technology, Tool. Example:- Data Engineering: Build a lager and custom Datasets by implementing fetcher and preprocessing units to periodically **retrieve** data)
13. DON’T CHANGE INFO SUCH AS Name, number, address, email_link, linkedin_link, Personal_site, github, companyName, location, timeFrame, Education
14. Keep the Experience 1 year in Summary
15. Pls add enough information that it will not look and feel Short.
16. there are only 3 section to keep in mind 
    1. fields (”Summary”, “Tech Skills”)
    2. workExp
    3. projectExp
17. NEVER CHANGE THIS 
        "workExp": (
        "companyName": "WIN Home Inspection",
        "location": "New Delhi, India",
        "jobTitle": "Data Engineer",
        "timeFrame": "Nov 2019 - Jan 2020")

MOST IMPORTANTLY OUTPUT JSON MUST BE THE SAME FORMAT AS THE EXAMPLE GIVEN  :- ( {sample_format}  )

and Job Description (  )
"""

st.write("Prompt, JSON & Job Description")
st.write(custom_prompt)

# Create a button for copying text to clipboard
if st.button("Copy to Clipboard"):
    pyperclip.copy(custom_prompt)
    st.success("Text copied to clipboard!")