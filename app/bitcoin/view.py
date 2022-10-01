from flask.views import MethodView
from flask import render_template, redirect, url_for,request,json,current_app,jsonify
from app.bitcoin.controllers import BitcoinController
import requests
import math


headers={
	'X-CMC_PRO_API_KEY':'4527c1dc-cd47-4e9b-aa70-ffd56228731a',
	'Accepts': 'application/json'
}

params = {
	'start':'1',
	'limit':'5',
	'convert':'USD'

}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

def get_price():
	lst={}
	json = requests.get(url,params=params,headers=headers).json()
	coins = json['data']
	for i in coins:
		if i['symbol'] == 'BTC':
			lst['price'] = i['quote']['USD']['price']
			lst['date'] = i['last_updated']
			new_price = i['quote']['USD']['price']
			updated_date = str(i['last_updated'])
	last_price = BitcoinController().get_bitcoin_price().get('price')
	if last_price:
		if (last_price)!=(new_price):
			BitcoinController().insert_coin_data(new_price,updated_date)
	else:
		BitcoinController().insert_coin_data(new_price,updated_date)
	return lst

class BitcoinPrice(MethodView):

	def get(self):
		data = get_price()
		return render_template('/bitcoin/price.html',result=data) 	

class CurrentBitcoinPrice(MethodView):
	def get(self):
		return get_price()


class PriceList(MethodView):
	def get(self,page):
		list_count = BitcoinController().fetch_list_count()
		pricelist = BitcoinController().fetch_paginated_list(page)
		list_count = list_count.get('list_count')/10
		page_num = math.ceil(list_count)+1
		return render_template('/bitcoin/pricelist.html',pricelist=pricelist,page_num=page_num)

class Home(MethodView):
	def get(self):
		return render_template('/bitcoin/start.html')

	def post(self):
		return redirect(url_for('bp.price'))