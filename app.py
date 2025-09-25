
import streamlit as st
import re
import string
import joblib

# Load model + vectorizer
model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

# Streamlit UI
st.title("📧 Spam Email Classifier")
st.write("Type a message and find out if it's Spam or Not Spam.")

# User input
user_input = st.text_area("Enter your message:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message first.")
    else:
        cleaned = clean_text(user_input)
        tfidf_input = vectorizer.transform([cleaned])
        prediction = model.predict(tfidf_input)[0]

        if prediction == "Spam" or prediction == 1:
            st.error("🚨 This message is **Spam**!")
        else:
            st.success("✅ This message is **Not Spam**.")
