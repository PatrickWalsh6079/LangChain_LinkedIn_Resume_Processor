import json
import os
from st_on_hover_tabs import on_hover_tabs
import streamlit as st
from tools.linkedin_scraper import create_json
from tools.llm_model import call_llm, interview_questions
from tools.load_json import embed_data


def main():
    st.set_page_config(layout="wide")

    st.header("Read LinkedIn Profiles")
    st.markdown('<style>' + open('./css/style.css').read() + '</style>', unsafe_allow_html=True)

    with st.sidebar:
        tabs = on_hover_tabs(tabName=['Add Profile', 'View Raw', 'View Profiles'],
                             iconName=['person', '{}', 'economy'], default_choice=0)

    if tabs == 'Add Profile':
        st.title("Add New Profile")
        profile = st.text_input('')
        add_profile = st.button('Add profile')

        if add_profile:
            with st.spinner('Adding LinkedIn profile...'):
                create_json(profile)
                name = profile.split('/')[-2]
                print(name)
                with st.spinner('Processing data...'):
                    embed_data()
                    # embed_data_for_all_profiles()
                    st.success('Profile successfully added!')

    elif tabs == 'View Raw':
        st.title("Raw JSON")

        # Define the folder path
        folder_path = './data/'

        # List files in the folder
        files = os.listdir(folder_path)

        if len(files) == 0:
            st.write("No files found in the folder.")
        else:
            st.write("Files in the folder:")
            for file in files:
                profile_button = st.button(file)
                if profile_button:
                    with open(f'./data/{file}', 'r') as json_file:
                        # Load the JSON data from the file
                        json_data = json.load(json_file)
                    st.json(json_data)

    elif tabs == 'View Profiles':
        st.title("Query Profile")
        # Define the folder path
        folder_path = './data/'

        # List files in the folder
        files = os.listdir(folder_path)

        if len(files) == 0:
            st.write("No files found in the folder.")
        else:
            st.write("Profiles in folder:")
            for file in files:
                st.write(file)
            chat = st.text_input('')
            submit = st.button('Submit')
            # sample_questions = st.button('Generate Interview Questions')

            if submit:
                with st.spinner('Loading...'):
                    response = call_llm(chat)
                    st.write(response)
            # elif sample_questions:
            #     with st.spinner('Generating interview questions...'):
            #
            #         response = interview_questions(profile_data)
            #
            #         # Display the generated questions
            #         st.write(response)


if __name__ == "__main__":
    main()
