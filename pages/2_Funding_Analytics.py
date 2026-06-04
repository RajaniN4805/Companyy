import streamlit as st
import pandas as pd
import plotly.express as px

funding = pd.read_csv(
    "data/funding_rounds.csv"
)

funding["raised_amount_usd"] = pd.to_numeric(
    funding["raised_amount_usd"],
    errors="coerce"
)

funding_type = funding.groupby(
    "funding_round_type"
)["raised_amount_usd"].sum().reset_index()

fig = px.pie(
    funding_type,
    names="funding_round_type",
    values="raised_amount_usd",
    title="Funding Distribution"
)

st.plotly_chart(fig)

top_rounds = funding.nlargest(
    20,
    "raised_amount_usd"
)

fig2 = px.bar(
    top_rounds,
    x="raised_amount_usd",
    y="company_id",
    orientation="h"
)

st.plotly_chart(fig2)
