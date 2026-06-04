import streamlit as st
import pandas as pd
import plotly.express as px

objects = pd.read_csv("data/objects.csv")

objects["funding_total_usd"] = pd.to_numeric(
    objects["funding_total_usd"],
    errors="coerce"
)

total_startups = len(objects)

total_funding = objects["funding_total_usd"].sum()

active = len(
    objects[
        objects["status"]=="operating"
    ]
)

closed = len(
    objects[
        objects["status"]=="closed"
    ]
)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Startups",f"{total_startups:,}")
col2.metric("Funding",f"${total_funding:,.0f}")
col3.metric("Operating",active)
col4.metric("Closed",closed)

top = objects.nlargest(
    10,
    "funding_total_usd"
)

fig = px.bar(
    top,
    x="name",
    y="funding_total_usd",
    title="Top Funded Startups"
)

st.plotly_chart(fig,use_container_width=True)
