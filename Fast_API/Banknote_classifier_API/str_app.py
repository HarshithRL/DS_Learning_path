import streamlit as st
import requests

# Define the URL of your FastAPI server
API_URL = 'http://127.0.0.1:8000'  # Adjust the URL accordingly

# Function to make API requests
def predict_banknote(variance, skewness, curtosis, entropy):
    payload = {
        'variance': variance,
        'skewness': skewness,
        'curtosis': curtosis,
        'entropy': entropy
    }
    response = requests.post(f'{API_URL}/predict', json=payload)
    return response.json()['prediction']

# Streamlit UI
def main():
    st.title('Banknote Predictor')
    st.write('Enter banknote measurements to predict authenticity:')

    variance = st.number_input('Variance:')
    skewness = st.number_input('Skewness:')
    curtosis = st.number_input('Curtosis:')
    entropy = st.number_input('Entropy:')

    if st.button('Predict'):
        prediction = predict_banknote(variance, skewness, curtosis, entropy)
        st.write(f'Prediction: {prediction}')

if __name__ == '__main__':
    main()
