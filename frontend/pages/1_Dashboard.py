import requests
import streamlit as st

st.title("📊 IndustrialBrain Dashboard")

st.caption(
    "Real-time overview of your IndustrialBrain AI platform."
)

response = requests.get(
    "http://127.0.0.1:8000/api/analytics"
)

if response.status_code == 200:

    data = response.json()

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(

            "📄 Documents",

            data["total_documents"]

        )

    with c2:

        st.metric(

            "📚 Total Pages",

            data["total_pages"]

        )

    with c3:

        st.metric(

            "🤖 AI Status",

            "Online"

        )

    with c4:

        st.metric(

            "⚡ Backend",

            "Running"

        )

    st.divider()

    left, right = st.columns([2,1])

    with left:

        st.subheader("📈 Platform Overview")

        st.info(
            f"""
### IndustrialBrain AI

Your AI platform currently contains **{data['total_documents']} documents**
with a total of **{data['total_pages']} pages**.

Upload more manuals, SOPs and industrial reports to improve
the quality of AI responses.
"""
        )

    with right:

        st.subheader("⚙ System Status")

        st.success("✅ FastAPI Server")

        st.success("✅ ChromaDB")

        st.success("✅ Embedding Model")

        st.success("✅ AI Assistant")

    st.divider()

    st.subheader("🚀 Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.button("📤 Upload Document")

    with c2:

        st.button("🤖 Ask AI")

    with c3:

        st.button("📚 View Library")

else:

    st.error(response.text)