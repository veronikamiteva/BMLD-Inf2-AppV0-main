import streamlit as st
from utils import helpers
from utils.data_manager import DataManager
from functions.convert_units import convert_units
# from functions.unit_converter_form import unit_converter_form
# from functions.reset_units import reset_units

st.title("📏 Einheitenumrechner (US ↔ EU Masseinheiten)")
st.markdown("Länge, Volumen, Gewicht und Temperatur ganz einfach umrechnen")

def unit_converter_form():
    with st.form(key="unit_converter"):
        value = st.number_input("Wert eingeben", min_value=0.0, format="%.2f")
        submit_button = st.form_submit_button(label="Umrechnen")
        return value, submit_button

# Initialize session state variables
if "category" not in st.session_state:
    st.session_state.category = list(helpers.categories.keys())[0]
if "from_unit" not in st.session_state:
    st.session_state.from_unit = helpers.categories[st.session_state.category][0]
if "to_unit" not in st.session_state:
    st.session_state.to_unit = helpers.categories[st.session_state.category][1]

# Function to reset unit selections when category changes
def reset_units():
    st.session_state.from_unit = helpers.categories[st.session_state.category][0]
    st.session_state.to_unit = helpers.categories[st.session_state.category][1]

# Move category selection outside the form
category = st.selectbox("Kategorie auswählen", list(helpers.categories.keys()), key="category", on_change=reset_units)

from_unit = st.selectbox("Umrechnen von", helpers.categories[category], key="from_unit")

# Remove selected 'from_unit' from 'to_unit' list
to_unit_options = [unit for unit in helpers.categories[category] if unit != st.session_state.from_unit]
to_unit = st.selectbox("Umrechnen in", to_unit_options, key="to_unit")


# Initialize result with a default value
result = None
# Calculate conversion
value, submit_button = unit_converter_form()  # Get the value and submit button state from the form
if submit_button:
    result = convert_units(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result} {to_unit}")

# Save the result to persistent storage
record_dict = None  # Initialize record_dict to avoid undefined variable error
if result is not None:
    record_dict = {
        "category": category,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "value": value,
        "result": result,
        "timestamp": helpers.ch_now(),
    }

if "data_df" not in st.session_state:
    st.session_state.data_df = []  # Initialize as an empty list

if record_dict is not None:  # Append only if record_dict is defined
    DataManager().append_record(session_state_key="data_df", record_dict=record_dict)
