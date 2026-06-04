import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/objects.csv")

df = df[
    ["relationships",
     "milestones",
     "funding_rounds",
     "funding_total_usd"]
]

df = df.dropna()

X = df.drop(
    "funding_total_usd",
    axis=1
)

y = df["funding_total_usd"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2
)

model = RandomForestRegressor()

model.fit(X_train,y_train)

st.success(
    f"Model Score: {model.score(X_test,y_test):.2f}"
)
