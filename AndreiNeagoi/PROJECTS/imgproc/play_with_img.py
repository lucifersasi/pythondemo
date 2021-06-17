
from PIL import Image, ImageFilter

pika = Image.open('pokedex/pikachu.jpg')
bulbasaur = Image.open('pokedex/bulbasaur.jpg')
# print(img)

# methods
# filtered_img = pika.filter(ImageFilter.BLUR) # we get smooth, sharpen etc.
# converted_img = pika.convert("L") # this converts into grey scale
# rotated_img = pika.rotate(90)
# resize = bulbasaur.resize((50,50))

# box = (10,10,100,100)
# part = bulbasaur.crop(box)

pika.thumbnail((100,100)) # doesn't get stretched out and loose quality intelligent best resolution finder
pika.save("thumbnail.png", 'png')
print(pika.size)

#saves
# filtered_img.save("blur.png", 'png')
# converted_img.save("grey.jpg", 'jpeg')



#shows
# PIL.ImageShow.show(filtered_img)
# converted_img.show()
# rotated_img.show()
# resize.show()
# part.show()
pika.show()