import psycopg2
from scrape import web_text
# import numpy as np


conn = psycopg2.connect(database="typing-DB-webscrape", user='postgres', password='ManishPort', host='localhost')

cur = conn.cursor()

quotes, num_of_quotes = web_text()

a = list(range(0, num_of_quotes))
b = quotes


listy = []
for i, j in zip(a, b):
    listy.append([i, j])
# print(listy)


insert_query = 'INSERT INTO "Symbiosis_quotes" (id, quote_text) values (%s, %s)'
cur.executemany(insert_query, listy)





conn.commit()
conn.close()