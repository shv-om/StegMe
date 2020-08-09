# to convert text to binary code list and a binary code list to text.
import random

class Text_to_binary:

	def __init__(self, text):
		self.text = text
		self.text += '`'

	def convert_to_binary(self):
		new_data = []

		for i in self.text:
			new_data.append(format(ord(i), '08b'))

		return new_data


class Binary_to_text:

	def __init__(self, data):
		self.data = data
		self.string = ""

	def convert_to_text(self):

		for j in self.data:
			#print(j)
			if j != '':
				try:
					self.string += chr(int(j, 2))
				except:
					self.string += chr(0)
				if int(j, 2) == 96:	# First occurance of '`' stops the iteration of the data
					break
			else:
				j = random.choice(['0', '1'])
				try:
					self.string += chr(int(j, 2))
				except:
					self.string += chr(0)
				if int(j, 2) == 96:	# First occurance of '`' stops the iteration of the data
					break

		'''for j in self.data:
			#print(j)
			try:
				self.string += chr(int(j, 2))
			except:
				self.string += chr(0)
			if j != '' and int(j, 2) == 96:	# First occurance of '`' stops the iteration of the data
				break
			else:
				pass'''

		self.string.rstrip('`')
			
		return self.string
