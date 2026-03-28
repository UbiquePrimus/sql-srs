import streamlit as st
import pandas as pd
import duckdb

data = {"a" : [1,2,3], "b" : [4,5,6]}
df = pd.DataFrame(data)

sql_query = st.text_area("Enter your query here")
st.write(f"Query: {sql_query}")

st.dataframe(duckdb.query(sql_query).df())