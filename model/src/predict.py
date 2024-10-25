import streamlit as st
import numpy as np
import pickle
import json
import base64
import os
import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler

# For Local Checks

def load_model():
    with open(
        r"C:\Users\91948\Documents\VS Code Files\Local_Algerian-Fire-Forecaster-main\model\saved models.pickle",
        "rb",
    ) as f:
        return pickle.load(f)

# For Deployment

# def load_model():
#     github_raw_url = "https://github.com/Bharathkumar-Tamilarasu/Algerian-Fire-Forecaster/blob/main/model/forecast%20model.pickle"

#     response = requests.get(github_raw_url)

#     if response.status_code == 200:
#         return pickle.loads(response.content)
#     else:
#         print(f"Failed to fetch the model file. Status code: {response.status_code}")
#         return None

# For Local Checks

def load_prediction_input():
    with open(
        r"C:\Users\91948\Documents\VS Code Files\Local_Algerian-Fire-Forecaster-main\model\prediction_input.json",
        "rb",
    ) as f:
        return json.load(f)

# For Deployment

# def load_prediction_input():
#     github_raw_url = "https://raw.githubusercontent.com/Bharathkumar-Tamilarasu/Algerian-Fire-Forecaster/main/model/prediction_input.json"

#     response = requests.get(github_raw_url)

#     if response.status_code == 200:
#         return json.loads(response.content)
#     else:
#         print(
#             f"Failed to fetch the prediction input file. Status code: {response.status_code}"
#         )
#         return None

def preprocess_input(temperature,rh,ws,rain,ffmc,dmc,isi,region,scaler):
    temp_df = [[temperature,rh,ws,rain,ffmc,dmc,isi,region]]
    scaled_input = scaler.fit_transform(temp_df)
    return scaled_input

def load_predicted_values(scaled_input,model):
  predicted_value = model.predict(scaled_input)
  return round(float(predicted_value[0]),1)

saved_model = load_model()
model = saved_model['model']
scaler = saved_model['scale']
prediction_input = load_prediction_input()
region = prediction_input['region']

image_url = "https://raw.githubusercontent.com/Bharathkumar-Tamilarasu/Algerian-Fire-Forecaster/main/resources/Fire%20Forest%20Forecast%201.jpg"


def show_predict_page():
    
    # temperature = 35
    # rh = 48
    # ws = 18
    # rain = 0.0
    # ffmc = 90.1
    # dmc = 54.2
    # isi = 12.5
    # region = 0

    # temp_df = [[temperature,rh,ws,rain,ffmc,dmc,isi,region]]
    # scaled_input = scaler.transform(temp_df)
    # predicted_value = model.predict(scaled_input)
    # st.write(round(float(predicted_value[0]),1))

    st.image(image_url)
    st.markdown("""##### Provide input for the prediction""")
    
    temp_region = st.selectbox('Region',region)
    ip_temperature = st.number_input('Temperature (celsius)', step=1)
    ip_rh = st.number_input('Relative Humidity (%)')
    ip_ws = st.number_input('Wind speed (km/h):')
    ip_rain = st.number_input('Total Rain (mm)')
    ip_ffmc = st.number_input('Fine Fuel Moisture Code (FFMC) index')
    ip_dmc = st.number_input('Duff Moisture Code (DMC) index')
    ip_isi = st.number_input('Initial Spread Index (ISI) index')

    if temp_region == 'Bejaia Region':
        ip_region = 0
    elif temp_region == "Sidi-Bel Abbes Region":
        ip_region = 1
 
    scaled_input = preprocess_input(ip_temperature,ip_rh,ip_ws,ip_rain,ip_ffmc,ip_dmc,ip_isi,ip_region,scaler)

    ip_ok = st.button(
        "Estimate",
    )

    if ip_ok:
        predicted_value = load_predicted_values(scaled_input,model)
        st.success(
            f"The property's estimated worth is {int(predicted_value)} lakh rupees."
        )
    else:
        st.error("Please Enter the input")