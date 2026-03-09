import streamlit as st
import pandas as pd
import plotly.express as px

st.title("AI Bio-Signal Triage Dashboard")

data = {
    "Time":["0","5","10","15","20"],
    "HeartRate":[85,92,105,115,120],
    "BloodPressure":[120,115,100,90,85],
    "SpO2":[98,97,95,93,91],
    "RespRate":[16,18,20,24,28]
}

df = pd.DataFrame(data)

st.subheader("Heart Rate Trend")
st.line_chart(df["HeartRate"])

st.subheader("Blood Pressure Trend")
st.line_chart(df["BloodPressure"])

st.subheader("SpO2 Trend")
st.line_chart(df["SpO2"])

st.subheader("Respiratory Rate Trend")
st.line_chart(df["RespRate"])
