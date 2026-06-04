import streamlit as st
import pandas as pd
import plotly.express as px

investments = pd.read_csv(
    "data/investments.csv"
)

top = investments.groupby(
    "funding_round_id"
).size().reset_index(name="investments")

fig = px.histogram(
    top,
    x="investments",
    nbins=40
)

st.plotly_chart(fig)
