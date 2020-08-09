import numpy as np
from PIL import Image

from convert import Binary_to_text

class Stego_Decode:

	def __init__(self, image_path):
		self.img = Image.open(image_path)
		self.decoded_message = ""

	def convert_to_pixels(self):
		self.pixels = np.asarray(self.img, np.uint8)
		#self.pixels.setflags(write=1)

	def decode(self):
		text_datalist = []

		for i in range(self.img.height):
			for j in range(self.img.width):
				for k in range(3):
					if k == 0:
						if bin(self.pixels[i][j][k]).lstrip('0b')[7:] == '0':
							text_datalist.append('0')
						else:
							#text_datalist.append(bin(self.pixels[i][j][k]).lstrip('0b')[7:])
							temp = bin(self.pixels[i][j][k]).lstrip('0b')
							if len(temp)<8:
								diff = 8-len(temp)
								temp = '0'*diff + temp
							text_datalist.append(temp[7:])
					else:
						pass

		# converting collected data to correct binary data
		'''data = text_datalist

		new_list = []

		try:
			for i in range(0, len(text_datalist), 8):
				new_list.append(str(data[i]) + str(data[i+1]) + str(data[i+2]) + str(data[i+3]) + str(data[i+4]) + str(data[i+5]) + str(data[i+6]) + str(data[i+7]))
		except:
			pass'''

		data = iter(text_datalist)

		new_list = []

		try:
			for i in range(len(text_datalist)):
				#print(next(data) + next(data) + next(data) + next(data) + next(data) + next(data) + next(data) + next(data))
				new_list.append(next(data) + next(data) + next(data) + next(data) + next(data) + next(data) + next(data) + next(data))
		except:
			pass

		# Comparing the real data with the converted data
		binary_data = Binary_to_text(new_list)

		self.decoded_message = binary_data.convert_to_text()

		return self.decoded_message
