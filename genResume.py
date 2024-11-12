from fpdf import FPDF
from fpdf.enums import WrapMode
import markdown2
import json
import io

class PDF(FPDF):
    def name(self, fields):
        self.add_page()
        self.set_font("helvetica", "B", 19)
        self.cell(0, 10, fields["name"], align="C")
        self.ln(10)

    def infoSec(self, fields):
        self.set_font("helvetica", "I", 10)
        self.cell(10)
        self.cell(text=f'{fields["address"]} | {fields["number"]} | ', align="C")
        self.write_html(f'<a href = " mailto : {fields["email_link"]} " > {fields["email_link"]} </a> | <a href = " {fields["linkedin_link"]} " > {fields["linkedin_link"]} </a>')
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
        self.set_font("helvetica", "", 10)
        self.write_html(html_text)
        self.ln(3)

    def summary(self, fields):
        self.add_section_line()
        self.set_font("helvetica", "B", 11)
        self.cell(0, 4, "Summary", ln=True)
        self.add_html_text(fields["Summary"])

    def tech_skills(self, fields):
        self.add_section_line()
        self.set_font("helvetica", "B", 11)
        self.cell(0, 3, "Technical Skills", ln=True)
        self.add_html_text(fields["Tech Skills"])

    def work_experience(self, workExp):
        self.add_section_line()
        self.set_font("helvetica", "B", 11)
        self.cell(0, 6, "Work Experience", ln=True)
        self.set_font("helvetica", "B", 10)
        self.cell(100, 6, workExp['companyName'], align="L")
        self.cell(90, 6, workExp['location'], align="R", ln=True)
        self.set_font("helvetica", "I", 10)
        self.cell(100, 2, workExp['jobTitle'], align="L")
        self.cell(90, 2, workExp['timeFrame'], align="R", ln=True)
        self.add_html_text(workExp['workDescription'])

    def project_experience(self, projectExp):
        self.add_section_line()
        self.set_font("helvetica", "B", 11)
        self.cell(0, 6, "Project Experience", ln=True)
        for proj in projectExp.values():
            self.set_font("helvetica", "B", 10)
            self.cell(0, 4, proj["name"], ln=True)
            self.set_font("helvetica", "I", 10)
            self.multi_cell(0, 5,text= f'**Technologies:** {proj["techStack"]}', markdown=True)
            # self.add_transparent_line()
            # self.multi_cell(0, 5, text= f'{proj["projectDescription"]}', markdown=True)
            # self.add_transparent_line()
            self.add_html_text(proj['projectDescription'])

    def education(self, education_data):
        self.add_section_line()
        self.set_font("helvetica", "B", 11)
        self.cell(0, 6, "Education", ln=True)
        for edu in education_data.values():
            self.set_font("helvetica", "B", 10)
            self.cell(100, 6, edu['name'], align="L")
            self.cell(90, 6, edu['location'], align="R", ln=True)
            self.set_font("helvetica", "", 10)
            self.cell(100, 6, edu['course'], align="L")
            self.cell(90, 6, edu['GradDate'], align="R", ln=True)
            self.ln(2)

    def certificates(self, certificates):
        self.add_section_line()
        self.set_font("helvetica", "B", 11)
        self.cell(0, 4, "Certificates", ln=True)
        self.add_html_text('\n'.join([f"- {cert}" for cert in certificates]))

def generate_pdf(data):

    fields = data['fields']
    workExp = data['workExp']
    projectExp = data['projectExp']
    education_data = data['education']
    certificates = data['certificates']

    pdf = PDF()
    pdf.name(fields)
    pdf.infoSec(fields)
    pdf.summary(fields)
    pdf.tech_skills(fields)
    pdf.work_experience(workExp)
    pdf.project_experience(projectExp)
    pdf.education(education_data)
    pdf.certificates(certificates)

    buffer = io.BytesIO()
    pdf.output(buffer)

    return buffer


