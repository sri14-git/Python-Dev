import streamlit as st
import plotly.express as px
from function import getdata
st.title("Weather Forecast With Histogram")
place=st.text_input("Enter the City")
slider=st.slider("Forecast Days ",min_value=1,max_value=5)
option=st.selectbox("Select Data to View",("Temperature","Sky"))
st.subheader(f"{option} for the next {slider} days in {place}....")

if place:
    fildata = getdata(place, slider)
    if option=="Temperature":
        temperature = [dict["main"]["temp"] for dict in fildata]
        dates=[dict["dt_txt"] for dict in fildata]
        figure=px.line(x=dates,y=temperature,labels={"y":"Temperature","x":"Dates"})
        st.plotly_chart(figure)
    if option=="Sky":
        fildata = [dict["weather"][0]["main"] for dict in fildata]
