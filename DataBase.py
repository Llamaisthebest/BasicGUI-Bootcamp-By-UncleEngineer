# DataBase

import sqlite3

conn = sqlite3.connect('product-datasase.sqlite3')
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS transaction_history (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				tid TEXT,
				stamp TEXT,
				product TEXT,
				price REAL,
				quan REAL,
				total REAL)""")

print('Success')

def insert_transaction(data):

	ID = None
	tid = data['tid']
	stamp = data['stamp']
	product = data['product']
	price = data['price']
	quan = data['quan']
	total = data['total']

	with conn:
		command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
		c.execute(command,(ID,tid,stamp,product,price,quan,total))
		conn.commit()
	print('Inserted!')


def veiw_transaction():
	with conn:
		c.execute("SELECT * FROM transaction_history")
		data = c.fetchall()
		print(data)

transaction = {'tid':'123412341234',
			   'stamp':'2021-12-12 11:46:20',
			   'product':'Beries',
			   'price':12,
			   'quan':1000,
			   'total':12000}

insert_transaction(transaction)

veiw_transaction()