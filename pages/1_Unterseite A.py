import pandas as pd
import streamlit as st

st.title('BMI Werte')

if 'data_df' not in st.session_state or st.session_state['data_df'].empty:
    st.info('Keine BMI Daten vorhanden. Berechnen Sie Ihren BMI auf der Startseite.')
    st.stop()
else:
    data_df = st.session_state['data_df']

# Ensure 'timestamp' column is in datetime format
data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], errors='coerce')

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)