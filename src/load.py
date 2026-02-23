import pandas as pd
from sqlalchemy import create_engine
import os


def load_to_postgres():

    db_config = {
        'user': 'postgres',
        'password': 'admin',
        'host': 'localhost',
        'port': '5433',
        'dbname': 'superstore'
    }

    connection_str = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
    engine = create_engine(connection_str)

    print(f"Loading to db{db_config['port']}...")

    csv_path = 'data/processed_data/superstore_processed.csv'

    if not os.path.exists(csv_path):
        csv_path = '../data/processed_data/superstore_processed.csv'

    if not os.path.exists(csv_path):
        print(
            f"Error: Cant find the file at {csv_path}.")
        return

    print(f"Loading: {csv_path}")
    df = pd.read_csv(csv_path)

    print(f"Sending {len(df)} rows to table 'orders'...")
    df.to_sql('orders', engine, if_exists='replace', index=False)

    print("Successfully loaded data to PostgreSQL!")


if __name__ == "__main__":
    load_to_postgres()
