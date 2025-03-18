import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol="webdav", fs_root_folder="Veronika_PhiPhi_DB")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    # parse_dates = ['timestamp']
    )

st.title("Unsere erste Streamlit App")

st.write("Einheitenumrechner")

st.write("Diese App wurde von den folgenden Personen entwickelt:")

student_email_veroninka = "mitevver@students.zhaw.ch"
student_email_phiphi = "cungphi1@students.zhaw.ch"
st.write("Veronika Miteva - " + f"{student_email_veroninka}")
st.write("Phi Phi Cung - " + f"{student_email_phiphi}")

st.write("Diese App ermöglicht das mühelose Umrechnen von Länge, Volumen, Gewicht und Temperatur zwischen verschiedenen Masseinheiten.")