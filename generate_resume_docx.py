from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# Core content for Vaibhav Jain
name = "VAIBHAV JAIN"
role = "Full-Stack Developer (MERN & React Native)"
location = "Bhilwara"
email = "developer.vaibhavjain@gmail.com"
linkedin = "LinkedIn"
phone = "6377137304"

summary = (
    "Highly motivated Full-Stack Developer specializing in MERN Stack and React Native, "
    "with a strong ability to build scalable web and mobile applications. Skilled in developing "
    "RESTful APIs with Node.js and Express, integrating MongoDB for data-driven solutions, and "
    "delivering cross-platform apps using React Native. Experienced in Agile environments with a focus "
    "on performance, clean code, and intuitive UI/UX. Quick learner with excellent problem-solving and "
    "debugging skills, passionate about continuous learning and staying updated with modern JavaScript technologies."
)

soft_skills = [
    "Design Understanding",
    "Team Collaboration",
    "Problem Solving",
    "Visual Design",
]

tech_skills = [
    "C, C++, Java (Basics)",
    "Data Structures & Algorithms",
    "HTML, CSS, JavaScript",
    "MERN Stack (MongoDB, Express, React, Node.js)",
    "React Native",
    "Bootstrap, Tailwind CSS, NativeWind",
    "REST APIs",
    "IoT",
    "Git, Postman",
]

projects = [
    ("Static Websites (Aug–Nov 2022)",
     "Built and deployed multiple business websites: GYM, Real Estate, Restaurant, Namkeen, Palak Computer, UPACA."),
    ("Portfolio (Jan 2023)",
     "Personal portfolio with clean, responsive UI and dynamic backend integration to showcase projects and skills."),
    ("Social Media Web App (Feb–Mar 2023)",
     "Full-featured MERN application with JWT auth, bcrypt, Cloudinary media uploads, regex email validation; "
     "features include posts, edit/delete, comments, follow system, and scalable MongoDB design."),
    ("Mobile Apps (Jul 2023)",
     "Developed various React Native apps: Food Delivery, Food Recipe, Apna Ghar, GYM, Movie, YouTube, Chat, Online Shop, Grow, Reelz."),
]

experience = [
    ("Web Design Intern — 150 Hours", 
     "Built responsive sites using HTML, CSS, JavaScript and collaborated on client projects (paid internship)."),
    ("Search Your College — React Migration", 
     "Redesigned and converted platform to React, improving load time by ~40% and scalability."),
    ("AB Tech Advisor — Software Engineer (Sep 2023 – Feb 2025)",
     "Developed and maintained cross-platform mobile apps in React Native; deployed features that increased user engagement by ~30%."),
]

education = [
    ("B.Tech, Computer Science — MDSU Ajmer", 
     "CGPA: 85% (Top rank in class). Projects with JavaScript, PHP, MySQL; active in clubs and coding contests."),
]

achievements = [
    "Hackathon participant at M.L.V. Textile & Engineering College",
]

certifications = [
    "Skill India: Corel Draw, Tally, Website Design",
    "Infosys: Spring Boot / React Native (workshops)",
    "Deloitte Technology & AWS (sessions)",
    "DSA with C++",
    "JioCinema React Clone",
    "Postman API Fundamentals",
    "SQL, JavaScript (Let’s Upgrade/NSDC)",
    "Workshops: ITM Wdutech Training Pvt. Ltd., GDG MAD (Google)",
]

languages = ["English", "Hindi"]

# Create document
document = Document()
section = document.sections[0]
# Narrow margins for modern resume look
section.top_margin = Inches(0.4)
section.bottom_margin = Inches(0.4)
section.left_margin = Inches(0.4)
section.right_margin = Inches(0.4)

# Create two-column layout using a full-width table
# Left column as teal sidebar, right column as content area
content_width = section.page_width - section.left_margin - section.right_margin
left_width = Inches(2.6)
right_width = content_width - left_width

table = document.add_table(rows=1, cols=2)
table.autofit = False

left_cell = table.rows[0].cells[0]
right_cell = table.rows[0].cells[1]

left_cell.width = left_width
right_cell.width = right_width

# Teal background for left sidebar
teal_hex = "43B97F"  # matches repo primary color
left_cell._tc.get_or_add_tcPr().append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{teal_hex}"/>'))

# Helper functions

def add_heading(paragraph, text, size=18, bold=True, color=None, all_caps=False):
    run = paragraph.add_run(text.upper() if all_caps else text)
    run.bold = bold
    run.font.size = Pt(size)
    if color:
        run.font.color.rgb = RGBColor.from_string(color)
    paragraph.space_after = Pt(4)
    return paragraph


def add_bullets(container, items, color=None):
    for item in items:
        p = container.add_paragraph(style=None)
        p.style = document.styles["List Bullet"]
        run = p.add_run(item)
        if color:
            run.font.color.rgb = RGBColor.from_string(color)
        run.font.size = Pt(10.5)


# LEFT SIDEBAR CONTENT
# Name block (reversed color)
name_p = left_cell.paragraphs[0]
add_heading(name_p, name, size=22, bold=True, color="FFFFFF")
role_p = left_cell.add_paragraph()
add_heading(role_p, role, size=12, bold=False, color="FFFFFF")

# Space
left_cell.add_paragraph(" ")

# Contact
contact_title = left_cell.add_paragraph()
add_heading(contact_title, "CONTACT", size=11, color="FFFFFF")

contact_items = [
    f"{location}",
    f"{email}",
    f"{linkedin}",
    f"{phone}",
]
add_bullets(left_cell, contact_items, color="FFFFFF")

# Skills
left_cell.add_paragraph(" ")
skills_title = left_cell.add_paragraph()
add_heading(skills_title, "PROFESSIONAL SKILLS", size=11, color="FFFFFF")
add_bullets(left_cell, soft_skills, color="FFFFFF")

left_cell.add_paragraph(" ")
tech_title = left_cell.add_paragraph()
add_heading(tech_title, "TECHNICAL SKILLS", size=11, color="FFFFFF")
add_bullets(left_cell, tech_skills, color="FFFFFF")

left_cell.add_paragraph(" ")
language_title = left_cell.add_paragraph()
add_heading(language_title, "LANGUAGES", size=11, color="FFFFFF")
add_bullets(left_cell, languages, color="FFFFFF")

left_cell.add_paragraph(" ")
ach_title = left_cell.add_paragraph()
add_heading(ach_title, "ACHIEVEMENTS", size=11, color="FFFFFF")
add_bullets(left_cell, achievements, color="FFFFFF")

left_cell.add_paragraph(" ")
cert_title = left_cell.add_paragraph()
add_heading(cert_title, "CERTIFICATIONS & AWARDS", size=11, color="FFFFFF")
add_bullets(left_cell, certifications, color="FFFFFF")

# RIGHT COLUMN CONTENT
# Header with name for emphasis
header = right_cell.paragraphs[0]
add_heading(header, name, size=24, bold=True, color="333333")
sub = right_cell.add_paragraph()
add_heading(sub, role, size=12, bold=False, color="1F7A5F")

right_cell.add_paragraph(" ")

# Summary
sum_title = right_cell.add_paragraph()
add_heading(sum_title, "ABOUT ME", size=13, color="1F7A5F", all_caps=True)

sum_p = right_cell.add_paragraph(summary)
sum_p.alignment = WD_ALIGN_PARAGRAPH.LEFT
for run in sum_p.runs:
    run.font.size = Pt(10.5)
    run.font.color.rgb = RGBColor(60, 60, 60)

right_cell.add_paragraph(" ")

# Education
edu_title = right_cell.add_paragraph()
add_heading(edu_title, "EDUCATION", size=13, color="1F7A5F", all_caps=True)
for title, desc in education:
    t = right_cell.add_paragraph()
    add_heading(t, title, size=11, bold=True, color="333333")
    d = right_cell.add_paragraph(desc)
    for run in d.runs:
        run.font.size = Pt(10.5)
        run.font.color.rgb = RGBColor(60, 60, 60)

right_cell.add_paragraph(" ")

# Career Summary / Experience
exp_title = right_cell.add_paragraph()
add_heading(exp_title, "CAREER SUMMARY", size=13, color="1F7A5F", all_caps=True)
for title, desc in experience:
    t = right_cell.add_paragraph()
    add_heading(t, title, size=11, bold=True, color="333333")
    d = right_cell.add_paragraph(desc)
    for run in d.runs:
        run.font.size = Pt(10.5)
        run.font.color.rgb = RGBColor(60, 60, 60)

right_cell.add_paragraph(" ")

# Projects
proj_title = right_cell.add_paragraph()
add_heading(proj_title, "PROJECTS", size=13, color="1F7A5F", all_caps=True)
for title, desc in projects:
    t = right_cell.add_paragraph()
    add_heading(t, title, size=11, bold=True, color="333333")
    d = right_cell.add_paragraph(desc)
    for run in d.runs:
        run.font.size = Pt(10.5)
        run.font.color.rgb = RGBColor(60, 60, 60)

# Save file
output_path = "/workspace/Vaibhav_Jain_Resume.docx"
document.save(output_path)
print(output_path)
