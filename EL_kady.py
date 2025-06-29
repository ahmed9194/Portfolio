import streamlit as st
from PIL import Image
import pandas as pd

# Configure page
st.set_page_config(
    page_title="Ahmed Hesham | AI Engineer & Full-Stack Developer",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .header {font-family: 'Segoe UI', sans-serif; color: #1e3a8a}
    .project-card {
        border-left: 4px solid #3b82f6;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-radius: 0 8px 8px 0;
    }
    .tech-badge {
        display: inline-block;
        background: #1e40af;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .social-btn {
        display: inline-block;
        padding: 0.5rem 1rem;
        background: #1e40af;
        color: white !important;
        border-radius: 6px;
        text-decoration: none !important;
        margin-right: 0.5rem;
    }
    input, textarea, button {
        width: 100%;
        padding: 0.75rem;
        margin-top: 0.5rem;
        border-radius: 6px;
        border: 1px solid #ccc;
        font-size: 1rem;
    }
    button {
        background-color: #1e40af;
        color: white;
        border: none;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# Load profile image
profile_img = Image.open("CV.jpg")

# Hero Section
col1, col2 = st.columns([1, 2])
with col1:
    st.image(profile_img, width=250)

with col2:
    st.markdown('<h1 class="header">Ahmed Hesham Elkady</h1>', unsafe_allow_html=True)
    st.markdown("### AI Engineer & Full-Stack Developer")
    st.write("B.Sc. in Computer & Data Science - Intelligent Systems | Alexandria National University")
    st.write("📊 CGPA: 3 | 🎓 Class of 2027")
    st.write("🚀 Passionate about building intelligent systems, AI-powered apps, and solving real-world problems using data and code.")

    st.markdown("""
    <div style="margin-top: 1rem;">
        <a href="https://github.com/ahmed9194" target="_blank" class="social-btn">GitHub</a>
        <a href="#contact" class="social-btn">Contact</a>
        <a href="cv.pdf" download class="social-btn">Download CV</a>
    </div>
    """, unsafe_allow_html=True)

# About Section
st.markdown("---")
st.markdown('<h2 class="header">About Me</h2>', unsafe_allow_html=True)

about_cols = st.columns(2)
with about_cols[0]:
    st.markdown("""
    ### Education
    **Alexandria National University**  
    B.Sc. in Computer and Data Science (Intelligent Systems)  
    *2022 - 2026 (Expected)*  
    CGPA: 3.16/4.0

    ### Technical Skills
    - **Languages**: Python, Java, PHP, JavaScript, HTML/CSS, SQL
    - **AI/ML**: Scikit-learn, TensorFlow, OpenCV, NLP, Genetic Algorithms
    - **Data Science**: Pandas, NumPy, Matplotlib, Seaborn
    - **Tools**: Git, Figma, Jupyter, Docker, Streamlit, VS Code
    """)

with about_cols[1]:
    st.markdown("""
    ### Professional Skills
    - Problem Solving & Algorithm Design
    - Full-Stack Development (Web & AI Apps)
    - Machine Learning & Deep Learning Pipelines
    - Feature Selection & Model Optimization
    - UI/UX Design and Prototyping
    - Technical Writing & Documentation

    ### Languages
    - English (Professional Proficiency)
    - French (Intermediate)
    """)

# Projects Section
st.markdown("---")
st.markdown('<h2 class="header">Featured Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "title": "Car Rental System",
        "description": "Full-stack web application for car rentals with admin dashboard",
        "tech": ["PHP", "MySQL", "JavaScript", "HTML/CSS"],
        "github": "https://github.com/ahmed9194/Car-rental_system",
        "category": "Web Development"
    },
    {
        "title": "Face Recognition System",
        "description": "Machine learning model for facial recognition using OpenCV",
        "tech": ["Python", "OpenCV", "Machine Learning"],
        "github": "https://github.com/ahmed9194/Face-Recognition",
        "category": "AI/ML"
    },
    {
        "title": "8-Puzzle Solver",
        "description": "AI solution using search algorithms (A*, BFS, DFS)",
        "tech": ["Python", "AI Algorithms"],
        "github": "https://github.com/ahmed9194/8-puzzle-game",
        "category": "AI/ML"
    },
    {
        "title": "Hybrid Movie Recommendation",
        "description": "Content + collaborative filtering recommendation system",
        "tech": ["Python", "Machine Learning", "Pandas"],
        "github": "https://github.com/ahmed9194/Hybrid-Movie-Recommendation-System",
        "category": "AI/ML"
    },
    {
        "title": "Device Store System",
        "description": "OOP-based PC store management system",
        "tech": ["OOP", "Java", "System Design"],
        "github": "https://github.com/ahmed9194/Device-Store",
        "category": "Software Engineering"
    },
    {
        "title": "Customer Churn Predictor",
        "description": "Streamlit app with Genetic Algorithm for feature selection & churn classification",
        "tech": ["Python", "GA", "ML", "Streamlit"],
        "github": "https://github.com/ahmed9194/Customer-Churn-Feature-Selection",
        "category": "AI/ML"
    },
    {
        "title": "Smart Tourism RAG Chatbot",
        "description": "Agentic chatbot using CrewAI, Qdrant, and Streamlit for tourism guidance",
        "tech": ["Python", "CrewAI", "RAG", "Streamlit"],
        "github": "https://github.com/ahmed9194/Tourism-RAG-Chatbot",
        "category": "AI/ML"
    }
]

# Project Filter
categories = ["All"] + sorted(set([p["category"] for p in projects]))
selected_category = st.selectbox("Filter by category", categories)

filtered_projects = projects if selected_category == "All" else [p for p in projects if p["category"] == selected_category]

for project in filtered_projects:
    with st.container():
        st.markdown(f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p>{project['description']}</p>
            <div>{' '.join([f"<span class='tech-badge'>{t}</span>" for t in project['tech']])}</div>
            <a href="{project['github']}" target="_blank" class="social-btn" style="margin-top: 1rem;">View on GitHub</a>
        </div>
        """, unsafe_allow_html=True)

# Contact Section
st.markdown("---")
st.markdown('<h2 class="header" id="contact">Contact Me</h2>', unsafe_allow_html=True)

contact_form = """
<form action="https://formsubmit.co/YOUR_EMAIL@example.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Hide Streamlit branding
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
