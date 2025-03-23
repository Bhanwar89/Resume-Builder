from fpdf import FPDF
from fpdf.enums import WrapMode
import markdown2
import json
import io

default_fields = {
    "info" : {
        "name": "Bhanwar Preet Singh",
        "number": "(416)-832-1695",
        "address": "Toronto, ON",
        "email_link": "bhanwar.bps86@gmail.com",
        "linkedin_link": "bhanwar-singh",
        "Personal_site" : "www.neuralbps.com",
        "github" : "Bhanwar89",
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
        "Deep Learning Specialization - Coursera",
        "AWS Certified Machine Learning - LinkedIn Learning",
        "Tableau Essential Learning - LinkedIn Learning"
    ]
}


class PDF(FPDF):
    def name(self, info):
        self.add_page()
        self.set_font("Arial", "B", 20)
        self.cell(0, 10, info["name"], align="C")
        self.ln(10)

    def infoSec(self, info):
        self.set_font("Arial", "I", 10)
        self.cell(10)
        self.cell(text=f'{info["address"]} | {info["number"]} |', align="C")
        self.write_html(f'''
        <a href="mailto:{info["email_link"]}">
        
        {info["email_link"]}</a> | 

        <a href="https://www.linkedin.com/in/bhanwar-singh/"> 

        {info["linkedin_link"]}</a> | 

        <a href="https://www.neuralbps.com/"> 
        
        {info["Personal_site"]}</a> | 

        <a href="https://github.com/Bhanwar89"> 
        
        {info['github']}</a>
        ''')
        self.ln(1)


    def add_section_line(self):
        self.set_draw_color(169, 169, 169)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def add_transparent_line(self):
        self.set_draw_color(240, 240, 240)  # Very light gray
        self.set_line_width(0.1)  # Thinner line for a more subtle effect
        self.line(10, self.get_y(), 200, self.get_y())  # Draw the line
        self.ln(3) 

    def add_html_text(self, text):
        html_text = markdown2.markdown(text)
        self.set_font("Arial", "", 10)
        self.write_html(html_text)
        self.ln(3)

    def summary(self, fields):
        self.add_section_line()
        self.set_font("Arial", "B", 12)
        self.cell(0, 4, "Summary", ln=True)
        self.add_html_text(fields["Summary"])

    def tech_skills(self, fields):
        self.add_section_line()
        self.set_font("Arial", "B", 12)
        self.cell(0, 3, "Technical Skills", ln=True)
        self.add_html_text(fields["Tech Skills"])

    def work_experience(self, workExp):
        self.add_section_line()
        self.set_font("Arial", "B", 12)
        self.cell(0, 6, "Work Experience", ln=True)
        self.set_font("Arial", "B", 10)
        self.cell(100, 6, workExp['companyName'], align="L")
        self.cell(90, 6, workExp['location'], align="R", ln=True)
        self.set_font("Arial", "I", 10)
        self.cell(100, 2, workExp['jobTitle'], align="L")
        self.cell(90, 2, workExp['timeFrame'], align="R", ln=True)
        self.add_html_text(workExp['workDescription'])

    def project_experience(self, projectExp):
        self.add_section_line()
        self.set_font("Arial", "B", 12)
        self.cell(0, 6, "Project Experience", ln=True)
        for proj in projectExp.values():
            self.set_font("Arial", "B", 11)
            self.cell(0, 4, proj["name"], ln=True)
            self.set_font("Arial", "I", 11)
            self.multi_cell(0, 5,text= f'**Technologies:** {proj["techStack"]}', markdown=True)
            self.add_html_text(proj['projectDescription'])

    def education(self, education_data):
        self.add_section_line()
        self.set_font("Arial", "B", 12)
        self.cell(0, 6, "Education", ln=True)
        for edu in education_data.values():
            self.set_font("Arial", "B", 10)
            self.cell(100, 6, edu['name'], align="L")
            self.cell(90, 6, edu['location'], align="R", ln=True)
            self.set_font("helvetica", "", 10)
            self.cell(100, 6, edu['course'], align="L")
            self.cell(90, 6, edu['GradDate'], align="R", ln=True)
            self.ln(2)

    def certificates(self, certificates):
        self.add_section_line()
        self.set_font("Arial", "B", 12)
        self.cell(0, 4, "Certificates", ln=True)
        self.add_html_text('\n'.join([f"- {cert}" for cert in certificates]))

def generate_pdf(data):
    fields = data['fields']
    workExp = data['workExp']
    projectExp = data['projectExp']
    info = default_fields["info"]
    education_data = default_fields['education']
    certificates = default_fields["certificates"]

    pdf = PDF()
    pdf.name(info)
    pdf.infoSec(info)
    pdf.summary(fields)
    pdf.tech_skills(fields)
    pdf.work_experience(workExp)
    pdf.project_experience(projectExp)
    pdf.education(education_data)
    pdf.certificates(certificates)

    buffer = io.BytesIO()
    pdf.output(buffer)

    return buffer


