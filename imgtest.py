import PIL
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

img = Image.open("img.png")
Xdim, Ydim = img.size
Xdim = 128
Ydim = 128

img = img.resize((int(Xdim), int(Ydim)))
img.save("img.png")
img = Image.open("img.png")


foreground = Image.open("test2.png")
position = Image.open("test4.png")

img.paste(foreground, (0, 0), foreground)
img.paste(position, (0, 0), position)

msg='Toby'
txt = Image.new('RGBA',img.size, (255,255,255,0))
font = ImageFont.truetype("font/Daum_SemiBold.ttf", int(12.8))
draw = ImageDraw.Draw(txt)
w, h = draw.textsize(msg,font)
draw.text(((128/2-w/2),110), msg,(255,255,255,220), font=font, align='center')
draw.text(((128/2-w/2),110), msg,(255,255,255,220), font=font, align='center')
img = Image.alpha_composite(img, txt)

msg='65'
if int(msg) > 9:
    text_w=2
else:
    text_w=9
txt = Image.new('RGBA',img.size, (255,255,255,0))
font = ImageFont.truetype("font/PL.ttf", 40)
d = ImageDraw.Draw(txt)
w, h = draw.textsize(msg,font)
d.text((text_w,82), msg,(255,255,255,180), font=font)
img = Image.alpha_composite(img, txt)

img.save('sample-out.png')