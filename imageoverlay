import os
from PIL import Image

filename = 'base.jpg'
filename1 = 'Cross.png'
base = Image.open(filename).convert("RGBA")
overlay = Image.open(filename1).convert("RGBA")

base.paste(overlay, (250, 450), overlay)
base.save('result.png')
