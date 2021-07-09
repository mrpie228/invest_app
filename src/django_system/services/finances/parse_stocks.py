from os import path
import os
import requests
import json
import sqlite3
from sqlite3 import Error
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d.%m.%Y %H:%M:%S")
PATH_TO_STOCKS_DB = 'dbs/stocks.db'
PATH_TO_STOCKS_DB_LIST = 'dbs/stocks_list.db'

API_KEY = 'daff707ebcbd9df18fa54565fd27508a'
all_stocks_url = f'https://financialmodelingprep.com/api/v3/stock/list/?apikey={API_KEY}'
nasdaq_stocks_url = f'https://financialmodelingprep.com/api/v3/nasdaq_constituent?apikey={API_KEY}'


def get_nasdaq_companies(new_file=False):
    path = 'dbs/nasdaq_companies.json'
    need_to_parse_companies_tickers = []
    sectors = []
    if new_file:
        r2 = requests.get(nasdaq_stocks_url)
        nasdaq_comp = r2.json()
        with open(path, 'w') as outfile:
            json.dump(nasdaq_comp, outfile)

    file = open(path)
    for company in json.load(file):
        need_to_parse_companies_tickers.append(company['symbol'])
        sectors.append(company['sector'])
    return need_to_parse_companies_tickers, sectors


def get_companies(need_to_parse_companies_tickers, connection, sectors, without_tables=False, with_request=True):
    path = 'dbs/all_companies.json'

    if with_request:
        r = requests.get(all_stocks_url)
        companies = r.json()
        with open(path, 'w') as outfile:
            json.dump(companies, outfile)
    else:
        file = open(path)
        companies = json.load(file)
    x = 0
    if without_tables:
        sql_create_all_stocks_table_command = f""" CREATE TABLE IF NOT EXISTS stocks_list (
                                                id integer PRIMARY KEY,
                                                name text NOT NULL,
                                                ticker text,
                                                price text,
                                                sector text,
                                                time text
                                            ); """
        for company in companies:
            if company['symbol'] in need_to_parse_companies_tickers:
                create_table(connection, sql_create_all_stocks_table_command)
                stock_in_db(connection, [company['name'], company['symbol'], company['price'], sectors[x], dt_string],
                            'stocks_list')
                x = x + 1
    else:
        for company in companies:
            if company['symbol'] in need_to_parse_companies_tickers:
                sql_create_all_stocks_table_command = f""" CREATE TABLE IF NOT EXISTS {company['symbol']} (
                                                id integer PRIMARY KEY,
                                                name text NOT NULL,
                                                ticker text,
                                                price text,
                                                sector text,
                                                time text
                                            ); """
                create_table(connection, sql_create_all_stocks_table_command)
                stock_in_db(connection, [company['name'], company['symbol'], company['price'], sectors[x], dt_string],
                            company['symbol'])
                x = x + 1


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)


def create_table(connection, commands):
    try:
        c = connection.cursor()
        c.execute(commands)
    except Error as e:
        print(e)


def stock_in_db(connection, what_add, table_name):
    sql = f''' INSERT INTO {table_name}(name,ticker,price,sector,time)
              VALUES(?,?,?,?,?) '''
    cur = connection.cursor()
    cur.execute(sql, what_add)
    connection.commit()

    return cur.lastrowid


def create_list_db(tickers, sectors):
    try:
        os.remove(PATH_TO_STOCKS_DB_LIST)
    except:
        pass
    connection = create_connection(PATH_TO_STOCKS_DB_LIST)
    get_companies(tickers, connection, sectors, True, False)
    connection.close()


def create_all():
    tickers, sectors = get_nasdaq_companies(new_file=True)
    connection = create_connection(PATH_TO_STOCKS_DB)
    get_companies(tickers, connection, sectors)
    connection.close()
    create_list_db(tickers, sectors)
    return len(tickers)
