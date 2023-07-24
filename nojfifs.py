import os
os.system("pip install pillow")
import sys
from PIL import Image

this_dir = os.path.dirname(__file__)
def process_downloaded_file(filename):
	for file in os.listdir(this_dir):
		last_characters = file[-4:]
		if(last_characters == 'jfif'):
			img = Image.open(file)
			fileName = file[:-4]
			img.save(fileName + "png")
			os.remove(fileName + "jfif")

for file in os.listdir(this_dir):
		last_characters = file[-4:]
		if(last_characters == 'jfif'):
			img = Image.open(file)
			fileName = file[:-4]
			img.save(fileName + "png")
			os.remove(fileName + "jfif")

		