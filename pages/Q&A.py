import streamlit as st


if 'qabot' not in st.session_state:
        st.error("Please Upload a PDF File")
else:
    st.sidebar.title("Options")
    selection = int(st.sidebar.slider( "Select Model Confidence", 25, 100, 25))
    