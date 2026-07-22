import requests
import streamlit as st

st.title("📤 Upload Industrial Document")

st.caption(
    "Upload PDF manuals, SOPs, reports, maintenance guides or industrial documentation."
)

uploaded_file = st.file_uploader(

    "Drag & Drop your PDF here",

    type=["pdf"]

)

if uploaded_file is not None:

    c1, c2 = st.columns(2)

    with c1:

        st.info(

            f"""
**Filename**

{uploaded_file.name}
"""
        )

    with c2:

        st.info(

            f"""
**Size**

{round(uploaded_file.size/1024,2)} KB
"""
        )

    st.divider()

    if st.button("🚀 Upload Document"):

        with st.spinner("Analyzing document with AI..."):

            files = {

                "file": (

                    uploaded_file.name,

                    uploaded_file.getvalue(),

                    "application/pdf"

                )

            }

            response = requests.post(

                "http://127.0.0.1:8000/api/upload",

                files=files

            )

        if response.status_code == 200:

            data = response.json()

            st.success("✅ Document uploaded successfully!")

            st.divider()

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(

                    "📄 Pages",

                    data["result"]["metadata"]["pages"]

                )

            with c2:

                st.metric(

                    "📚 Chunks",

                    data["result"]["chunks"]

                )

            with c3:

                st.metric(

                    "📖 Words",

                    data["result"]["metadata"]["words"]

                )

            st.divider()

            st.subheader("🤖 AI Summary")

            st.info(

                data["result"]["summary"]

            )

            st.subheader("🏷 Classification")

            st.success(

                data["result"]["classification"]

            )

            st.subheader("📊 Metadata")

            st.json(

                data["result"]["metadata"]

            )

        else:

            st.error(

                response.text

            )