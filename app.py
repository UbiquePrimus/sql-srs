import streamlit as st
import pandas as pd
import duckdb
import io

csv = '''
beverage, price
orange juice, 2.5
Expresso, 2
Tea, 3
'''
beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food item, food price
cookie juice, 2.5
chocolatine, 2
muffin, 3
'''
food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.query(answer).df()


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


sql_query = st.text_area("Enter your query here")
if sql_query:
    st.write(f"Query: {sql_query}")
    st.dataframe(duckdb.query(sql_query).df())

tab1, tab2 = st.tabs(["Tables", "Solutions"])

with tab1:
    st.write("beverages")
    st.dataframe(beverages)
    st.write("food items")
    st.dataframe(food_items)
    st.write("Expected")
    st.dataframe(solution)

with tab2:
    st.write("""
             SELECT * FROM beverages \n
CROSS JOIN food_items""")