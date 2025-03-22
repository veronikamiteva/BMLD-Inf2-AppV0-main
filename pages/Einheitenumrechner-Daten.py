# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously

import pandas as pd
import streamlit as st

st.title('Einheitenumrechnungswerte')

if 'data_df' not in st.session_state or st.session_state['data_df'].empty:
    st.info('Keine Einheitenumrechnungsdaten vorhanden. Führen Sie eine Umrechnung auf der Startseite durch')
    st.stop()
else:
    data_df = st.session_state['data_df']

# Ensure 'timestamp' column is in datetime format
data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], errors='coerce')

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)