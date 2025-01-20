import google.generativeai as genai
import streamlit as st

# Configure API Key
genai.configure(api_key='your-gemini-api-key')

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# Streamlit app
st.title("Conversational App with Gemini API")
st.write("This is a simple conversational app using the Gemini API and Streamlit.")

# User input
user_question = st.text_input("Enter your question:", placeholder="Type your question here")

# Generate the answer when button is clicked
if st.button("Generate Answer"):
    if user_question.strip():  # Ensure the question is not empty   
            # Get the response from Gemini API
            response = model.generate_content(user_question)
            
            # Debug: Print the response structure
            # st.write("Response Structure:")
            # st.write(response)
            answer = response.candidates[0].content.parts[0].text
            st.success("Answer:")
            st.write(answer)

            
