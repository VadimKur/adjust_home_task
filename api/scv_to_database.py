import sqlite3
import csv

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

cursor.execute("SELECT * FROM usage_info_api_usageinfomodel;")
all_results = cursor.fetchall()
print(all_results)

with open('dataset.csv', 'r') as file:
    print('started the insertion')
    for idx, row in enumerate(file):
        line = row.split(',')
        line.insert(0, idx)
        cursor.execute('insert into usage_info_api_usageinfomodel values (?,?,?,?,?,?,?,?,?,?)', line)
        connection.commit()
sql = "DELETE FROM usage_info_api_usageinfomodel WHERE date = 'date'"
cursor.execute(sql)
connection.commit()

print('finished')
connection.close()
