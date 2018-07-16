#!/urs/bin/env python

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from steamapi import Inventory
from threading import Thread

class FirstLayout(BoxLayout):
	logbox = ObjectProperty(None)

	def submit(self, text):
		self.text = text
		t = Thread(target=self.bg_proc, args=())
		t.start()

	def bg_proc(self):
		a = Inventory(self.text, 570)
		self.logbox.text += 'Fetching inventory items for ' + str(self.text).upper() + ' - '
		buffer = a.get_inventory_descriptions()
		price_buffer = ''
		counter = float()
		if len(buffer) != 0:
			self.logbox.text += ' OK\nFetching item prices. It will take some time...\n'
			for i in buffer:
				price_buffer = a.get_item_price(i)
			 	self.logbox.text += i + ' - $' + price_buffer + '\n'
			 	counter += float(price_buffer)
			self.logbox.text += 'Your total inventory sum is - $' + str(counter)
		else:
			self.logbox.text += ' Failed\n'


class Main(App):
	def build(self):
		self.title = 'Dota 2 Inventory calculator v0.1'
		return FirstLayout()

if __name__ == '__main__':
	Main().run()