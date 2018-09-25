from PIL import Image

class MyImage:
	def __init__(self, filename: str):
		self.img = Image.open(filename).convert('RGB')
		self.pixels = self.img.load()
		self.size = self.img.size