from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('excel.csv')
font = ImageFont.truetype('arial.ttf',60)
for index,j in df.iterrows():
    img = Image.open('certificate sam.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(400,373),text='{}'.format(j['name']),fill=(0,0,0),font=font)
    img.save('output/{}.jpg'.format(j['name']))