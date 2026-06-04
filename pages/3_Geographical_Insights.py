import streamlit as st
import pandas as pd
import plotly.express as px

companies = pd.read_csv(
    "data/objects.csv"
)

country = companies.groupby(
    "country_code"
).size().reset_index(name="count")

fig = px.choropleth(
    country,
    locations="country_code",
    color="count",
    title="Startup Distribution"
)

st.plotly_chart(fig)
