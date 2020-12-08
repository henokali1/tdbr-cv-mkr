from PIL import Image, ImageDraw, ImageFont

def mk_grid():
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

x=1150
y=560
txt_loc = {
    'name':(1150, 558),
    'passport_no':(1150, 620),
    'place_of_issue':(1150, 690),
    'nationality':(1150, 750),
    'religion':(1150, 820),
    'date_of_birth':(1150, 880),
    'place_of_birth':(1150, 940),
    'marital_status':(1150, 1010),
    'height':(1150, 1070),
    'weight':(1150, 1135),
    'country':(905, 1320),
    'period':(1260, 1320),
    'no_of_kids':(1145, 1690),
}

img = Image.open('tadbeer-cv-template/tadbeer-cv-template-1.jpg')
d1 = ImageDraw.Draw(img)
font = ImageFont.truetype('fonts/FreeMonoBold.ttf', 28)

full_name='HENOK ALI UMER'
passport_no = 'EP3958734'
place_of_issue = 'PLACE OF ISSUE'
nationality = 'ETHIOPIAN'
religion = 'RELIGION'
date_of_birth = '30-12-1993'
place_of_birth = 'PLACE OF BIRTH'
marital_status = 'MARITAL STATUS'
height = '174cm'
weight = '73Kg'
country = 'U.A.E'
period = '5 YEARS'
no_of_kids = '3'

d1.text(txt_loc['name'], full_name, fill=(255, 0, 0), font=font)
d1.text(txt_loc['passport_no'], passport_no, fill=(255, 0, 0), font=font)
d1.text(txt_loc['place_of_issue'], place_of_issue, fill=(255, 0, 0), font=font)
d1.text(txt_loc['nationality'], nationality, fill=(255, 0, 0), font=font)
d1.text(txt_loc['religion'], religion, fill=(255, 0, 0), font=font)
d1.text(txt_loc['date_of_birth'], date_of_birth, fill=(255, 0, 0), font=font)
d1.text(txt_loc['place_of_birth'], place_of_birth, fill=(255, 0, 0), font=font)
d1.text(txt_loc['marital_status'], marital_status, fill=(255, 0, 0), font=font)
d1.text(txt_loc['height'], height, fill=(255, 0, 0), font=font)
d1.text(txt_loc['weight'], weight, fill=(255, 0, 0), font=font)
d1.text(txt_loc['country'], country, fill=(255, 0, 0), font=font)
d1.text(txt_loc['period'], period, fill=(255, 0, 0), font=font)
d1.text(txt_loc['no_of_kids'], no_of_kids, fill=(255, 0, 0), font=font)

img.show()
img.save("out/1.jpg")