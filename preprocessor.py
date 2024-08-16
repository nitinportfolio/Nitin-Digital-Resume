import pandas as pd
import numpy as np
import streamlit as st
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""


st.markdown(no_sidebar_style, unsafe_allow_html=True)
