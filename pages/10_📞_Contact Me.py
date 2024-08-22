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
DESCRIPTION = " Senior Data Scientist/ AI Consultant"
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


    st.write("📩", EMAIL)
    st.write("📞", CONTACT)

# ---- SOCIAL LINKS ----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ---- CONTACT ----
with st.container():
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