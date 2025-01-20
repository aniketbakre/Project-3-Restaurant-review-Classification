import streamlit as st
import base64

# Set page title
st.title("Restaurant Review Classification")

# Model download button
@st.cache_data
def get_model_file():
    # Need to correct model path when uploading
    with open("model/sentiment_model.pkl", "rb") as file:
        return file.read()

model_data = get_model_file()
b64_model = base64.b64encode(model_data).decode()
href = f'<a href="data:file/model;base64,{b64_model}" download="sentiment_model.pkl">Download Model</a>'
st.markdown(href, unsafe_allow_html=True)

# Input Window
user_input = st.text_input("Enter your input:")

# Submit Button
if st.button("Submit"):
    if user_input:
        # Replace this with your model inference logic
        output = f"Your model output for input '{user_input}'"
        # Output Window
        st.success(f"Output: {output}")
    else:
        st.error("Please enter an input to proceed.")
