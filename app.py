
import os
import logging
import duckdb
import streamlit as st

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

if "exercises_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

con = duckdb.connect("data/exercices_sql_tables.duckdb", read_only=False)

#solution_df = duckdb.query(answer_str).df()


st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

with st.sidebar:
    theme = st.selectbox(
        "What do you want to study?",
        ["cross_joins", "Window functions", "GroupBy"],
        index=None,
        placeholder="Select your subject",
    )
    if theme:
        st.write("You are studying", theme)
        select_exercise_query = f"SELECT * FROM memory_state WHERE theme = '{theme}'"
    else:
        select_exercise_query = f"SELECT * FROM memory_state"
        st.write("No theme selected, picking first one in queue.")
    exercise = (
        con.execute(select_exercise_query)
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )
    st.write(exercise)

exercise_name = exercise.loc[0,"exercise_name"]
sql_solution = f"answers/{exercise_name}.sql"
with open(sql_solution, "r") as f:
    answer = f.read()

solution_df = con.execute(answer).df()

sql_query = st.text_area("Enter your query here")
if sql_query:
    result = con.execute(sql_query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("The columns don't match")

    if result.shape[0] != solution_df.shape[0]:
        st.write("The rows don't match")

#if sql_query:
#    st.write(f"Query: {sql_query}")
#    result = duckdb.query(sql_query).df()
#    st.dataframe(result)
#
#    if len(result.columns) != len(solution_df.columns):
#        st.write("The columns don't match")
#
#    try:
#        result = result[solution_df.columns]
#        st.dataframe(result.compare(solution_df))
#    except KeyError as e:
#        st.write("The columns don't match")
#
#    if result.shape[0] != solution_df.shape[0]:
#        st.write("The rows don't match")
#
tab1, tab2 = st.tabs(["Tables", "Solutions"])

with tab1:
    exercise_tables = exercise.loc[0,"tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)


with tab2:
    st.code(answer, language="sql")

