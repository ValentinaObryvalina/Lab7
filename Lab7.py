'''from PIL import Image
img = Image.open("dog.jpeg")
img.show()
print(img.size, img.format, img.mode)


from PIL import Image
img = Image.open("dog.jpeg")
print(img.size)
img1 = img.resize((1200, 800))
img1.show()
img1.save("mdog.jpg")

converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.save("perev_dog.jpg")
converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
converted_img.save("r_dog.jpg")


from PIL import Image, ImageFilter
filenames = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

for file in filenames:
    with Image.open(file) as img:
        img.load()
        new_img = img.filter(ImageFilter.EDGE_ENHANCE)
        new_img.save("new_"+ file)


from PIL import Image
znak = "watermark.png"
with Image.open(znak) as img_znak:
    img_znak.load()

img_znak = Image.open(znak)
img_znak = img_znak.resize((img_znak.width // 2, img_znak.height // 2))

filename = "dog.jpeg"
with Image.open(filename) as img:
    img.load()

img.paste(img_znak, (200, 200))
img.save("znak_dog.jpeg")'''






