import streamlit as st
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

base_url = os.getenv("BaseUrl")

categories = ["Add New category"]

def run_cat_selection(selection):
    ind = st.session_state["categories"].index(selection)
    st.title(selection)
    st.subheader(st.session_state["category_det"][ind-1])


def add_new_ctegory(categories):
    with st.form("Details",clear_on_submit=True):
        category_name = st.text_input("Name")
        category_details = st.text_input("Description")
        submit_button = st.form_submit_button('CREATE')

        if submit_button:
            if not category_name:
                st.error("Name field is required")
            else:
                if not category_details:
                    category_details = ""
                categories.append(category_name)
                st.session_state['categories'].append(category_name)
                st.session_state["category_det"].append(category_details)
                payload = json.dumps({
                    "uid": st.session_state["loggedIn"]["uid"],
                    "categories" : st.session_state["categories"],
                    "category_det": st.session_state["category_det"]
                })
                url = f"{base_url}/update-user-categories"
                result = requests.post(
                    url,
                    headers={'Content-Type': 'application/json'},
                    data=payload,
                )
                st.success("Category created", icon="👌")

if 'loggedIn' not in st.session_state:
    st.error("Please Login to Use feature......Return Home to login")
else:
    st.sidebar.title("Navigation")
    if "categories" not in st.session_state:
        st.session_state['categories'] = categories
        st.session_state["category_det"] = []

    selection = st.sidebar.radio("Go to", st.session_state['categories'])
    if selection == "Add New category":
        add_new_ctegory(categories)
    else:
        run_cat_selection(selection)