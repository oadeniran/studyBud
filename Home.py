import os
import random
import streamlit as st
from dotenv import load_dotenv
from streamlit_chat import message
import requests
import json

load_dotenv()
base_url = os.getenv("BaseUrl")

def signUp():
    st.title("Sign Up")
	
    with st.form("signup",clear_on_submit=False):
        username = st.text_input("Username (lowercase)")
        password = st.text_input("Password", type="password")
        level = st.selectbox("What is your level", ["College", "Highschool"])
        signUp_button = st.form_submit_button('Sign Up')

    required_fields = [
        (username, "Username field is required."),
        (password, "Password field is required."),
    ]
	
    if signUp_button:
        errors = [error_msg for field, error_msg in required_fields if not field]
        if errors:
            for error in errors:
                st.error(error)
        else:
            payload = {
                "username" : username.lower(),
                "password" : password,
                "level" : level
            }
            url = f"{base_url}/signup"
            result = requests.post(
                url,
                data =payload,
            )
            contents_of_results = result.content
            contents_of_results = json.loads(contents_of_results.decode('utf-8'))
            if contents_of_results['status_code'] == 200:
                st.success(contents_of_results['message'])
                st.info("Now proceed to sign in")
            else:
                st.error(contents_of_results['message'])

def login():
    st.title("Login")

    with st.form("login",clear_on_submit=True):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button('login')

    required_fields = [
    (username, "Username field is required."),
    (password, "Password field is required."),
    ]
    if login_button:
        errors = [error_msg for field, error_msg in required_fields if not field]
        if errors:
            for error in errors:
                st.error(error)
        else:
            payload = {
                "username" : username.lower(),
                "password" : password
            }
            url = f"{base_url}/login"
            result = requests.post(
                url,
                data=payload,
            )
            contents_of_results = result.content
            contents_of_results = json.loads(contents_of_results.decode('utf-8'))
            if contents_of_results['status_code'] == 200:
                st.success(contents_of_results['message'])
                st.session_state['loggedIn'] = {"uid" : contents_of_results["uid"]}
                st.info("...Successfully signed in. You can use all features now...")
            else:
                st.error(contents_of_results['message'])


def main():
    if 'loggedIn' in st.session_state:
        st.write("The Onestop AI tool to help you power through your study. Kindly check the about page to ")

        st.write("You are logged in, proceed to use all our wonderful features")
    else:
        st.title('Welcome to StudyBuddy😎😎')

        # Adding a brief description
        st.write("""Being your StudyBuddy, my Job is to help you power through your study with ease. Kindly Signup to access all features if you do not have an account. If you have an account already, please Login to proceed.""")

        st.sidebar.title("Option")

        selection = st.sidebar.radio("Go to", ["Sign up","Login"])
        if selection == "Sign up":
            signUp()
        elif selection == "Login":
            login()


if __name__ == "__main__":
    main()
