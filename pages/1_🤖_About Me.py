from pathlib import Path

import streamlit as st
from PIL import Image


# -----PATH SETTINGS ----
current_dir = Path(_file_).parent if"_file_" in locals() else Path.cwd()
print(current_dir)
#print(Path(_file_).parent)
print(Path.cwd())
css_file = current_dir/"style"/"main.css"
resume_file = current_dir/"assets"/"Nitin-Resume.pdf"
profile_pic = current_dir/"assets"/"Nitin-Pic.png"
img_recommendation = current_dir/"assets"/"movie.jpg"
img_olympics = current_dir/"assets"/"olympics.png"




# ---- GENERAL SETTINGS ----
PAGE_TITLE = "Digital Resume | Nitin Monga"
PAGE_ICON = ":wave"
NAME = "Nitin Monga"
DESCRIPTION = " Senior Data Scientist/ AI Consultant "
#EMAIL = "nitinmonga@gmail.com"
CONTACT = "+91 7022945888"
EMAIL = "nitinmonga@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/nitinmonga-ai/",
    "GitHub":"https://github.com/nitinportfolio",
    "Portfolio": "https://nitinaiportfolio.com"
}



st.set_page_config(page_title = PAGE_TITLE, page_icon=PAGE_ICON)


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
#st.subheader("About Me")


# st.write(f"temprature: :blue[{temperature}]")
# st.write("**bold** not bold")
st.write("""I am a highly skilled and results-driven **Data Scientist and Artificial Intelligence Engineer** with a profound dedication to leveraging advanced AI and Machine Learning technologies to tackle intricate challenges. My expertise traverses multiple domains, including **Statistical Data Analysis, Machine Learning, Deep Learning, Natural Language Processing, Computer Vision, Genrative AI, LangChain and Large Language Models**. Equipped with a deep understanding of these domains, I adeptly design and implement innovative solutions that drive impactful outcomes.

Proficient in programming languages such as **Python, R, and SQL**, I possess a robust foundation in handling vast datasets and extracting actionable insights. My proficiency extends to data visualization and communication, enabling me to **effectively convey technical findings to both technical and non-technical stakeholders**. I take pride in my ability to distill complex concepts into digestible insights, facilitating informed decision-making across diverse teams and departments.

Thriving in dynamic environments, I am committed to remaining at the **forefront of AI technologies**, continually expanding my skill set and exploring emerging trends. With a relentless pursuit of excellence, I am driven to make a meaningful impact through the application of **cutting-edge AI solutions**.

I am extensively engaged in delivering comprehensive training sessions tailored for prominent global IT enterprises, focusing specifically on the dynamic fields of Data Science and Machine Learning. These sessions encompass a wide range of topics, including but not limited to **Data Analysis, Predictive Modeling, Deep Learning, NLP, GenAI, LangChain, LLMs and Development & Deployment AI applications**.

Over time, I have conceptualized and executed **algorithmic trading strategies utilizing Python and AI frameworks** for various trading clientele. Utilize machine learning techniques to **analyze market data and identify profitable trading opportunities**. Additionally, I have adeptly provided training to non-technical individuals in effectively utilizing these algorithmic trading methodologies.

I bring forth over **19 years of diverse and extensive experience spanning the breadth of the IT domain**, coupled with a dedicated focus of over 8 years specifically within the realm of Data Science and Machine Learning technology stack. Throughout my career journey, I have honed a robust skill set encompassing various facets of IT, including **software development, project management, and strategic planning**, while concurrently immersing myself in the cutting-edge innovations of Data Science and Machine Learning.""")
st.write("#")
st.markdown("#### **Work Experience**")

st.write("**Xilytica**  \nData Science Freelance Consultant & Trainer  \nFeb 2014 - Present")
#st.write("######")
st.write("**Wipro Technologies, Bangalore**  \nTechnical Lead/ Manager  \nOct 2011 – 31 Jan 2014")
st.write("**ACS - A Xerox Company, Bangalore**  \nSr. Technical Lead  \nFeb 2009 – Oct 2011")
st.write("**3i INFOTECH Inc., New Jersey, U.S.A.**  \nTechnical Analyst  \nMar 2007 – Dec 2008")
st.write("**3i INFOTECH Ltd., Chennai**  \nSoftware Engineer  \nJan 2005 – Feb 2007")

st.write('#####')

st.markdown("#### **Career Summary**")
st.write("""
- 5+ Years as a Data Science, Machine Learning & Deep Learning Trainer, providing training & consulting solutions to Companies, Colleges & Individuals.
- 7+ Years of Entrepreneur/Start-Up experience that involved building Training Platforms, Business Development, Sales & Marketing.
- 10+ Years in IT Industry with demonstrated capability in Databases, SQL, PLSQL, & Business Intelligence Reporting.
- 2 + Years of experience in handling & managing IT projects as a project manager.
""")

st.markdown("#### **Management Competencies**")
st.write("""
- Understand & map client’s requirements & enhancements to the product and provide technical solutions.
- Maintaining MIS for all phases and reporting project progress to the client & management.
- Creating a WBS (Work Breakdown Structure) to define and organize the total project scope Project planning, estimation, and tracking.
- Define escalation/response/resolution time for reported roblems on the basis of criticality.
- Team mentoring, deployment, monitoring, and development.
- Providing pre-sales technical/estimation support to the business development team.
""")

st.markdown("#### **Core Skills**")
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
st.markdown("""
##### **Financial Analysis & Equity Market**
- Algorithmic Trading
- Fundamental Analysis
- Technical Analysis
- Financial Modeling
- Market Data Analysis
- Portfolio Optimization
- Backtesting Algo Trading Strategies
- Trading Platform - Kite API/ Angelone API
""")

st.markdown("""
#### **Entrepreneurial Journey**
- I’ve single-handedly built my training and consulting platforms, Skill Venue and Xilytica,from the ground up. Idea was to built an online learning & mentoring platform to bringtrainers, mentors & college students/ working professionals to it. So that trainers, mentorscan provide their respective services to colleges & individuals. But due to unforeseencircumstances, had to pivot the platform to providing Data Science & Machine LearningTraining & Consulting platform.
- While delivering tangible outcomes for my clients, I was also involved in actively developing business leads and onboarding trainers & mentors for my clients.
- I’ve also dipped my toes into digital marketing, content strategy, and running digital advertising, generating leads over various social platforms for my companies.
- Lastly, recruiting, and grooming talent has been a pleasant outcome of my entrepreneurial venture as I have got to be part of several people’s career journeys.
- Since last few years, I have trained & mentored many college students & working professionals in Data Science & Machine learning.
- I have been undertaking Data Science & AI projects to companies & start-ups in India & US.
""")

st.markdown("----------------------------------")
st.markdown("""
#### **Corporate Journey**
""")
st.markdown(
    """
##### **Wipro Technologies**\n
###### *Lead/ Manager*\n
**ANZ Bank - Migrating Bank's Servers & Software to Latest Version**

- Managing a team of 15+ members.
- Determine overall project plan, structure, schedule, and staffing requirements.
- Actively participated in a weekly status meeting with the client, discussing project status and bottlenecks.
- Tracking work progress, conducting daily stand-up calls to get the daily status, andunderstanding bottlenecks or risks if any.
- Coordinating with offshore team, ensuring on-time deliverables.
- Delegating work to the team members based on the skills and keeping management informed on deliverables and raising red flags whenever saw any risk.
- Involved in other management activities such as – Resource Management: resource planning and loading, project planning, working on cost estimation sheet, work allocation,reporting internal and external project performance on a periodic basis, and other activitiesusing Wipro-specific tools and matrix.\n

**CITI Bank - Operational Risk Management**

- Leading a team of 8 + members.
- Involved in requirement gathering, analysis, and feasibility.
- Involved in data analysis, database design, and developing and tuning critical PL/SQL objects.
- Technical discussion with the clients on technical design and taking inputs.
- Effective Monitoring, requirement, and work progress tracking.
- Involved in code review, design, test scenarios & Unit test cases.
- Working with the various streams, Project documentation, Integrated Change Control;communication with the stakeholders, and handling escalations.

##### **ACS - A Xerox Company**
###### *Sr. Tech Lead*


**Michlen & Office Depot
DIGITAL FUEL - Implementation Digital Fuel BI tool**

- Build & trained the technical & functional team of 10+ members
- Implemented Digital Fuel Service Flow BI Reporting tool for different clients.
- Helping and guiding team members on the technical front whenever required.
- Daily status call with the client and stakeholders on status and bottlenecks.
- Determine overall project plan, structure, schedule, and staffing requirements.
- Ensuring target realizations and bulge ratios, Implementing service improvement plans,giving leads to senior management.
- Performed capacity planning and was responsible for project prioritization by providing information about the resource availability to business managers, project sponsors &clients.

##### **3i Infotech, India/ US**
###### *Software Engineer*
**PSCM, John Snow Inc - Oracle BI Reports, Database**

- Involved in requirement gathering & delivery for different Discoverer BI reports.
- Coordinating with the offshore team for delegation, requirement clarifications, and on-time delivery of project modules.
- Testing deliverables to make sure development is bugs-free and aligned with the client’s requirements.
- Involved in Database design, developing PL/SQL objects, and creating different Oracle BI reports.
- Created new database PL/SQL objects such as packages, procedures, and triggers and also customized existing objects.
- Responsible for testing the development patches before applying to the UAT or production environment and also responsible for on-time teams deliverables.
    """
)

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https??formsubmit.com/ !!!
    contact_form = """
    <form action="https://formsubmit.co/nitinportfolio.ai@gmail.com" method="POST">
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








