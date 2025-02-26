import streamlit as st

# Page Configuration
st.set_page_config(page_title="✨ Unit Converter", page_icon="🔄", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #f7f9fc;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            color: #ff4b4b;
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
        }
        .stTextInput, .stSelectbox, .stNumberInput {
            border-radius: 10px;
            background-color: #ffffff;
            color: #333;
            font-size: 16px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            padding: 10px;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #ff7878;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<div class='title'>🔄 Unit Converter</div>", unsafe_allow_html=True)
st.write("Convert **Length**, **Weight**, and **Temperature** with ease! 🚀💖")

# Conversion Data
units = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, 
        "Inch": 39.3701, "Foot": 3.28084, "Yard": 1.09361, "Mile": 0.000621371
    },
    "Weight": {
        "Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": lambda c: {"Fahrenheit": (c * 9/5) + 32, "Kelvin": c + 273.15, "Rankine": (c + 273.15) * 9/5},
        "Fahrenheit": lambda f: {"Celsius": (f - 32) * 5/9, "Kelvin": (f - 32) * 5/9 + 273.15, "Rankine": f + 459.67},
        "Kelvin": lambda k: {"Celsius": k - 273.15, "Fahrenheit": (k - 273.15) * 9/5 + 32, "Rankine": k * 9/5},
        "Rankine": lambda r: {"Celsius": (r - 491.67) * 5/9, "Fahrenheit": r - 459.67, "Kelvin": r * 5/9}
    }
}

# Select Unit Type
unit_type = st.selectbox("🌟 Choose Category:", list(units.keys()))

# Input Value
value = st.number_input("✍️ Enter Value:", format="%.2f")

# Select From and To Units
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("🔻 From:", list(units[unit_type].keys()))
with col2:
    to_unit = st.selectbox("🔺 To:", list(units[unit_type].keys()))

# Conversion Logic
if st.button("💡 Convert Now!"):
    if unit_type == "Temperature":
        if from_unit == to_unit:
            result = value
        else:
            result = units["Temperature"][from_unit](value)[to_unit]
    else:
        result = value * (units[unit_type][to_unit] / units[unit_type][from_unit])

    st.success(f"🎉 {value} {from_unit} = **{round(result, 4)} {to_unit}**")
