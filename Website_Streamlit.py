import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

# Set Streamlit page config
st.set_page_config(page_title="Salman Ranjha", layout="wide")

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

coding_lottie = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_pprxh53t.json")

# Sidebar
with st.sidebar:
    st.image("profile.jpg", width=180)  # 👈 Put your image in the same folder as this script
    st.title("Salman Ranjha")
    st.caption("Tech + Data + Strategy")
    selected = option_menu("Menu", ["About", "Experience", "Projects", "Skills", "Contact"],
                           icons=["person", "briefcase", "code-slash", "gear", "envelope"],
                           menu_icon="cast", default_index=0)

# -------------------- About --------------------
if selected == "About":
    col1, col2 = st.columns(2)

    with col1:
        st.image("profile.jpg", width=250, caption="Salman Ranjha")  # 👈 Local image

    with col2:
        st.header("Hi, I'm Salman 👋")
        st.write("""
        A multidisciplinary professional blending economics, computer science, and data analytics.
        I love building things at the intersection of tech and business, and mentoring others along the way.
        """)
        st.markdown("📍 Based in St. Gallen, Switzerland")
        st.markdown("📧 [Email Me](mailto:salman.ranjha@outlook.com)")

    st.subheader("Education")
    with st.expander("🎓 Universität St. Gallen - Master's in Computer Science (2024 - Present)"):
        st.write("Coursework: ML/DL, NLP, Databases, Cyber Security, Marketing Analytics")

    with st.expander("🎓 Bocconi University - Bachelor’s in Econ + CS (2018 - 2021)"):
        st.write("Research Thesis on Formula 1 brand & Twitter engagement")

# -------------------- Experience --------------------
elif selected == "Experience":
    st.header("Professional Experience")

    with st.container():
        st.subheader("Teaching Assistant - Universität St. Gallen")
        st.caption("Feb 2025 – Present")
        st.markdown("- Guided students in Python, ML, and Streamlit")
        st.markdown("- Led project teams and evaluated code quality")

    with st.container():
        st.subheader("Technical Business Analyst - FBK S.r.l.")
        st.caption("Apr 2022 – Oct 2024")
        st.markdown("- Delivered SaaS projects for Johnson & Johnson")
        st.markdown("- Created dashboards, integrated APIs, automated reports")

    with st.container():
        st.subheader("Data Analyst - Curetech Solutions")
        st.caption("June 2021 – Mar 2022")
        st.markdown("- Built data pipelines and structured metadata")

    with st.container():
        st.subheader("Research Assistant - Zeds Astronomical Observatory")
        st.caption("2015 – 2018")
        st.markdown("- Analyzed celestial objects and contributed to AAVSO database")

# -------------------- Projects --------------------
elif selected == "Projects":
    st.header("Projects & Research")
    with st.expander("📊 Formula 1 Brand Analysis (Bocconi Thesis)"):
        st.write("""
        Analyzed historical Twitter data using NLP and econometrics to assess its impact on F1 brand growth.
        Tools: Python, StatsModels, Tweepy
        """)
    st.info("More project cards will go here – ML apps, dashboards, etc.")

# -------------------- Skills --------------------
elif selected == "Skills":
    st.header("Tech Stack & Languages")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🧠 Programming")
        st.code("Python (ML, NLP, DL), VBA, APIs")
        st.subheader("🗄️ Databases")
        st.code("SQL (Oracle, Exasol, MySQL), MongoDB, Neo4j")

    with col2:
        st.subheader("📊 Tools")
        st.code("Tableau, PowerBI, Postman")
        st.subheader("🌐 Languages")
        st.write("🇬🇧 English (Native)")
        st.write("🇮🇹 Italian (Intermediate)")
        st.write("🇩🇪 German (Beginner)")
        st.write("🇹🇷 Turkish (Conversational)")

# -------------------- Contact --------------------
elif selected == "Contact":
    st.header("Get in Touch")
    st.write("I'm always open to collaborating, mentoring, or discussing ideas over coffee ☕.")

    contact_form = """
    <form action="https://formsubmit.co/salman.ranjha@outlook.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Write your message here..." required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    st.write("---")
    st.markdown("📫 Or email me directly at [salman.ranjha@outlook.com](mailto:salman.ranjha@outlook.com)")
