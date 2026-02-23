import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:admin@localhost:5433/superstore')
query = 'SELECT * FROM orders LIMIT 5;'
df = pd.read_sql(query, engine)
print(df)
