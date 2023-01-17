#!/usr/bin/env python
# coding: utf-8
import argparse
import pandas as pd
from sqlalchemy import create_engine

def parse_args(known=False):
    parser = argparse.ArgumentParser(description='Ingest Parquet data to Postgres')
    parser.add_argument('--user', type=str, help='User name for Postgres')
    parser.add_argument('--password', type=str, help='Password for Postgres')
    parser.add_argument('--host', type=str, help='Host for Postgres')
    parser.add_argument('--port', type=str, help='Host for Postgres')
    parser.add_argument('--db', type=str, help='Database name for Postgres')
    parser.add_argument('--table_name', type=str, help='Table name for Postgres')
    parser.add_argument('--database_name', type=str, help='Host for Postgres')
    parser.add_argument('--fpth', type=str, help='Path to the csv file')
    return parser.parse_args()

def main(params):
    engine = create_engine(f'postgresql://{params.user}:{params.password}@{params.host}:{params.port}/{params.db}')
    df = pd.read_csv(params.fpth)
    df.to_sql(name=params.table_name, con=engine)

if __name__ == "__main__":
    args = parse_args()
    main(args)