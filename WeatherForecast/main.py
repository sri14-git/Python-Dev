import streamlit as st

st.title("Weather Forecast With Histogram")
place=st.text_input("Enter the City")
slider=st.slider("Forecast Days ",min_value=1,max_value=5)
option=st.selectbox("Select Data to View",("Temperature","Sky"))
st.subheader(f"{option} for the next {slider} days in {place}....")