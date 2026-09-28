import streamlit as st

st.title("File Upload App")
st.header("Streamlit Basic")
st.subheader("Build Simple web applications")

uploaded_file = st.file_uploader("Upload a file")
st.sidebar.title("Course Menu")

option = st.sidebar.selectbox(
    "Choose a topic",
    ["Home", "File Upload", "About"]
)

st.write("Selected:", option)


if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("File name:", uploaded_file.name)
    