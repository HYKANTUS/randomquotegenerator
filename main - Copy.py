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
from getpass import getpass
import sys
import time

account = 'account_name'
password = 'account_password'

# random image file
path = "input"
files = os.listdir(path)
file = random.choice(files)
filepath = 'input\\' + file

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
font = ImageFont.truetype("BeautyMountainsPersonalUse-od7z.ttf", 148)

line_dimensions = [draw.textsize(line, font=font) for line in para]
offset = (MAX_H - sum(h for w, h in line_dimensions)) // 2

current_h = offset
for line, (w, h) in zip(para, line_dimensions):
    draw.text(((MAX_W - w) // 2, current_h), line, font=font)
    current_h += h

print(f'quote written on image')

directory = 'output\\'
filename = f'output{id_generator()}.jpg'
img.save(directory + filename)
image = directory + filename
print(f'image saved as output{id_generator()}.jpg to {directory}')

# instagram post
bot = Bot()
photo = image

print(f'output photo chosen. File: {photo}')

username = account
password = password

bot.login(username=username,
          password=password)

caption = 'Randomly generated image. Made in Python using the Pillow library. Script by Hykantus. #quotes #love #motivation #life #inspiration #quoteoftheday #instagram #motivationalquotes #instagood #quote #follow #bhfyp #like #happiness #positivevibes #success #believe #loveyourself #lifestyle #selflove #inspirationalquotes #happy #lovequotes #yourself #poetry #mindset #goals #quotestagram #quotestoliveby #bhfyp'

bot.upload_photo(photo,
                 caption=caption)

print(f'successfully posted image with caption. Caption: {caption}')

print('sleeping for 900 seconds (15 mins)\nCountdown until the next time this script will run: ')
for remaining in range(900, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)
sys.stdout.write("\rComplete. Running Code again now:             \n")
