import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
files = os.listdir("photoTools")
for photo in files:
    with Image.open("photoTools/"+photo) as image:

        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("fonts/Inter-Regular.otf", 30)

        draw.text((10,10), "Top 3 popular freddy", font=font, fill="white")

        image.save("result/"+photo)