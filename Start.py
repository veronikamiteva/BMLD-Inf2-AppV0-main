import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

st.write("Diese App wurde von den folgenden Personen entwickelt:")

student_email_veroninka = "mitevver@students.zhaw.ch"
student_email_phiphi = "cungphi1@students.zhaw.ch"
st.write("Veronika Miteva - " + f"{student_email_veroninka}")
st.write("Phi Phi Cung - " + f"{student_email_phiphi}")

st.write("Diese App dient als leeres Gerüst für die App-Entwicklung im Modul Informatik 2 (BMLD/ZHAW).")