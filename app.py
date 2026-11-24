import re
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Mostafa Abdelkader | Data Engineer",
    page_icon="📊",
    layout="centered",
)

# ------------------------------------------------------------------
# Optional images: put these files next to app.py
#   photo.jpg        -> your portrait
#   fixora_logo.jpg  -> Fixora project logo
#   faculty.jpg      -> Faculty building photo
# ------------------------------------------------------------------
BASE = Path(__file__).parent
PHOTO = BASE / "photo.jpeg"
FIXORA = BASE / "fixora_logo.jpeg"
FACULTY = BASE / "faculty.jpeg"

ACCENT = "#2563eb"
ACCENT_LIGHT = "#60a5fa"

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp {{
    font-family: 'Manrope', system-ui, sans-serif;
}}

.block-container {{
    max-width: 960px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}}

.hero-wrap {{
    background: #0b1120;
    background-image: radial-gradient(rgba(96,165,250,.16) 1px, transparent 1px);
    background-size: 26px 26px;
    color: #f1f5f9;
    border: 1px solid rgba(96,165,250,.15);
    border-radius: 18px;
    padding: 40px 32px;
    margin-bottom: 8px;
    box-shadow: 0 10px 35px rgba(0,0,0,.18);
}}

.hero-wrap h1 {{
    font-size: clamp(34px, 5.5vw, 58px);
    font-weight: 800;
    letter-spacing: -.03em;
    line-height: 1.05;
    margin: 0 0 12px;
    color: #f1f5f9;
}}

.role {{
    color: {ACCENT_LIGHT};
    font-size: clamp(18px, 2.5vw, 22px);
    font-weight: 700;
    margin: 0 0 18px;
}}

.lead {{
    color: #c0ccdc;
    font-size: 17px;
    line-height: 1.7;
    max-width: 60ch;
    margin: 0 0 24px;
}}

.btn {{
    display: inline-block;
    padding: 11px 18px;
    border-radius: 8px;
    font-weight: 700;
    font-size: 14px;
    text-decoration: none !important;
    margin: 0 8px 10px 0;
    border: 1.5px solid rgba(255,255,255,.28);
    color: #f1f5f9 !important;
    transition: all .2s ease;
}}

.btn:hover {{
    border-color: {ACCENT_LIGHT};
    color: {ACCENT_LIGHT} !important;
}}

.btn.p {{
    background: {ACCENT_LIGHT};
    border-color: {ACCENT_LIGHT};
    color: #071426 !important;
}}

.btn.p:hover {{
    background: #3b82f6;
    border-color: #3b82f6;
}}

[data-testid="stImage"] img {{
    border-radius: 18px;
    border: 2px solid rgba(96,165,250,.22);
    object-fit: cover;
}}

.avatar {{
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background: {ACCENT_LIGHT};
    color: #071426;
    display: grid;
    place-items: center;
    font-weight: 800;
    font-size: 48px;
    margin: auto;
}}

.sec-title {{
    font-size: 14px;
    font-weight: 800;
    color: {ACCENT_LIGHT};
    letter-spacing: .08em;
    text-transform: uppercase;
    margin: 40px 0 16px;
    border-top: 1px solid rgba(128,140,160,.2);
    padding-top: 28px;
}}

.item h3, .proj h3 {{
    font-size: 20px;
    margin: 0 0 4px;
    font-weight: 700;
}}

.meta {{
    color: #94a3b8;
    font-size: 14px;
    margin: 0 0 8px;
}}

.tags {{
    color: {ACCENT_LIGHT};
    font-weight: 700;
    font-size: 14px;
    margin: 0 0 8px;
}}

.flow {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px 26px;
    margin: 12px 0 14px;
    padding: 0;
    list-style: none;
}}

.flow li {{
    position: relative;
    border: 1px solid rgba(128,140,160,.35);
    padding: 6px 12px;
    border-radius: 7px;
    font-size: 13px;
    font-weight: 700;
}}

.flow li:not(:last-child)::after {{
    content: "→";
    position: absolute;
    left: calc(100% + 5px);
    top: 50%;
    transform: translateY(-52%);
    color: {ACCENT_LIGHT};
    font-weight: 800;
}}

.flow li:last-child {{
    border-color: {ACCENT_LIGHT};
}}

.repo {{
    font-weight: 700;
    color: {ACCENT_LIGHT} !important;
    text-decoration: none !important;
}}

.card {{
    background: #151e30;
    border: 1px solid rgba(128,140,160,.2);
    border-radius: 14px;
    padding: 20px;
    height: 100%;
    transition: transform .2s ease, border-color .2s ease;
}}

.card:hover {{
    transform: translateY(-3px);
    border-color: rgba(96,165,250,.4);
}}

.card h3 {{
    font-size: 16px;
    margin: 0 0 12px;
}}

.chips {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin: 0;
    padding: 0;
    list-style: none;
}}

.chips li {{
    font-size: 12.5px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid rgba(128,140,160,.35);
}}

.svc dt {{
    font-weight: 700;
    margin-top: 12px;
}}

.svc dd {{
    margin: 0;
    color: #94a3b8;
    line-height: 1.6;
}}

/* Contact cards */
.contact-grid {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
    margin-top: 24px;
}}

.contact-card {{
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 20px;
    min-height: 100px;

    background: #151e30;
    border: 1px solid rgba(96,165,250,.15);
    border-radius: 14px;

    text-decoration: none !important;
    color: #f1f5f9 !important;

    transition: all .25s ease;
}}

.contact-card:hover {{
    transform: translateY(-4px);
    border-color: {ACCENT_LIGHT};
    background: #1a2740;
    box-shadow: 0 8px 24px rgba(37,99,235,.12);
}}

.contact-icon {{
    min-width: 48px;
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    background: rgba(96,165,250,.10);
    border: 1px solid rgba(96,165,250,.20);
    color: {ACCENT_LIGHT};
    font-size: 20px;
    font-weight: 800;
}}

.contact-info {{
    min-width: 0;
}}

.contact-title {{
    font-size: 14px;
    font-weight: 800;
    color: #f1f5f9;
    margin-bottom: 5px;
}}

.contact-value {{
    font-size: 13px;
    color: #94a3b8;
    overflow-wrap: anywhere;
    line-height: 1.5;
}}

.contact-arrow {{
    margin-left: auto;
    color: {ACCENT_LIGHT};
    font-size: 18px;
    opacity: 0;
    transition: opacity .2s ease;
}}

.contact-card:hover .contact-arrow {{
    opacity: 1;
}}

.footer {{
    text-align: center;
    color: #94a3b8;
    font-size: 14px;
    margin-top: 48px;
    border-top: 1px solid rgba(128,140,160,.2);
    padding-top: 20px;
}}

@media (max-width: 640px) {{
    .contact-grid {{
        grid-template-columns: 1fr;
    }}

    .hero-wrap {{
        padding: 30px 22px;
    }}
}}
</style>
""",
    unsafe_allow_html=True,
)


def html(s: str) -> None:
    """Render HTML without Markdown treating indented lines as code."""
    st.markdown(re.sub(r"\n\s*", "", s), unsafe_allow_html=True)


def section(title: str) -> None:
    html(f'<div class="sec-title">{title}</div>')


def flow(steps: list[str]) -> str:
    return '<ul class="flow">' + "".join(f"<li>{s}</li>" for s in steps) + "</ul>"


# ------------------------------------------------------------------
# Hero
# ------------------------------------------------------------------
left, right = st.columns([1.7, 1], vertical_alignment="center", gap="large")

with left:
    html(
        """
<div class="hero-wrap" style="margin:0">
<h1>Mostafa Abdelkader</h1>
<p class="role">Data Engineer and Data Scientist</p>
<p class="lead">I build reliable ETL/ELT pipelines and machine learning models that turn raw data
into information teams can trust. Data Science student at Alexandria University, graduating 2027.</p>
<a class="btn p" href="#contact">Get in touch</a>
<a class="btn" href="https://github.com/mostafaabdelkader1045" target="_blank">GitHub</a>
<a class="btn" href="https://www.linkedin.com/in/mostafa-abdelkader-ab3634407" target="_blank">LinkedIn</a>
</div>
"""
    )

with right:
    if PHOTO.exists():
        st.image(str(PHOTO), use_container_width=True)
    else:
        html('<div class="avatar">MA</div>')


# ------------------------------------------------------------------
# How I work with data
# ------------------------------------------------------------------
section("How I work with data")
html(flow(["Source", "Extract", "Transform", "Load", "Analyze and model"]))


# ------------------------------------------------------------------
# About
# ------------------------------------------------------------------
section("About")
st.write(
    "I am interested in the full journey of data: where it comes from, how it is cleaned "
    "and modeled, where it is stored, and how it supports decisions."
)
st.write(
    "My work began with Python, SQL and data analysis, and now covers pipeline "
    "orchestration, data warehousing and applied machine learning. I want to bridge "
    "data infrastructure and intelligent solutions."
)


# ------------------------------------------------------------------
# Experience
# ------------------------------------------------------------------
section("Experience")
html(
    """
<div class="item"><h3>Data Engineering Trainee</h3>
<p class="meta">Digital Egypt Pioneers Initiative (DEPI)</p></div>
"""
)
st.markdown(
    """
- Build ETL/ELT pipelines in Python and SQL to extract, transform and load data.
- Orchestrate workflows with Apache Airflow and implement transformations with dbt.
- Containerize data environments with Docker.
- Work with PostgreSQL, MySQL and SQLite, applying data warehousing, modeling, data lake and governance concepts.
"""
)

html(
    """
<div class="item" style="margin-top:24px"><h3>Machine Learning Intern</h3>
<p class="meta">Python, Scikit-learn</p></div>
"""
)
st.markdown(
    """
- Prepared real-world datasets through preprocessing, exploratory analysis and feature preparation.
- Implemented and evaluated KNN, SVM, PCA and LDA, tuning hyperparameters to improve performance.
- Presented results with Matplotlib visualizations.
"""
)


# ------------------------------------------------------------------
# Projects
# ------------------------------------------------------------------
section("Projects")

# Fixora
html('<div class="proj"><h3>Fixora</h3><p class="tags">Team project</p></div>')
if FIXORA.exists():
    st.image(str(FIXORA), caption="Fixora project logo", use_container_width=True)

st.write(
    "A team project built with fellow Data Science students. "
    "The repository has the code and documentation."
)
html(
    '<a class="repo" href="https://github.com/shvwkyyy/Fixora" target="_blank">'
    "View on GitHub →</a>"
)

st.divider()

# Football Scout
html(
    '<div class="proj"><h3>Football Scout Recommendation System</h3>'
    '<p class="tags">Python, Pandas, Scikit-learn</p></div>'
)
st.write(
    "A machine learning scouting tool that ranks midfield targets using age, "
    "market value and performance statistics."
)
html(flow(["Player data", "Feature prep", "Scikit-learn model", "Ranked targets"]))
html(
    '<a class="repo" target="_blank" '
    'href="https://github.com/mostafaabdelkader1045/Football_Scout_Recommendation_System">'
    "View on GitHub →</a>"
)

st.divider()

# GDP ETL
html(
    '<div class="proj"><h3>GDP Data ETL Pipeline</h3>'
    '<p class="tags">Python, Web Scraping, Pandas, SQLite</p></div>'
)
st.write("Extracts and processes GDP data from online sources into a queryable database.")
html(flow(["Web source", "Scrape", "Clean with Pandas", "SQLite"]))
html(
    '<a class="repo" target="_blank" '
    'href="https://github.com/mostafaabdelkader1045/GDP-ETL">View on GitHub →</a>'
)


# ------------------------------------------------------------------
# Skills
# ------------------------------------------------------------------
section("Skills")
skills = {
    "💻 Languages": ["Python", "SQL", "Java", "JavaScript"],
    "⚙️ Data engineering": ["ETL/ELT", "Apache Airflow", "dbt", "Docker", "Data warehousing"],
    "🗄️ Databases": ["PostgreSQL", "MySQL", "MongoDB", "SQLite", "DuckDB"],
    "📈 Analytics and ML": ["Pandas", "NumPy", "Scikit-learn", "Power BI", "Excel"],
    "🏛️ Architecture": ["Data modeling", "RDBMS", "Data lakes", "Lakehouse", "Data governance"],
}

items = list(skills.items())
for i in range(0, len(items), 2):
    cols = st.columns(2)
    for col, (title, chips) in zip(cols, items[i : i + 2]):
        with col:
            chips_html = "".join(f"<li>{c}</li>" for c in chips)
            html(
                f'<div class="card"><h3>{title}</h3>'
                f'<ul class="chips">{chips_html}</ul></div>'
            )
    st.write("")


# ------------------------------------------------------------------
# Education
# ------------------------------------------------------------------
section("Education")
html(
    """
<div class="item"><h3>B.Sc. in Data Science</h3>
<p class="meta">Alexandria University, Faculty of Computers and Data Science, 2023 to 2027</p></div>
"""
)
st.write("Focus: data engineering, machine learning, database systems, data analytics.")

if FACULTY.exists():
    st.image(
        str(FACULTY),
        caption="Faculty of Computers and Data Science, Alexandria University",
        use_container_width=True,
    )


# ------------------------------------------------------------------
# Services
# ------------------------------------------------------------------
section("Services")
html(
    """
<dl class="svc">
<dt>Data pipelines</dt><dd>ETL/ELT pipelines that collect, clean and prepare data for analysis.</dd>
<dt>Database design</dt><dd>Data modeling, normalization, SQL queries and optimization.</dd>
<dt>Data collection</dt><dd>Python web scraping that turns online sources into structured data.</dd>
<dt>Workflow automation</dt><dd>Scheduled, repeatable workflows with Airflow, dbt and Docker.</dd>
</dl>
"""
)


# ------------------------------------------------------------------
# Contact
# ------------------------------------------------------------------
html('<div id="contact"></div>')
section("Contact")

st.write(
    "I'm open to internships, junior roles and data projects. "
    "Feel free to reach out — let's connect."
)

html(
    """
<div class="contact-grid">

<a class="contact-card" href="mailto:mostafaabdelkader1045@gmail.com">
    <div class="contact-icon">✉</div>
    <div class="contact-info">
        <div class="contact-title">Email</div>
        <div class="contact-value">Send me an email</div>
    </div>
    <div class="contact-arrow">↗</div>
</a>

<a class="contact-card"
   href="https://www.linkedin.com/in/mostafa-abdelkader-ab3634407"
   target="_blank" rel="noopener noreferrer">
    <div class="contact-icon">in</div>
    <div class="contact-info">
        <div class="contact-title">LinkedIn</div>
        <div class="contact-value">Let's connect professionally</div>
    </div>
    <div class="contact-arrow">↗</div>
</a>

<a class="contact-card"
   href="https://github.com/mostafaabdelkader1045"
   target="_blank" rel="noopener noreferrer">
    <div class="contact-icon">⌘</div>
    <div class="contact-info">
        <div class="contact-title">GitHub</div>
        <div class="contact-value">Explore my projects</div>
    </div>
    <div class="contact-arrow">↗</div>
</a>

<a class="contact-card"
   href="https://wa.me/201270942272"
   target="_blank" rel="noopener noreferrer">
    <div class="contact-icon">◉</div>
    <div class="contact-info">
        <div class="contact-title">WhatsApp</div>
        <div class="contact-value">Send me a message</div>
    </div>
    <div class="contact-arrow">↗</div>
</a>

</div>
"""
)

html('<div class="footer">Mostafa Abdelkader · Alexandria, Egypt</div>')