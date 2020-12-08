from PIL import Image, ImageDraw, ImageFont

img = Image.open('tadbeer-cv-template/tadbeer-cv-template-1.jpg')
d1 = ImageDraw.Draw(img)
font = ImageFont.truetype('fonts/FreeMono.ttf', 20)

width, height = img.size
print(f'width: {width}, height: {height}')
for x in range(0,width, 80):
    for y in range(0, height, 20):
        d1.text((x, y), f'{int(x/10)},{int(y/10)}', fill=(255, 0, 0), font=font)
img.show()
img.save("out/grid.jpg")
