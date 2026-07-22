import requests
import streamlit as st

st.title("📚 Document Library")

st.caption(
    "Browse all uploaded industrial documents."
)

response = requests.get(
    "http://127.0.0.1:8000/api/documents"
)

if response.status_code == 200:

    documents = response.json()

    if len(documents) == 0:

        st.info(
            "No documents have been uploaded yet."
        )

    else:

        st.success(
            f"{len(documents)} Documents Found"
        )

        st.divider()

        for doc in documents:

            with st.container():

                st.subheader(
                    "📄 " + doc["filename"]
                )

                c1, c2, c3 = st.columns(3)

                with c1:

                    st.metric(

                        "Pages",

                        doc["pages"]

                    )

                with c2:

                    st.metric(

                        "Department",

                        doc["department"]

                    )

                with c3:

                    st.metric(

                        "Equipment",

                        doc["equipment"]

                    )

                st.write(
                    "**Document Type:**",
                    doc["document_type"]
                )

                st.write(
                    "**Uploaded:**",
                    doc["uploaded_at"]
                )

                st.write(
                    "**AI Summary**"
                )

                st.info(
                    doc["summary"]
                )

                st.divider()

else:

    st.error(
        response.text
    )