import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="predict the penguin",
    page_icon=":penguin:",
    layout="wide",
    initial_sidebar_state="expanded",
)

model_pipe = joblib.load("penguinspipe.pkl")

st.title("Predict the Penguin!")

island = st.selectbox("Select one island", 
                       ["Torgersen","Biscoe","Dream"])

bill_length = st.number_input("Digit the bill length (mm)",25,65,40)
bill_depth = st.number_input("Digit the bill depth (mm)",8,30,20)
flipper_length = st.number_input("Digit the flipper length (mm)",150,250,200)
body_mass = st.number_input("Insert the weight of the penguin (g)",2000,7000,4200)


sex = st.radio("Select the gender of the penguin", ["Male", "Female"])

data = {
        "island": [island],
        "bill_length_mm": [bill_length],
        "bill_depth_mm": [bill_depth],
        "flipper_length_mm":[flipper_length],
        "body_mass_g": [body_mass],
        "sex": [sex],
        }

input_df = pd.DataFrame(data)

if st.button("Prediction"):
    res = model_pipe.predict(input_df).astype(int)[0]

    classes = {0:'Adelie',
           1:'Gentoo',
           2:'Chinstrap',
           }

    y_pred = classes[res]

    st.success(f'The species of the penguin is: {y_pred}.')
