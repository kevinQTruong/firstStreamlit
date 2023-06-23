import numpy as np
from datetime import time, datetime
import altair as alt
import pandas as pd
import streamlit as st

st.header("st.slider - Day 8")

st.subheader("Slider")

age = st.slider("How old are you?", 0, 130, 25)

st.write("I'm", age, "years old")

st.subheader("Range slider")

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

st.write("Values:", values)

st.subheader("Range time slider")

appointment = st.slider(
    "Schedule your appointment:", value=(time(10, 30), time(12, 45))
)

st.write("You're scheduled for:", appointment)

st.subheader("Datetime slider")

start_time = st.slider(
    "When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm"
)

st.write("Start time:", start_time)

st.header("st.write - Day 5")

st.write("Hello, *World!* :sunglasses:")

st.write(1234)

df = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)

st.write(df)

st.write("Below is a DataFrame:", df, "Above is a dataframe.")

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=["a", "b", "c"],
)

st.write(df2)

c = (
    alt.Chart(df2)
    .mark_point()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(c)
