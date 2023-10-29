from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


with Image.open("img_1.png") as pic_original:
    print("Зображення відкрито\nРозмір:", pic_original.size)
    print("Формат:", pic_original.format)
    print("Тип:", pic_original.mode)
    pic_original.show()