# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 09:48:48 2026

@author: ntoto
"""

import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Ntoto Nhleleko Ntimane | Portfolio",
    page_icon="📈",
    layout="wide"
)

# ---------------- STYLING & BACKGROUND ----------------
st.markdown("""
<style>
/* Background with visible data science theme */
.stApp {
    background-image:
        linear-gradient(
            rgba(13,110,253,0.35),
            rgba(111,66,193,0.35)
        ),
        url("https://images.unsplash.com/photo-1551288049-bebda4e38f71");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Hero text */
.big-title {
    font-size: 48px;
    font-weight: 800;
    color: white;
}
.subtitle {
    font-size: 22px;
    color: #f8f9fa;
}

/* Card styling */
.card {
    padding: 25px;
    border-radius: 15px;
    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}

/* Badges */
.badge {
    display: inline-block;
    padding: 8px 14px;
    margin: 5px;
    border-radius: 20px;
    background-color: #0d6efd;
    color: white;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown('<p class="big-title">Ntoto Nhleleko Ntimane</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Mathematics & Statistics Student | University of Venda</p>',
    unsafe_allow_html=True
)

st.write(
    "📊 Aspiring data-driven problem solver with a strong foundation in mathematics, "
    "statistics, programming, and analytical thinking."
)

st.divider()

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)
col1.metric("🎓 Field", "Maths & Stats")
col2.metric("🎂 Age", "20")
col3.metric("📈 Interest", "Data Science")

st.divider()

# ---------------- TABS ----------------
tabs = st.tabs([
    "👤 About",
    "🎓 Education",
    "🛠 Skills",
    "🌍 Languages",
    "📊 Interests",
    "📬 Contact"
])

# ---------------- ABOUT ----------------
with tabs[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("👤 About Me")
    st.write(
        """
        I am **Ntoto Nhleleko Ntimane**, a student at the **University of Venda**
        studying **Mathematics and Statistics**.

        My interests lie in **data science**, **analytics**, and applying
        mathematical and statistical methods to solve real-world problems.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- EDUCATION ----------------
with tabs[1]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🎓 Education")
    st.markdown(
        """
        **Bachelor of Mathematics and Statistics**  
        University of Venda  

        **High School**  
        Electrical Technology (**Electronics**)
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SKILLS ----------------
with tabs[2]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🛠 Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Programming")
        st.markdown("""
        - Python  
        - C++  
        - Java  
        - HTML  
        - SQL  
        """)

    with col2:
        st.subheader("Mathematics & Statistics")
        st.markdown("""
        - Probability & Statistics  
        - Calculus  
        - Algebra  
        - Data Analysis  
        - Statistical Modelling  
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- LANGUAGES ----------------
with tabs[3]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🌍 Languages Spoken")
    st.markdown("""
    <span class="badge">English</span>
    <span class="badge">Xitsonga</span>
    <span class="badge">Afrikaans</span>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- INTERESTS ----------------
with tabs[4]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📊 Academic Interests")
    st.markdown("""
    - Data Science & Analytics  
    - Financial Mathematics & Trading  
    - Algorithm Design  
    - Statistical Computing  
    - Building analytical applications
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTACT ----------------
with tabs[5]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📬 Contact")
    st.markdown(
        """
        **Name:** Ntoto Nhleleko Ntimane  
        **Email:** ntotonhleleko@gmail.com  
        **University:** University of Venda  
        **Field:** Mathematics & Statistics  
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Ntoto Nhleleko Ntimane | Data Science Portfolio")
