#!/urs/bin/env python

from urllib.request import urlopen, quote
from json import loads

class Inventory():

	def __init__(self, nickname='0x109ab', appid=730):
		self.__nickname = str(nickname).lower()
		self.__appid = int(appid)

	def __get_inventory_url(self):
		try:
			int(self.__nickname)
			nickname_type = 'profiles'
		except Exception as e:
			nickname_type = 'id' 

		return ('http://steamcommunity.com/'
		+ nickname_type + '/'
		+ str(self.__nickname)
		+ '/inventory/json/'
		+ str(self.__appid) + '/2/')

	def __get_item_url(self, item):
		return ('http://steamcommunity.com/market/priceoverview/?'
		+ 'country=US&currency=1&appid=' + str(self.__appid)
		+ '&market_hash_name='+quote(item))


	def set_nickname(self, nickname):
		self.__nickname = nickname

	def set_appid(self, appid):
		self.__appid = appid

	def get_inventory_list(self):
		try:
			return loads(urlopen(self.__get_inventory_url()).read())
		except Exception as e:
			print('Could\'t fetch inventory db', e)
			return None

	def get_inventory_descriptions(self):
		description_list = list()
		buffer = self.get_inventory_list()
		try:
			for item in buffer['rgDescriptions']:
				try:
					description_list.append(
					buffer['rgDescriptions'][item]['market_hash_name'])
				except Exception as e:
					print('Could\'t get inventory item', e)
		except Exception as e:
			pass
		del buffer
		return description_list

	def get_item_list(self, item):
		try:
			return loads(urlopen(self.__get_item_url(item)).read())
		except Exception as e:
			return None

	def get_item_price(self, item):
		try:
			return self.get_item_list(item)['median_price'][5:]
		except Exception as e:
			return '0.00'

	def get_nickname(self):
		return self.__nickname

	def get_appid(self):
		return self.__appid
