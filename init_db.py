import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

# -------------------------------------------------------
# EXERCISES LIST
# -------------------------------------------------------
data = {
    "theme": ["cross_joins", "cross_joins"],
    "exercise_name": ["beverages_and_food", "sizes_and_trademarks"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"]],
    "last_reviewed": ["07-04-2026", "04-04-2026"]
}
memory_state_df = pd.DataFrame(data)
#con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")
con.execute("CREATE OR REPLACE TABLE memory_state AS SELECT * FROM memory_state_df")

# -------------------------------------------------------
# CROSS JOIN EXERCISES
# -------------------------------------------------------

csv = """
beverage, price
orange juice, 2.5
Expresso, 2
Tea, 3
"""
beverages = pd.read_csv(io.StringIO(csv))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

csv2 = """
food item, food price
cookie juice, 2.5
chocolatine, 2
muffin, 3
"""
food_items = pd.read_csv(io.StringIO(csv2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

sizes = '''
size
XS
M
L
XL
'''
sizes = pd.read_csv(io.StringIO(sizes))
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

trademarks = '''
trademark
Nike
Asphalte
Abercrombie
Lewis
'''
trademarks = pd.read_csv(io.StringIO(trademarks))
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")