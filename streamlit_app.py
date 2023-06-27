import time as tm
from datetime import time, datetime
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import requests

st.set_page_config(layout="wide")

st.header("external api - Day 26")
st.sidebar.header("Input")
selected_type = st.sidebar.selectbox(
    "Select an activity type",
    [
        "education",
        "recreational",
        "social",
        "diy",
        "charity",
        "cooking",
        "relaxation",
        "music",
        "busywork",
    ],
)

suggested_activity_url = f"http://www.boredapi.com/api/activity?type={selected_type}"
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
    with st.expander("About this app"):
        st.write(
            "Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API."
        )
with c2:
    with st.expander("JSON data"):
        st.write(suggested_activity)

st.subheader("Suggested activity")
st.info(suggested_activity["activity"])

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        label="Number of Participants",
        value=suggested_activity["participants"],
        delta="",
    )
with col2:
    st.metric(
        label="Type of Activity",
        value=suggested_activity["type"].capitalize(),
        delta="",
    )
with col3:
    st.metric(label="Price", value=suggested_activity["price"], delta="")


st.header("session state - Day 25")


def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs / 2.2046


def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg * 2.2046


st.header("Input")
col1, spacer, col2 = st.columns([2, 1, 2])
with col1:
    pounds = st.number_input("Pounds:", key="lbs")

with col2:
    # by giving a key "kg" streamlit will auto store this value int the session state
    kilogram = st.number_input("Kilograms:", key="kg", on_change=kg_to_lbs)

st.header("Output")
st.write("st.session_state object:", st.session_state)


st.header("st.cache - Day 24")

# Using cache
a0 = tm.time()
st.subheader("Using st.cache")


@st.cache_data
def load_data_a():
    df = pd.DataFrame(np.random.rand(2000000, 5), columns=["a", "b", "c", "d", "e"])
    return df


st.write(load_data_a())
a1 = tm.time()
st.info(a1 - a0)

# Not using cache
b0 = tm.time()
st.subheader("Not using st.cache")


def load_data_b():
    df = pd.DataFrame(np.random.rand(2000000, 5), columns=["a", "b", "c", "d", "e"])
    return df


st.write(load_data_b())
b1 = tm.time()
st.info(b1 - b0)


st.header("st.experimental_get_query_params - Day 23")

with st.expander("About this app"):
    st.write(
        "`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser."
    )

st.header("1. Instructions")
st.markdown(
    """
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
"""
)

# 2. Contents of st.experimental_get_query_params
st.header("2. Contents of st.experimental_get_query_params")
st.write(st.experimental_get_query_params())

st.header("3. Retrieving and displaying information from the URL")
query_params = st.experimental_get_query_params()

firstname = query_params.get("firstname", [""])[0]
surname = query_params.get("surname", [""])[0]

st.write(f"Hello **{firstname} {surname}**, how are you?")

st.header("form - Day 22")

st.header("1. Example of using `with` notation")
st.subheader("Coffee machine")

with st.form("my_form"):
    st.subheader("**Order your coffee**")

    # Input widgets
    coffee_bean_val = st.selectbox("Coffee bean", ["Arabica", "Robusta"])
    coffee_roast_val = st.selectbox("Coffee roast", ["Light", "Medium", "Dark"])
    brewing_val = st.selectbox(
        "Brewing method", ["Aeropress", "Drip", "French press", "Moka pot", "Siphon"]
    )
    serving_type_val = st.selectbox("Serving format", ["Hot", "Iced", "Frappe"])
    milk_val = st.select_slider("Milk intensity", ["None", "Low", "Medium", "High"])
    owncup_val = st.checkbox("Bring own cup")

    # Every form must have a submit button
    submitted = st.form_submit_button("Submit")

if submitted:
    st.markdown(
        f"""
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        """
    )
else:
    st.write("☝️ Place your order!")


st.header("progress - Day 21")

with st.expander("About this app"):
    st.write(
        "You can now display the progress of your calculations in a Streamlit app with the `st.progress` command."
    )

my_bar = st.progress(0)

for percent_complete in range(100):
    tm.sleep(0.05)
    my_bar.progress(percent_complete + 1)

st.balloons()

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
user_food = st.sidebar.selectbox(
    "What is your favorite food?",
    ["", "Tom Yum Kung", "Burrito", "Lasagna", "Hamburger", "Pizza"],
)

st.subheader("Output")

col1, col2, col3 = st.columns(3)

with col1:
    if user_name != "":
        st.write(f"👋 Hello {user_name}!")
    else:
        st.write("👈  Please enter your **name**!")

with col2:
    if user_emoji != "":
        st.write(f"{user_emoji} is your favorite **emoji**!")
    else:
        st.write("👈 Please choose an **emoji**!")

with col3:
    if user_food != "":
        st.write(f"🍴 **{user_food}** is your favorite **food**!")
    else:
        st.write("👈 Please choose your favorite **food**!")


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
