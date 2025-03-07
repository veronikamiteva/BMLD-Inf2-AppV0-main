import streamlit as st
import pandas as pd

st.title("Unsere erste Streamlit App")

st.write("Einheitenumrechner")

st.write("Diese App wurde von den folgenden Personen entwickelt:")

student_email_veroninka = "mitevver@students.zhaw.ch"
student_email_phiphi = "cungphi1@students.zhaw.ch"
st.write("Veronika Miteva - " + f"{student_email_veroninka}")
st.write("Phi Phi Cung - " + f"{student_email_phiphi}")

st.write("Diese App ermöglicht das mühelose Umrechnen von Länge, Volumen, Gewicht und Temperatur zwischen verschiedenen Masseinheiten.")