import os
import random
import string
import pinecone
import traceback
import streamlit as st
from dotenv import load_dotenv
from streamlit_chat import message
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader




def signUp():
    pass

def login():
    pass
    



def main():
    st.title('Welcome to StudyBuddy')

    # Adding a brief description
    st.write("The Onestop AI tool to help you power through your study. Kindly check the about page to ")

    st.write("Sign up to access all features if you do not have an account")

    
    st.write("Login to your account to continue ")


    st.sidebar.title("Option")

    selection = st.sidebar.radio("Go to", ["Sign up","Login"])
    if selection == "Sign up":
        signUp()
    elif selection == "Login":
        login()


if __name__ == "__main__":
    main()
