from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os

fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
x=50
y=50
r=100
g=100
b=100

img = Image.open("tadbeer-cv-template-1.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype(os.path.join(fonts_path, 'SansSerif.ttf'), 24)
draw.text((x, y),"Sample Text dfasddf dfa fda dfa fda dfa dfa fa dfa fasdfasdfasdf\nSample Text dfasddf dfa fda dfa fda dfa dfa fa dfa fasdfasdfasdf\nSample Text dfasddf dfa fda dfa fda dfa dfa fa dfa fasdfasdfasdf\nSample Text dfasddf dfa fda dfa fda dfa dfa fa dfa fasdfasdfasdf\nSample Text dfasddf dfa fda dfa fda dfa dfa fa dfa fasdfasdfasdf\nSample Text dfasddf dfa fda dfa fda dfa dfa fa dfa fasdfasdfasdf\nSample Text dfasddf dfa fda dfa fda dfa dfa fa dfa fasdfasdfasdf\nSample Text dfasddf dfa fda dfa fda dfa dfa fa dfa fasdfasdfasdf\nSample Text dfasddf dfa fda dfa fda dfa dfa fa dfa fasdfasdfasdf\n")

# draw.text((0, 0),"Sample Text",(255,255,255),font=font)
img.save('sample-out.png')