import streamlit as st

def run_cat_selection(selection):
    pass

def add_new_ctegory():
    with st.form("Details",clear_on_submit=True):
        category_name = st.text_input("Name")
        category_details = st.text_input("Description", type="password")
        submit_button = st.form_submit_button('CREATE')

        if submit_button:
            if not category_name:
                st.error("Name field is required")
            else:
                categories.append(category_name)


if 'loggedIn' not in st.session_state:
    st.error("Please Login to Use feature")
else:
    categories = ["Add New category"]

    st.sidebar.title("Navigation")
    if "categories" not in st.session_state:
        st.session_state['categories'] = categories
        selection = st.sidebar.radio("Go to", categories)
    else:
        selection = st.sidebar.radio("Go to", st.session_state['categories'])