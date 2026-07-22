import requests
import streamlit as st

st.title("🤖 IndustrialBrain AI Assistant")

st.caption(
    "Ask questions about your uploaded industrial documents."
)

try:

    documents = requests.get(
        "http://127.0.0.1:8000/api/documents"
    ).json()

except:

    documents = []

if len(documents) == 0:

    st.warning(
        "No uploaded documents found."
    )

    st.stop()

st.divider()

selected = st.selectbox(

    "📄 Select Document",

    documents,

    format_func=lambda x: x["filename"]

)

st.info(

    f"Currently chatting with: **{selected['filename']}**"

)

question = st.text_area(

    "💬 Your Question",

    height=140,

    placeholder="Example: Summarize this document or explain the maintenance procedure."

)

if st.button("🚀 Ask AI"):

    if question.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "🤖 AI is thinking..."
        ):

            response = requests.post(

                "http://127.0.0.1:8000/api/chat",

                json={

                    "question": question,

                    "document_id": selected["id"]

                }

            )

        if response.status_code == 200:

            data = response.json()

            st.divider()

            st.subheader("🤖 AI Response")

            st.success(
                data["answer"]
            )

            c1, c2 = st.columns([1,2])

            with c1:

                st.metric(

                    "Confidence",

                    f"{data['confidence']} %"

                )

            with c2:

                st.progress(
                    min(
                        int(data["confidence"]),
                        100
                    )
                )

            if data["citations"]:

                st.subheader("📚 Sources")

                for item in data["citations"]:

                    st.info(item)

        else:

            st.error(
                response.text
            )