import streamlit as st
import pandas as pd

companies = pd.read_csv(
    "data/objects.csv"
)

startup = st.selectbox(
    "Select Startup",
    companies["name"].dropna()
)

data = companies[
    companies["name"]==startup
]

st.dataframe(data.T)
