from pathlib import Path

import streamlit as st
from PIL import Image


# -----PATH SETTINGS ----
current_dir = Path(_file_).parent if"_file_" in locals() else Path.cwd()
css_file = current_dir/"style"/"main.css"
resume_file = current_dir/"assets"/"Nitin-Resume.pdf"
profile_pic = current_dir/"assets"/"Nitin-Pic.png"
img_recommendation = current_dir/"assets"/"movie.jpg"
img_olympics = current_dir/"assets"/"olympics.png"




# ---- GENERAL SETTINGS ----
PAGE_TITLE = "Digital Resume | Nitin Monga"
PAGE_ICON = ":wave"
NAME = "Nitin Monga"
DESCRIPTION = " Senior Data Scientist "
EMAIL = "nitinmonga@gmail.com"
CONTACT = "+91 7022945888"
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/nitinmonga-ai/",
    "GitHub":"https://github.com/nitinportfolio",
    "Portfolio": "https://nitinportfolio"
}
PROJECTS = {
    "🎖️Recommendation Engine - Recommending Movies that you might like based on your interest. Clike here"
    "🎖️Olympics Analysis - Analysing Olympics data. Clike here"
    "🎖️Olympics Analysis - Analysing Olympics data. Clike here"
    "🎖️Olympics Analysis - Analysing Olympics data. Clike here"
    "🎖️Olympics Analysis - Analysing Olympics data. Clike here"
    "🎖️Olympics Analysis - Analysing Olympics data. Clike here"
}
st.set_page_config(page_title = PAGE_TITLE, page_icon=PAGE_ICON)
#####################################################
#t.markdown("<style> {display: none;} </style>", unsafe_allow_html=True)


#############################################################---


#st.markdown("<style> app.py {display: none;} </style>", unsafe_allow_html=True)


# ---- LOAD CSS, PDF, & PROFILE PIC ----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
img_recommendation = Image.open(img_recommendation)
img_olympics = Image.open(img_olympics)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("style/style.css")

# ---- HERO SECTION ----
col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(profile_pic, width = 230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "📄 Download Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream",
    )
    st.write("📩", EMAIL)
    st.write("📞", CONTACT)

# ---- SOCIAL LINKS ----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ---- EXPERIENCE & QUALIFICATIONS ----
st.write("#")
st.subheader("Work Experience")

st.write("**Xilytica**  \nData Science Freelance Consultant & Trainer  \nFeb 2014 - Present")
#st.write("######")
st.write("**Wipro Technologies, Bangalore**  \nTechnical Lead/ Manager  \nOct 2011 – 31 Jan 2014")
st.write("**ACS - A Xerox Company, Bangalore**  \nSr. Technical Lead  \nFeb 2009 – Oct 2011")
st.write("**3i INFOTECH Inc., New Jersey, U.S.A.**  \nTechnical Analyst  \nMar 2007 – Dec 2008")
st.write("**3i INFOTECH Ltd., Chennai**  \nSoftware Engineer  \nJan 2005 – Feb 2007")

st.write('#####')

st.subheader("Career Summary")
st.write("""
- 5+ Years as a Data Science, Machine Learning & Deep Learning Trainer, providing training & consulting solutions to Companies, Colleges & Individuals.
- 7+ Years of Entrepreneur/Start-Up experience that involved building Training Platforms, Business Development, Sales & Marketing.
- 10+ Years in IT Industry with demonstrated capability in Databases, SQL, PLSQL, & Business Intelligence Reporting.
- 2 + Years of experience in handling & managing IT projects as a project manager.
""")

st.subheader("Management Competencies")
st.write("""
- Understand & map client’s requirements & enhancements to the product and provide technical solutions.
- Maintaining MIS for all phases and reporting project progress to the client & management.
- Creating a WBS (Work Breakdown Structure) to define and organize the total project scope Project planning, estimation, and tracking.
- Define escalation/response/resolution time for reported roblems on the basis of criticality.
- Team mentoring, deployment, monitoring, and development.
- Providing pre-sales technical/estimation support to the business development team.
""")

st.subheader("Core Skills")
st.markdown("<h5>Data Science & Machine Learning Tools</h5>",unsafe_allow_html=True)
st.markdown("""
- Python
- R 
- SQL
- SkLearn
- TensorFlow 2.0
- PowerBI
- Tableau
- Statistics
- Streamlit
- PL-SQL
- HTML & CSS
- Oracle Database
""")
st.write("######")
st.markdown("<h5>Data Science & Machine Learning Skills</h5>", unsafe_allow_html = True)

st.write("""
- **Data Analysis:** Analysing data to understand data, data types, correlations 
- **Regression:** Simple, Multiple Regression, Lasso Regression,Ridge Regression, KNN, etc
- **Classification:** Logistic Regression, SVM, Decision Tree, Random Forest, XGBoost, etc
- **Clustering:** K Means Clustering, Hierarchical Clustering 
- Forecasting
- Computer Vision
- Visualisations
- NLP - Natural Language Processing
- ANN - Artificial Neural Network
- CNN - Convolutional Neural Network 
- RNN - Recurrent Neural Network
""")

        #---- PROJECTS ----#
with st.container():

    st.write("---")
    st.header("My Data Science Projects")
    st.write("##")
    image_column, text_column = st.columns([1,2])
    with image_column:
        st.image(img_recommendation)
    with text_column:
        st.subheader(" Movie Recommender System")
        st.write(
            """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
            """
        )
        st.markdown("[Watch GitHub Repo](https://github.com/nitinportfolio/gitportfolio.git)")

    st.write("#")
    st.write("#")
    st.write("##")

with st.container():

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_olympics)
    with text_column:
        st.subheader("Olympics Analysis")
        st.write(
            """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
            """
        )
        st.markdown("[View Demo ](http://localhost:8501/Olympics_Analysis")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https??formsubmit.com/ !!!
    contact_form = """
    <form action="https://formsubmit.co/nitinaiportfolio@gmail.com" method="POST">
    <input type = "hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name = "message" placeholder = Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html = True)
    with right_column:
        st.empty()








