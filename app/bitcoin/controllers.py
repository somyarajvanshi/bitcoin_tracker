from config import Config

class BitcoinController:

	def __init__(self):
		self.db_conn = Config.SQLITE_CONN

	def insert_coin_data(self,new_price,updated_date):
		query = '''insert into bitcoin_data (price,datestamp) values("{}","{}")'''.format(new_price,updated_date)
		return self.db_conn.write_db(query)

	def get_bitcoin_price(self):
		query = '''select id,price from bitcoin_data where id=(select max(id) from bitcoin_data)'''
		return self.db_conn.query_db_one(query)

	def get_price_list(self):
		query = '''select * from bitcoin_data'''
		return self.db_conn.query_db(query)

	def fetch_list_count(self):
		query = '''select count(1) as list_count from bitcoin_data'''
		return self.db_conn.query_db_one(query)

	def fetch_paginated_list(self,page):
		query = '''select * from bitcoin_data limit 10 offset {}'''.format((page-1)*10)
		print(query)
		return self.db_conn.query_db(query)