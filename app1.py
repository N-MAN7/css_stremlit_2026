# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 09:48:48 2026

@author: ntoto
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Nhleleko | Portfolio",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("👨‍🎓 Nhleleko")
st.subheader("Mathematics & Statistics Student | University of Venda")

st.write(
    "Interactive academic portfolio showcasing my background, skills, and interests."
)

st.divider()

# Sidebar navigation
st.sidebar.title("📍 Navigation")

if "page" not in st.session_state:
    st.session_state.page = "About"

if st.sidebar.button("👤 About Me"):
    st.session_state.page = "About"

if st.sidebar.button("🎓 Education"):
    st.session_state.page = "Education"

if st.sidebar.button("🛠 Skills"):
    st.session_state.page = "Skills"

if st.sidebar.button("📊 Projects & Interests"):
    st.session_state.page = "Projects"

if st.sidebar.button("📬 Contact"):
    st.session_state.page = "Contact"

# Content rendering
page = st.session_state.page

if page == "About":
    st.header("👤 About Me")
    st.write(
        """
        I am **Nhleleko**, a 20-year-old student at the **University of Venda**,
        studying **Mathematics and Statistics**.

        I have a strong interest in problem-solving, data analysis,
        programming, and applying mathematical and statistical methods
        to real-world problems.
        """
    )

elif page == "Education":
    st.header("🎓 Education")
    st.markdown(
        """
        **Bachelor of Mathematics and Statistics**  
        University of Venda  

        **High School Qualification**  
        Electrical Technology (Electronics)
        """
    )

elif page == "Skills":
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

elif page == "Projects":
    st.header("📊 Academic Interests & Projects")
    st.markdown(
        """
        - Data analysis with Python (Pandas, NumPy)
        - Algorithm design and problem solving
        - Financial mathematics and trading analysis
        - Building educational and analytical applications
        """
    )

elif page == "Contact":
    st.header("📬 Contact Information")
    st.write(
        """
        **Name:** Nhleleko  
        **Email:** ntotonhleleko@gmail.com  
        **University:** University of Venda  
        **Field:** Mathematics & Statistics  
        """
    )

st.divider()
st.caption("© 2026 Nhleleko | Interactive Portfolio")
