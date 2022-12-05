import streamlit as st
import pandas as pd
from urllib.parse import urlencode
from urllib.request import urlretrieve

st.title("Houses for Sale in Dublin on daft.ie")

@st.cache
def load_data():
    # Download the dataset from daft.ie
    query = {
        "s[ignored_agents][0]": "543",
        "s[ignored_agents][1]": "6911",
        "s[ignored_agents][2]": "7027",
        "s[ignored_agents][3]": "7035",
        "s[ignored_agents][4]": "7141",
        "sort_by": "dateASC",
        "searchSource": "sale",
        "action": "search",
        "offset": "0",
    }
    url = "https://www.daft.ie/dublin-city/residential-property-for-sale?" + urlencode(query)
    urlretrieve(url, "data.csv")

    # Load the dataset and return as a Pandas DataFrame
    return pd.read_csv("data.csv")

data = load_data()

# Explore the data
st.subheader("Exploratory Data Analysis")
st.write(data.describe())
st.line_chart(data)

# Select columns to display
selected_columns = st.multiselect("Select Columns", data.columns)
st.dataframe(data[selected_columns])