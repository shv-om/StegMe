import numpy as np
from PIL import Image

class Stego_Encode:

	def __init__(self, image_path, binary_text_list):
		self.im = Image.open(image_path)
		self.binary_text_list = binary_text_list
		self.pix = np.zeros((self.im.width, self.im.height, 3), np.uint8)

	def encode(self):
		text_data = iter(self.binary_text_list)
		next_data = iter(text_data.__next__())

		for i in range(self.im.width):
			for j in range(self.im.height):
				temp_pixel = iter(self.im.getpixel((i, j)))
				for k in range(3):
					if k==0:
						try:
							#print("first try")
							temp = bin(temp_pixel.__next__()).lstrip('0b')[:7] + next(next_data)
							if len(temp)<8:
								diff = 8-len(temp)
								temp = '0'*diff + temp
							self.pix[i][j][k] = int(temp, 2)
							#print(temp)
						except StopIteration:
							try:
								#print("second try")
								next_data = iter(text_data.__next__())
								temp = bin(temp_pixel.__next__()).lstrip('0b')[:7] + next(next_data)
								if len(temp)<8:
									diff = 8-len(temp)
									temp = '0'*diff + temp
								self.pix[i][j][k] = int(temp, 2)
								#print(temp)
							except StopIteration:
								#print("second except")
								temp_a = self.im.getpixel((i, j))
								self.pix[i][j][k] = temp_a[k]
					else:
						try:
							#print("Else Statement")
							temp_else = self.im.getpixel((i, j))
							self.pix[i][j][k] = temp_else[k]
						except StopIteration:
							break
		return self.pix
