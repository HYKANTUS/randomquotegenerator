# pillow imports
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# miscellaneous imports
import random
import os
import string
from instabot import Bot
import textwrap

# random image file
path = "C:\\Users\\HP\\Documents\\pythonProject\\input"
files = os.listdir(path)
file = random.choice(files)
filepath = 'C:\\Users\\HP\\Documents\\pythonProject\\input\\' + file

print(f'random file found. File: {filepath}')


# random ID - for output .jpg
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


outfile = f'output{id_generator()}.jpg'

print(f'output filename generated. Name: output{id_generator()}.jpg')

# random quote
lines = open('quotes.txt').read().splitlines()
quote = random.choice(lines)

print(f'random quote found. Quote: {quote}')

# quote draw on image
astr = quote
para = textwrap.wrap(astr, width=15)

MAX_W, MAX_H = 1200, 1200
img = Image.open(filepath)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("C:\\Users\\HP\\Documents\\pythonProject\\BeautyMountainsPersonalUse-od7z.ttf", 148)

current_h, pad = 50, 10
for line in para:
    w, h = draw.textsize(line, font=font)
    draw.text(((MAX_W - w) / 2, current_h), line, font=font)
    current_h += h + pad

print(f'quote written on image')

directory = 'C:\\Users\\HP\\Documents\\pythonProject\\output\\'
filename = f'output{id_generator()}.jpg'
img.save(directory + filename)
image = directory + filename
print(f'image saved as output{id_generator()}.jpg to {directory}')

# instagram post
bot = Bot()
photo = image

print(f'output photo chosen. File: {photo}')

username = 'username'
password = 'password'

bot.login(username=username,
          password=password)

print(f'logged into instagram account. Account: {username}')

caption = 'Randomly generated image. Made in Python using the Pillow library. Script by Hykantus. '

bot.upload_photo(photo,
                 caption=caption)

print(f'successfully posted image with caption. Caption: {caption}')
