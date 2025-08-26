# app.py
import streamlit as st
import plotly.graph_objects as go
from datetime import date

# -------------- PAGE CONFIG --------------
st.set_page_config(
    page_title="Arish Mahammad • Portfolio",
    page_icon="🛠️",
    layout="wide"
)

# -------------- SESSION / THEME TOGGLE --------------
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"
if "display_mode" not in st.session_state:
    st.session_state.display_mode = "Showcase"

def set_theme(mode: str):
    st.session_state.theme = mode

def set_display_mode(mode: str):
    st.session_state.display_mode = mode

# -------------- GLOBAL STYLES (light/dark) --------------
light_css = """
<style>
:root {
  --bg: #ffffff;
  --card: #f7f7f9;
  --text: #161616;
  --muted: #5b5b5b;
  --accent: #3b82f6;
  --badge: #e9efff;
}
</style>
"""
dark_css = """
<style>
:root {
  --bg: #0b0d10;
  --card: #12151a;
  --text: #eaeef6;
  --muted: #a2a8b3;
  --accent: #60a5fa;
  --badge: #1e2738;
}
</style>
"""
base_css = """
<style>
html, body, [class*="css"]  {
  background: var(--bg) !important;
  color: var(--text) !important;
}
h1,h2,h3,h4 { letter-spacing: .3px; }
.block-container { padding-top: 2rem; }
.card {
  background: var(--card);
  border: 1px solid rgba(128,128,128,0.15);
  border-radius: 18px;
  padding: 20px;
}
.badge {
  display:inline-block;
  padding:6px 10px;
  border-radius: 999px;
  background: var(--badge);
  color: var(--text);
  font-size: 0.85rem;
  margin: 4px 6px 0 0;
  border: 1px solid rgba(128,128,128,0.15);
}
.small { color: var(--muted); font-size: 0.9rem; }
.hr { height:1px; background: rgba(128,128,128,0.2); margin: 10px 0 16px 0; }
.link a { text-decoration: none; }
.kpi {
  text-align:center;
  padding:14px;
  border-radius:16px;
  background: var(--card);
  border: 1px solid rgba(128,128,128,0.15);
}
.kpi h2 { margin:0; }
input, textarea { color: var(--text) !important; }
</style>
"""
st.markdown(dark_css if st.session_state.theme == "Dark" else light_css, unsafe_allow_html=True)
st.markdown(base_css, unsafe_allow_html=True)

# -------------- SIDEBAR --------------
with st.sidebar:
    st.title("👋 Arish Mahammad")
    st.caption("Aspiring ML/AI/Data Engineer • B.Tech CSE (Data Science)")
    st.radio("Theme", ["Dark", "Light"], index=0 if st.session_state.theme=="Dark" else 1, on_change=lambda: set_theme("Dark" if st.session_state.theme=="Light" else "Light"), key="theme_radio")
    st.selectbox("Display Mode", ["Showcase", "Minimal"], index=0 if st.session_state.display_mode=="Showcase" else 1, on_change=lambda: set_display_mode(st.session_state.display_mode), key="display_select")
    st.divider()
    page = st.radio("Navigate", ["🏠 Home", "🙋 About Me", "🛠️ Skills", "📂 Projects", "📜 Certifications", "📬 Contact"])

# -------------- HOME --------------
if page == "🏠 Home":
    left, right = st.columns([1.2, 1])
    with left:
        st.markdown("## 🚀 Building data-driven products")
        st.write(
            "I’m **Arish Mahammad**, an enthusiastic ML practitioner focused on **Supervised/Unsupervised Learning** "
            "and **NLP**. I love turning raw data into clear insights and reliable models."
        )
        st.write(
            "Comfortable with **Python** (NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Plotly, Cufflinks), "
            "**Streamlit**, **C++**, and **SQL**. I’m also **learning Web Development** to ship full-stack ML apps."
        )
        st.markdown(
            '<div class="small">Based in Kolkata • Open to internships, projects, and collaboration</div>',
            unsafe_allow_html=True
        )
        st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

        # KPIs
        k1, k2, k3 = st.columns(3)
        with k1:
            st.markdown('<div class="kpi"><div class="small">Certifications</div><h2>3</h2></div>', unsafe_allow_html=True)
        with k2:
            st.markdown('<div class="kpi"><div class="small">Core Skills</div><h2>9+</h2></div>', unsafe_allow_html=True)
        with k3:
            st.markdown(f'<div class="kpi"><div class="small">Active Since</div><h2>{date.today().year}</h2></div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Quick Links")
        st.subheader("🔗 Direct Links")
        st.write("📧 Email: [arishmahammad8@gmail.com](mailto:arishmahammad8@gmail.com)")
        st.write("💼 LinkedIn: [linkedin.com/in/arish-mahammad](https://www.linkedin.com/in/arish-m-227002242)")
        st.write("🐙 GitHub: [github.com/arishmahammad](https://github.com/arishmahammad)")
        st.write("✖️ X (Twitter): [x.com/ArishMahammad1](https://x.com/ArishMahammad1?t=WAcgBhBFwvP3dqL-Kv6alw&s=09)")
        st.write("📸 Instagram: [instagram.com/arishmahammad02](https://www.instagram.com/arishmahammad02?igsh=OHljY2FqNWlzMmox)")
        st.markdown('</div>', unsafe_allow_html=True)

# -------------- ABOUT ME (Tell Myself) --------------
elif page == "🙋 About Me":
    st.markdown("## 🙋 About Me")
    st.markdown(
        """
        I’m a second-year **B.Tech CSE (Data Science)** student who enjoys **learning by building**.
        My current focus is on:  
        - 📈 **Supervised/Unsupervised Learning** (solid on data preprocessing, feature engineering, model selection)  
        - 🗣️ **NLP** (text cleaning, vectorization, classical NLP, moving into transformer tooling)  
        - 🧰 **Deploying ML** with **Streamlit** for fast, interactive demos  
        """
    )

    a1, a2 = st.columns(2)
    with a1:
        st.markdown("### 💡 Strengths")
        st.markdown(
            """
            - Turning vague problems into clean datasets and baselines  
            - Clear plots & dashboards to explain results  
            - Bias/variance intuition and practical evaluation  
            """
        )
    with a2:
        st.markdown("### 🧭 Values")
        st.markdown(
            """
            - Learn fast, share simply  
            - Ship small, iterate weekly  
            - Communicate honestly with data  
            """
        )

    st.markdown("### 🎯 Goals (Near-Term)")
    st.markdown(
        """
        - Build 3–4 **end-to-end ML apps** (classification, clustering, NLP)  
        - Publish a clean **portfolio repo**  
        - Apply for **internships / freelance** data projects  
        """
    )

    st.markdown("### 🎮 Outside Work")
    st.markdown("- 🎯 Interests: Quantum Computing, AI, NLP, Cloud for Data Engineering.")

# -------------- SKILLS --------------
elif page == "🛠️ Skills":
    st.markdown("## 🛠️ Skills")

    # Skill Badges
    st.markdown("#### Core")
    core = ["Python", "NumPy", "Pandas", "Matplotlib", "Seaborn", "Scikit-learn", "Plotly", "Cufflinks", "Streamlit", "SQL", "C++"]
    st.markdown("".join([f'<span class="badge">{s}</span>' for s in core]), unsafe_allow_html=True)

    st.markdown("#### Domains")
    dom = ["Supervised Learning", "Unsupervised Learning", "NLP", "Data Cleaning", "Feature Engineering", "Visualization"]
    st.markdown("".join([f'<span class="badge">{s}</span>' for s in dom]), unsafe_allow_html=True)

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

    # Radar Chart (Plotly)
    st.markdown("#### Proficiency Radar (self-assessed)")
    labels = ["Python", "Data Wrangling", "ML (Classical)", "NLP", "Visualization", "SQL", "C++", "Deployment"]
    vals =  [8.5, 8.0, 8.0, 7.5, 8.0, 7.0, 6.5, 7.5]  # 0–10
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=vals + [vals[0]], theta=labels + [labels[0]], fill='toself', name="Skill"))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,10])), showlegend=False, margin=dict(l=0,r=0,t=20,b=0))
    st.plotly_chart(fig, use_container_width=True)

# -------------- PROJECTS --------------
elif page == "📂 Projects":
    st.markdown("## 📂 Projects")
    st.caption("Filter by type or keyword to explore quickly.")

    # Project data (edit these)
    projects = [
        {
            "title": "Student Report Card System",
            "desc": "GUI app with Tkinter to manage student records and generate report cards.",
            "tags": ["Python", "Tkinter", "CRUD", "Education"],
            "url": "https://github.com/your-handle/report-card"
        },
        {
            "title": "NLP Clean & Classify",
            "desc": "Text preprocessing + traditional ML classifiers for sentiment/topic.",
            "tags": ["Python", "NLP", "Scikit-learn", "Streamlit"],
            "url": "https://github.com/your-handle/nlp-clean-classify"
        },
        {
            "title": "Clustering Customer Segments",
            "desc": "EDA + KMeans/GMM for actionable customer segments with visuals.",
            "tags": ["Unsupervised", "EDA", "Plotly", "Pandas"],
            "url": "https://github.com/your-handle/customer-clusters"
        },
        {
            "title": "VirtuAI (YouTube)",
            "desc": "Faceless channel showcasing AI tools and modern lifestyle hacks.",
            "tags": ["Content", "YouTube", "AI Tools"],
            "url": "https://youtube.com/@your-handle"
        },
    ]

    all_tags = sorted({t for p in projects for t in p["tags"]})
    c1, c2 = st.columns([2, 3])
    with c1:
        picked = st.multiselect("Filter by tags", all_tags, default=[])
    with c2:
        q = st.text_input("Search title/description")

    def show_project(p):
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader(p["title"])
            st.write(p["desc"])
            st.markdown("".join([f'<span class="badge">{t}</span>' for t in p["tags"]]), unsafe_allow_html=True)
            st.markdown(f'**Repo/Demo:** {p["url"]}')
            st.markdown('</div>', unsafe_allow_html=True)

    shown = 0
    for p in projects:
        if picked and not any(t in picked for t in p["tags"]):
            continue
        if q and (q.lower() not in p["title"].lower() and q.lower() not in p["desc"].lower()):
            continue
        show_project(p); shown += 1

    if shown == 0:
        st.info("No projects match your current filter. Try clearing filters.")

# -------------- CERTIFICATIONS --------------
elif page == "📜 Certifications":
    st.markdown("## 📜 Certifications")
    st.write("Verified Coursera credentials:")

    certs = [
        {
            "name": "Data Analysis with Python — IBM",
            "verify": "https://coursera.org/verify/2PJPSC7CWWAQ",
            "local_pdf": "Coursera Data Analysis with Python.pdf"
        },
        {
            "name": "Machine Learning with Python — IBM",
            "verify": "https://coursera.org/verify/LW2SUKM58V77",
            "local_pdf": "Coursera Machine Learning with Python Certificate.pdf"
        },
        {
            "name": "Mathematical Biostatistics Boot Camp 1 — Johns Hopkins University",
            "verify": "https://coursera.org/verify/9N60SY77ONNG",
            "local_pdf": "Coursera Statistic with Data Science 1.pdf"
        },
    ]

    cols = st.columns(3)
    for i, c in enumerate(certs):
        with cols[i % 3]:
            st.markdown(f"**{c['name']}**")
            st.markdown(f"🔗 Verify: {c['verify']}")
            # If the PDF exists in the same folder, offer download
            try:
                with open(c["local_pdf"], "rb") as f:
                    st.download_button("Download PDF", f, file_name=c["local_pdf"])
            except Exception:
                st.caption("Place the PDF next to app.py to enable download.")

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
    st.caption("Tip: You can also host your PDFs in a public repo and link them here.")

# -------------- CONTACT --------------
elif page == "📬 Contact":
    st.markdown("## 📬 Contact")
    st.write("Reach out for collaboration, internships, and projects.")

    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Name")
            email = st.text_input("Email")
        with c2:
            subject = st.text_input("Subject")
            purpose = st.selectbox("Purpose", ["Project", "Internship", "Collab", "Other"])
        message = st.text_area("Message", height=140)
        submitted = st.form_submit_button("Send")
        if submitted:
            if not name or not email or not message:
                st.error("Please fill Name, Email, and Message.")
            else:
                st.success("Thanks! Copy the summary below and email it to me.")
                st.code(
                    f"To: your_email@example.com\n"
                    f"Subject: {subject or 'Inquiry'} ({purpose})\n"
                    f"From: {name} <{email}>\n\n{message}"
                )

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
    st.markdown("### 📄 Resume")
    st.caption("Drop your latest resume as PDF in this folder and rename to `Arish_Resume.pdf`.")
    try:
        with open("Arish_Resume.pdf", "rb") as f:
            st.download_button("Download Resume", f, file_name="Arish_Resume.pdf")
    except Exception:
        st.info("Resume not found. Add `Arish_Resume.pdf` next to `app.py`.")

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
    st.markdown("### 🤖 Ask Me Anything (quick Q&A)")
    user_q = st.text_input("Ask about my skills, tools, interests...")
    if user_q:
        ql = user_q.lower()
        if "nlp" in ql:
            st.write("I work with text cleaning, tokenization, TF-IDF, classical models, and I’m exploring transformer tooling.")
        elif "deploy" in ql or "streamlit" in ql:
            st.write("I ship fast demos with Streamlit, focusing on clean UI, clear metrics, and simple UX.")
        elif "skills" in ql or "stack" in ql:
            st.write("Python (NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Plotly, Cufflinks), Streamlit, SQL, C++.")
        else:
            st.write("I’m glad you asked! If you don’t see it above, I’m probably learning it next 😄")

# -------------- DISPLAY MODE TWEAKS --------------
if st.session_state.display_mode == "Minimal":
    st.markdown(
        """
        <style>
        h1,h2,h3 { font-weight: 600 !important; }
        .stSidebar, .badge { opacity: 0.92; }
        .card { padding: 16px; }
        </style>
        """,
        unsafe_allow_html=True
    )