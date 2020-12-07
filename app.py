# from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw 
# import os

# fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
# x=500
# y=500
# r=100
# g=100
# b=100

# img = Image.open("tadbeer-cv-template-1.jpg")
# draw = ImageDraw.Draw(img)
# # font = ImageFont.truetype(os.path.join(fonts_path, 'fonts/SansSerif.ttf'), 24)
# font = ImageFont.truetype('fonts/SansSerif.ttf', 24)
# # draw.text((x, y),"Sample Text")

# draw.text((0, 0),"Sample Text adsfasdf asdfasd fsadf asdf asdf asfd asdf asdfa sdf",(255,255,255),font=font)
# img.save('sample-out.jpg')

from PIL import Image, ImageDraw, ImageFont

img = Image.open('tadbeer-cv-template-1.jpg')
d1 = ImageDraw.Draw(img)
font = ImageFont.truetype('FreeMono.ttf', 44)


d1.text((28, 36), "Hello, TutorialsPoint!", fill=(255, 0, 0), font=font)
img.show()
img.save("image_text.jpg")
