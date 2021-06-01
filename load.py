#CS 205 final project

import pandas as pd
import sqlite3


def initialize_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    # create table
    c.execute("""CREATE TABLE IF NOT EXISTS professor_table (
                pk int,
                professor string, 
                department string, 
                college string, 
                location string, 
                glasses bool, 
                hair color enum, 
                hat bool, 
                sex string, 
                facial_hair bool)""")
    prof = pd.read_csv("GuessWhoData.csv")
    prof.to_sql("professor_table", conn, if_exists="replace", index=False)
    #c.execute("SELECT department FROM professor_table")
    #print(c.fetchall())
    #c.execute("DROP TABLE professor_table")

    c.execute("""CREATE TABLE IF NOT EXISTS computer_table (
                pk int,
                professor string, 
                department string, 
                college string, 
                location string, 
                glasses bool, 
                hair color enum, 
                hat bool, 
                sex string, 
                facial_hair bool)""")
    prof = pd.read_csv("GuessWhoData.csv")
    prof.to_sql("computer_table", conn, if_exists="replace", index=False)


initialize_db()    
