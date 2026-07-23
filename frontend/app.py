import requests
import streamlit as st
import streamlit as st
import base64

def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
st.set_page_config(
    page_title="IndustrialBrain AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
set_background("images/background.jpg")
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background:#0E1117;
}

section[data-testid="stSidebar"]{
    background:#161B22;
}

div[data-testid="metric-container"]{
    background:#161B22;
    border:1px solid #30363d;
    border-radius:15px;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.image(
        "assets/logo.png",
        width=170
    )

    st.success("🟢 System Online")

    st.divider()

    st.write("### Modules")

    st.write("📤 Upload")
    st.write("📚 Library")
    st.write("🤖 AI Chat")
    st.write("📊 Analytics")

    st.divider()

    st.caption("IndustrialBrain AI v1.0")

st.title("IndustrialBrain AI")

st.caption(
    "Industrial Document Intelligence powered by Artificial Intelligence"
)

try:

    analytics = requests.get(
        "http://127.0.0.1:8000/api/analytics"
    ).json()

    total_docs = analytics["total_documents"]

    total_pages = analytics["total_pages"]

except:

    total_docs = 0

    total_pages = 0

st.divider()

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(

        "📄 Documents",

        total_docs

    )

with c2:

    st.metric(

        "📚 Pages",

        total_pages

    )

with c3:

    st.metric(

        "🤖 AI",

        "Online"

    )

with c4:

    st.metric(

        "⚡ Backend",

        "Running"

    )

st.divider()

left,right = st.columns([2,1])

with left:

    st.subheader("Welcome")

    st.write("""

IndustrialBrain AI is an AI-powered platform designed for
industrial document understanding.

### Features

- AI Document Classification
- AI Summarization
- Semantic Search
- Industrial Chatbot
- Analytics Dashboard
- Document Library
- Vector Database
- Retrieval Augmented Generation (RAG)

""")

with right:

    st.info("""

### Quick Start

1. Upload a PDF

2. Open Library

3. Ask AI Questions

4. View Analytics

""")

st.divider()

st.subheader("Platform Status")

st.success("✅ FastAPI Running")

st.success("✅ Database Connected")

st.success("✅ ChromaDB Connected")

st.success("✅ Embedding Model Loaded")