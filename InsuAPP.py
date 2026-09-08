import streamlit as st
import pandas as pd
import joblib

model = joblib.load('insurance_model.pkl')

st.title('Insurance Premium Predictor')

age = st.number_input(
    'Age',
    min_value=18,
    max_value=100,
    value=30
)

bmi = st.number_input(
    'BMI',
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

children = st.number_input(
    'Children',
    min_value=0,
    max_value=10,
    value=0
)

sex = st.selectbox(
    'Sex',
    ['female', 'male']
)

smoker = st.selectbox(
    'Smoker',
    ['no', 'yes']
)

region = st.selectbox(
    'Region',
    [
        'northeast',
        'northwest',
        'southeast',
        'southwest'
    ]
)

customer = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'children': [children],
    'sex_male': [1 if sex == 'male' else 0],
    'smoker_yes': [1 if smoker == 'yes' else 0],
    'region_northwest': [
        1 if region == 'northwest' else 0
    ],
    'region_southeast': [
        1 if region == 'southeast' else 0
    ],
    'region_southwest': [
        1 if region == 'southwest' else 0
    ]
})

if st.button('Predict'):
    prediction = model.predict(customer)[0]
    prediction = max(0, prediction)

    st.success(
        f'Predicted Insurance Premium: '
        f'${prediction:,.2f}'
    )

st.caption(
    'This estimate is for educational purposes only.'
)