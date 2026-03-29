import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

option = st.selectbox(
    "What do you want to study?",
    ["Joins", "Window functions", "GroupBy"],
    index=None,
    placeholder="Select your subject"
)
st.write("You are studying", option)

data = {"a" : [1,2,3], "b" : [4,5,6]}
df = pd.DataFrame(data)

sql_query = st.text_area("Enter your query here")
st.write(f"Query: {sql_query}")

st.dataframe(duckdb.query(sql_query).df())