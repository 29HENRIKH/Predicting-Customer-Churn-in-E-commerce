# import pickle
# import streamlit as st 

# model = pickle.load(open('C:/Users/Admin/Desktop/Projects/Predicting-Customer-Churn-in-E-commerce/model.pkl', 'rb'))
# def main() :
#    st.title('Churn Guard')

#    st.write('This app predicts whether a customer will churn based on their profile.')

#    st.write('Stay Ahead. Know Who Will Leave Before They Do.')

#     # Input fields
#    gender = st.selectbox("Gender", ["Male", "Female"])
#    partner = st.selectbox("Has a Partner?", ["Yes", "No"])
#    dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
#    tenure = st.slider("Tenure (in months)", 0, 72)
#    phone = st.selectbox("Phone Service", ["Yes", "No"])
#    multi_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
#    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
#    online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
#    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
#    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
#    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
#    payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
#    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, step=0.1)
#    total_charges = st.number_input("Total Charges", min_value=0.0, step=0.1)
    
#      # Now we make the prediction code 
# if st.button('Predict'):
#       makeprediction = model.predict([[gender, partner, dependents, tenure, phone, multi_lines, 
#       internet, online_sec, tech_support, contract, paperless, payment, 
#       monthly_charges, total_charges]])
#       output = round(makeprediction)
#       st.success(f'Prediction: The customer is likely to {output}')

#   #   # Encode inputs manually (adjust to match your model training)
#   #     encoded_input = np.array([
#   #       1 if gender == "Male" else 0,
#   #       1 if partner == "Yes" else 0,
#   #       1 if dependents == "Yes" else 0,
#   #       tenure,
#   #       1 if phone == "Yes" else 0,
#   #       1 if multi_lines == "Yes" else 0,
#   #       0 if internet == "No" else (1 if internet == "DSL" else 2),
#   #       1 if online_sec == "Yes" else 0,
#   #       1 if tech_support == "Yes" else 0,
#   #       0 if contract == "Month-to-month" else (1 if contract == "One year" else 2),
#   #       1 if paperless == "Yes" else 0,
#   #       0 if payment == "Electronic check" else (1 if payment == "Mailed check" else (2 if payment == "Bank transfer" else 3)),
#   #       monthly_charges,
#   #       total_charges
#   #   ]).reshape(1, -1)

#   #  if st.button('Predict'):
#   #       prediction = model.predict(encoded_input)[0]
#   #       result = "Churn" if prediction == 1 else "Not Churn"
#   #       st.success(f'Prediction: The customer is likely to **{result}**.')



# if __name__ == '__main__':
#        main()

# import streamlit as st
# import pickle
# import numpy as np

# # ✅ Load the model ONCE, globally
# model = pickle.load(open('C:/Users/Admin/Desktop/Projects/Predicting-Customer-Churn-in-E-commerce/model.pkl', 'rb'))

# def main():
#     st.title('Churn Guard')

#     # Input features
#     gender = st.selectbox("Gender", ["Male", "Female"])
#     partner = st.selectbox("Has a Partner?", ["Yes", "No"])
#     dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
#     tenure = st.slider("Tenure (months)", 0, 72)
#     phone = st.selectbox("Phone Service", ["Yes", "No"])
#     multi_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
#     internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
#     online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
#     tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
#     contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
#     paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
#     payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
#     monthly_charges = st.number_input("Monthly Charges", 0.0)
#     total_charges = st.number_input("Total Charges", 0.0)

#     # Prediction button
#     if st.button("Predict"):
#         # Manual encoding (if no preprocessor is saved with model)
#         encoded = np.array([
#             1 if gender == "Male" else 0,
#             1 if partner == "Yes" else 0,
#             1 if dependents == "Yes" else 0,
#             tenure,
#             1 if phone == "Yes" else 0,
#             1 if multi_lines == "Yes" else 0,
#             0 if internet == "No" else (1 if internet == "DSL" else 2),
#             1 if online_sec == "Yes" else 0,
#             1 if tech_support == "Yes" else 0,
#             0 if contract == "Month-to-month" else (1 if contract == "One year" else 2),
#             1 if paperless == "Yes" else 0,
#             0 if payment == "Electronic check" else (1 if payment == "Mailed check" else (2 if payment == "Bank transfer" else 3)),
#             monthly_charges,
#             total_charges
#         ]).reshape(1, -1)

#         prediction = model.predict(encoded)[0]
#         result = "Churn" if prediction == 1 else "Not Churn"
#         st.success(f"Prediction: The customer is likely to **{result}**.")

# if __name__ == '__main__':
#     main()
# import streamlit as st
# import pickle
# import numpy as np

# # ✅ Load model
# model = pickle.load(open('C:/Users/Admin/Desktop/Projects/Predicting-Customer-Churn-in-E-commerce/model.pkl', 'rb'))

# def main():
#     st.title('Churn Guard')
#     st.write('Predict whether a customer is likely to churn.')

#     # Input widgets (now includes all features)
#     gender = st.selectbox("Gender", ["Male", "Female"])
#     partner = st.selectbox("Has a Partner?", ["Yes", "No"])
#     dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
#     tenure = st.slider("Tenure (months)", 0, 72)
#     phone = st.selectbox("Phone Service", ["Yes", "No"])
#     multi_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
#     internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
#     online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
#     online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
#     device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
#     tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
#     streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
#     streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
#     contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
#     paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
#     payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
#     monthly_charges = st.number_input("Monthly Charges", 0.0)
#     total_charges = st.number_input("Total Charges", 0.0)

#     if st.button("Predict Churn"):
#         # ✅ Manual encoding of all inputs
#         encoded = np.array([
#             1 if gender == "Male" else 0,
#             1 if partner == "Yes" else 0,
#             1 if dependents == "Yes" else 0,
#             tenure,
#             1 if phone == "Yes" else 0,
#             1 if multi_lines == "Yes" else 0,
#             0 if internet == "No" else (1 if internet == "DSL" else 2),
#             1 if online_sec == "Yes" else 0,
#             1 if online_backup == "Yes" else 0,
#             1 if device_protection == "Yes" else 0,
#             1 if tech_support == "Yes" else 0,
#             1 if streaming_tv == "Yes" else 0,
#             1 if streaming_movies == "Yes" else 0,
#             0 if contract == "Month-to-month" else (1 if contract == "One year" else 2),
#             1 if paperless == "Yes" else 0,
#             0 if payment == "Electronic check" else (1 if payment == "Mailed check" else (2 if payment == "Bank transfer" else 3)),
#             monthly_charges,
#             total_charges
#         ]).reshape(1, -1)

#         prediction = model.predict(encoded)[0]
#         result = "Churn" if prediction == 1 else "Not Churn"
#         st.success(f"Prediction: The customer is likely to **{result}**. This is because the customer  ")

# if __name__ == '__main__':
#     main()
import streamlit as st
import pickle
import numpy as np

# ✅ Load model
model = pickle.load(open('model.pkl', 'rb'))

def main():
    st.set_page_config(page_title="Churn Guard", layout="centered")
    st.title(' Churn Guard')
    st.markdown("Welcome to **Churn Guard** — a predictive tool built to help businesses anticipate customer churn before it happens. Provide customer profile details below to get insights.")

    # Input widgets
    gender = st.selectbox("Gender", ["Male", "Female"])
    partner = st.selectbox("Has a Partner?", ["Yes", "No"])
    dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
    tenure = st.slider("Tenure (months)", 0, 72)
    phone = st.selectbox("Phone Service", ["Yes", "No"])
    multi_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
    monthly_charges = st.number_input("Monthly Charges", 0.0)
    total_charges = st.number_input("Total Charges", 0.0)

    if st.button("Predict Churn"):
        # Manual encoding
        encoded = np.array([
            1 if gender == "Male" else 0,
            1 if partner == "Yes" else 0,
            1 if dependents == "Yes" else 0,
            tenure,
            1 if phone == "Yes" else 0,
            1 if multi_lines == "Yes" else 0,
            0 if internet == "No" else (1 if internet == "DSL" else 2),
            1 if online_sec == "Yes" else 0,
            1 if online_backup == "Yes" else 0,
            1 if device_protection == "Yes" else 0,
            1 if tech_support == "Yes" else 0,
            1 if streaming_tv == "Yes" else 0,
            1 if streaming_movies == "Yes" else 0,
            0 if contract == "Month-to-month" else (1 if contract == "One year" else 2),
            1 if paperless == "Yes" else 0,
            0 if payment == "Electronic check" else (1 if payment == "Mailed check" else (2 if payment == "Bank transfer" else 3)),
            monthly_charges,
            total_charges
        ]).reshape(1, -1)

        # Prediction and probability
        prediction = model.predict(encoded)[0]
        probabilities = model.predict_proba(encoded)[0]
        prob_churn = round(probabilities[1] * 100, 2)
        prob_not_churn = round(probabilities[0] * 100, 2)

        result = "Churn" if prediction == 1 else "Not Churn"
        st.success(f" Prediction: The customer is likely to **{result}**.")

        # Show probabilities
        st.markdown(f"**Probability of Churn:** {prob_churn}%")
        st.markdown(f"**Probability of Not Churning:** {prob_not_churn}%")

        # Explain the result
        if prediction == 1:
            st.info(" This prediction is based on behavior patterns such as short tenure, low service usage, or flexible contract types.")
        else:
            st.info(" The customer appears stable, possibly due to longer tenure, bundled services, or annual contracts.")

        # Advice
        st.markdown("---")
        st.subheader(" Advice")
        st.write("Focus on improving service experience, offering rewards for loyalty, and reducing friction during customer support to boost retention.")

if __name__ == '__main__':
    main()
