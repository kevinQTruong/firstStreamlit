from datetime import time, datetime
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout="wide")

st.header("Layout - Day 19")

with st.expander("About this app"):
    st.write(
        "This app shows the various ways on how you can layout your Streamlit app."
    )
    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
        width=250,
    )

st.sidebar.header("Input")

user_name = st.sidebar.text_input("What is your name?")
user_emoji = st.sidebar.selectbox(
    "Choose an emoji", ["", "😄", "😆", "😊", "😍", "😴", "😕", "😱"]
)
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.subheader('Output')

col1, col2, col3 = st.columns(3)

with col1:
    if user_name != '':
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')


st.header("File uploader - Day 18")

st.subheader("Upload a CSV file")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv", "pdf"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataframe")
    st.write(df)
    st.subheader("Descriptive statistics")
    st.write(df.describe())
else:
    st.info("🖕 Upload a CSV file")

st.header("Secret - Day 17")

st.write(st.secrets["message"])

st.header("Day 16 - Customizing the theme of Streamlit apps")

st.write("Contents of the `.streamlit/config.toml` file of this app")

st.code(
    """
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
"""
)

number = st.sidebar.slider("Select a number:", 0, 10, 5)
st.write("Selected number from slider widget is:", number)

st.header("st.latex - Day 15")

st.latex(
    r"""
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    """
)


# st.header("streamlit_pandas_profiling - Day 14")

# df = pd.read_csv(
#     "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
# )

# pr = df.profile_report()

# st_profile_report(pr)

st.header("st.checkbox- Day 12")

st.write("What would you like to order?")

icecream = st.checkbox("Ice Cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("You ordered ice cream")

if coffee:
    st.write("You ordered coffee")

if cola:
    st.write("You ordered cola")

st.header("st.multiselect- Day 11")

st.subheader("Multiselect")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)

st.header("st.selectbox- Day 10")

st.subheader("Selectbox")

option = st.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
)

st.write("You selected:", option)

st.header("st.line_chart - Day 9")

st.subheader("Line chart")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

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
