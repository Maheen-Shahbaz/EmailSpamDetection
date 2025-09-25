# Spam Email Detection App

This project is a **Spam Email Detection** application built using **Python**, **Scikit-learn**, and **Streamlit**. The app allows users to enter email text and predicts whether it is **Spam** or **Not Spam**.

## Features
- User-friendly **Streamlit interface** for easy interaction.
- **Machine Learning model** trained on email data to detect spam.
- **TF-IDF vectorizer** used for text feature extraction.
- Quick and accurate predictions for individual emails.

## Files in this Repository
- `app.py` - The Streamlit application code.
- `spam_classifier_model.pkl` - Pre-trained ML model.
- `tfidf_vectorizer.pkl` - TF-IDF vectorizer used for preprocessing.
- `spams.csv` - Original dataset used for training.
- `spam_detection.ipynb` - Jupyter Notebook with data analysis and model training steps.

## How to Run Locally
1. Clone the repository:
   git clone https://github.com/yourusername/email-spam-detection.git

2. Navigate to the project folder:
cd email-spam-detection

3. Install required packages:
pip install -r requirements.txt

4. Run the Streamlit app:
streamlit run app.py

5. Deployment
This app can be deployed easily on Streamlit Cloud or Hugging Face Spaces for a public URL.
