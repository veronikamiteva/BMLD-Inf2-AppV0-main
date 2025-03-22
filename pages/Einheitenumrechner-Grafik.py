# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously

import streamlit as st

st.title('Einheitenumrechnungsverlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Einheitenumrechnungsdaten vorhanden. Führen Sie eine Umrechnung auf der Startseite durch.')
    st.stop()

# Data by category
categories = data_df['category'].unique()
for category in categories:
    st.subheader(f'Daten für Kategorie: {category}')
    category_data = data_df[data_df['category'] == category]
    
    # Display line chart
    st.line_chart(data=category_data.set_index('timestamp')['value'], 
                  use_container_width=True)
    st.caption(f'Werte über Zeit für Kategorie: {category}')
    
    # Display table for the category
    st.table(category_data)
