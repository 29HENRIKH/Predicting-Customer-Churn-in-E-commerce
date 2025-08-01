import pickle
import streamlit as st

model_path = pickle.load(open('C:/Users/Admin/Desktop/Projects/Predicting-Customer-Churn-in-E-commerce/model.pkl', 'rb'))

st.title('Churn Guard')

st.write('This app predicts whether a customer will churn based on their profile.')

st.write('Stay Ahead. Know Who Will Leave Before They Do.')

def predict_churn(features):
    prediction = model_path.predict([features])
    return 'Churn' if prediction[0] == 1 else 'No Churn'

st.sidebar.header('User Input Features')
def user_input_features():
    # Input fields
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen?", [0, 1])
    partner = st.selectbox("Has a Partner?", ["Yes", "No"])
    dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
    tenure = st.slider("Tenure (in months)", 0, 72)
    phone = st.selectbox("Phone Service", ["Yes", "No"])
    multi_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, step=0.1)
    total_charges = st.number_input("Total Charges", min_value=0.0, step=0.1)
    
    return (gender, senior, partner, dependents, tenure, phone, multi_lines, 
            internet, online_sec, tech_support, contract, paperless, payment, 
            monthly_charges, total_charges)

features = user_input_features()

# prediction button 
if st.button('Predict Churn'):
    makeprediction = model_path.predict([features])
    output = 'Churn' if makeprediction[0] == 1 else 'No Churn'
    st.success(f'The predicted churn is: {output}')
if __name__ == '__main__':
    st.write('Please fill in the details to predict customer churn.')
    st.write('The model will output whether the customer is likely to churn or not based on the provided features.')


    