from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


with Image.open("img_1.png") as pic_original:
    pic_gray = pic_original.convert('L')
    pic_gray.save('gray.jpg')
    print("Зображення відкрито\nРозмір:", pic_gray.size)
    print("Формат:", pic_gray.format)
    print("Тип:", pic_gray.mode)
    pic_gray.show()