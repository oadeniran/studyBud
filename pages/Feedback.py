import streamlit as st

st.title('StudyBuddy Feedback and Reviews😎😎')

if 'loggedIn' in st.session_state:
        st.write("✨✨Thanks for trying out studdy buddy. Kindly drop your reviews and feedbacks✨✨")

        st.write("We expect feedback on things you found off or things you would like to be implemented")

        feedback = st.text_area("Your Feedback", height=50)

        submit_button = st.button("!Submit!")

        if submit_button:
            if len(feedback) > 5:
                print("Here")
            else:
                st.error("You must provide a feedback")

else:
    st.write("Please login to give reviews")
