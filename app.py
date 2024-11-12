import streamlit as st
from genResume import generate_pdf
import json
import pyperclip



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
st.json({
    "fields": {
        "name": "Bhanwar Preet Singh",
        "number": "(416)-832-1695",
        "address": "Toronto, ON",
        "email_link": "bhanwar.bps86@gmail.com",
        "linkedin_link": "www.linkedin.com/in/bhanwar-preet-singh",
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
    },
    "education": {
        "s1": {
            "name": "Loyalist College",
            "course": "Ontario College Graduate Certificate in AI and Data Science",
            "location": "Toronto, ON",
            "GradDate": "Aug 2024"
        },
        "s2": {
            "name": "SGTB Institute of Management and Information Tech",
            "course": "BCA - Bachelor of Computer Application",
            "location": "New Delhi, India",
            "GradDate": "Apr 2021"
        }
    },
    "certificates": [
        "MERN Stack - LinkedIn Learning",
        "AWS Certified Machine Learning - LinkedIn Learning",
        "Tableau Essential Learning - LinkedIn Learning"
    ]
}, expanded=False
)



custom_prompt = "Here is some text you can copy!"

st.write("Prompt, JSON & Job Description")
st.write(custom_prompt)

# Create a button for copying text to clipboard
if st.button("Copy to Clipboard"):
    pyperclip.copy(custom_prompt)
    st.success("Text copied to clipboard!")