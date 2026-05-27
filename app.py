import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to get Gemini response
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(question)

    return response.text

# Streamlit App
st.set_page_config(page_title="Gemini LLM APP")

st.header("Gemini AI BOT Application")

user_input = st.text_input("Input:", key="input")

submit = st.button("Click Me To Generate Response")

if submit:
    if user_input:
        response = get_gemini_response(user_input)

        st.subheader("The Response is")

        st.write(response)
    else:
        st.warning("Please enter a prompt.")
