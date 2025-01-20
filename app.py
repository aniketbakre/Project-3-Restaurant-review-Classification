import streamlit as st
import joblib
import time

# Set page title
st.title("Restaurant Review Classification")


if 'model' not in st.session_state:
    try:
        with st.spinner('Hello! Please wait.. I am loading the model for you...'):
            time.sleep(4)
        # loading the model and vectorizer
        st.session_state.model = joblib.load(r"model\sentiment_model.pkl")
        st.session_state.vectorizer = joblib.load(r"model\vectorizer.pkl")
        st.session_state.model_loaded = True
        st.write("Model and vectorizer loaded successfully.")
    except Exception as e:
        st.session_state.model_loaded = False
        st.write(f"Error loading model or vectorizer: {e}")

else:
    if st.session_state.model_loaded:
        st.write("Model and vectorizer are already loaded.")
    else:
        st.write("There was an error loading the model and vectorizer.")

# input window for review
review = st.text_area("Enter your review here:")

# Button to submit the review
if st.button("Submit"):
    if review:
        if st.session_state.model_loaded:
            with st.spinner('Processing your review...'):
                time.sleep(2)
            # Transform the new review using loaded vectorizer
            review_transformer = st.session_state.vectorizer.transform([review])

            # Predict sentiment using loaded model
            prediction = st.session_state.model.predict(review_transformer)

            # Display the result
            sentiment = "Liked" if prediction[0] == 1 else "Not Liked"

            # Set color based on sentiment
            color = "blue" if sentiment == "Liked" else "red"

            # Display the result with conditional color
            st.subheader("Result:")
            st.markdown(f"This Person <span style='color:{color};'>{sentiment}</span> This Restaurant.", unsafe_allow_html=True)
        else:
            st.write("Please load the model and vectorizer first.")

    else:
        st.write("Please enter a review before submitting.")