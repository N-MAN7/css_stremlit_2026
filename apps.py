# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 14:50:34 2026

@author: ntoto
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Nhleleko | Portfolio",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("👨‍🎓 Nhleleko")
st.subheader("Mathematics & Statistics Student | University of Venda")

st.write(
    """
    Welcome to my academic portfolio.  
    This page showcases my background, skills, and interests in Mathematics,
    Statistics, programming, and data-related work.
    """
)

st.divider()

# About Me
st.header("📌 About Me")
st.write(
    """
    I am a 20-year-old student at the **University of Venda**, studying
    **Mathematics and Statistics**.  
    I am passionate about problem-solving, data analysis, programming,
    and applying mathematical concepts to real-world problems.
    """
)

# Education
st.header("🎓 Education")
st.markdown(
    """
    - **Bachelor's Degree**  
      *Mathematics and Statistics*  
      **University of Venda**
    """
)

# Skills
st.header("🛠 Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        **Programming**
        - Python
        - C++
        - Java
        - HTML
        - SQL
        """
    )

with col2:
    st.markdown(
        """
        **Mathematics & Statistics**
        - Probability & Statistics
        - Algebra
        - Calculus
        - Data Analysis
        - Statistical Modelling
        """
    )

# Projects / Interests
st.header("📊 Academic Interests & Projects")
st.markdown(
    """
    - Data analysis using Python (Pandas, NumPy)
    - Algorithm design and problem solving
    - Financial mathematics and trading analysis
    - Building small systems and applications for learning
    """
)

# Contact
st.header("📬 Contact")
st.write(
    """
    **Name:** Nhleleko  
    **University:** University of Venda  
    **Field:** Mathematics & Statistics  
    """
)

st.divider()

st.caption("© 2026 Nhleleko | Student Portfolio")
