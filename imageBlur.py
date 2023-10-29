from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


with Image.open("img_1.png") as pic_original:
    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('blured.jpg')
    pic_blured.show()