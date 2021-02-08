import os
import sys
from PIL import Image, ImageDraw, ImageFont

# 상대경로를 절대경로로 변환
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# 시작말
print('확장자가 png인 사진만 가능합니다. 사진은 꼭 이 프로그램이 있는 폴더에 넣어 주세요.')

# 그라데이션 색 물어보기
def question():
    global gradientName
    gradientName = input("그라데이션 색을 골라 주세요.: ")

question()

# 사용자가 말한 그라데이션 색 파일 불러오기
# resource_path() 안에 경로를 써야 상대경로를 절대경로로 바꿔줌
#사용자가 여러번 틀려도 다시 비교할수있도록 while문을 사용
i = 0
while i < 1:

    if gradientName == 'black':
        gradientImg = Image.open(resource_path('./images/Gradient/' + gradientName + '.png'))
        print('그라데이션 색: ' + gradientName)
        print(gradientImg)
        break

    elif gradientName == 'blue':
        gradientImg = Image.open(resource_path('./images/Gradient/' + gradientName + '.png'))
        print('그라데이션 색: ' + gradientName)
        print(gradientImg)
        break

    elif gradientName == 'red':
        gradientImg = Image.open(resource_path('./images/Gradient/' + gradientName + '.png'))
        print('그라데이션 색: ' + gradientName)
        print(gradientImg)
        break

    elif gradientName == 'yellow':
        gradientImg = Image.open(resource_path('./images/Gradient/' + gradientName + '.png'))
        print('그라데이션 색: ' + gradientName)
        print(gradientImg)
        break

    # 사용자가 입력한게 black, blue, red, yellow 중에서 없으면 그라데이션 색을 물어보는 함수 다시 호출
    else:
        print('없는 그라데이션 색입니다.')
        question()
        continue

# 포지션 물어보기
def question3():
    global position
    position = input("포지션을 입력해 주세요. (FW, MF, DF, GK): ")

question3()

while i < 1:

    if position == 'FW' or position == 'MF' or position == 'DF' or position == 'GK':
        positionImg = Image.open(resource_path('./images/position/' + position + '.png'))
        print('포지션: ' + position)
        print(positionImg)
        break

    else:
        print('할 수 없는 포지션입니다.')
        question3()
        continue

#등번호 물어보기
def question2():
    global back_number
    back_number = int(input("등번호를 입력해 주세요. 1부터 99까지만 가능합니다.: "))

question2()

while i < 1:

    if back_number > 99:
        print('할 수 없는 등번호입니다.')
        question2()
        continue
    else:
        print('등번호: '+str(back_number))
        break

# 폰트 물어보기
def font():
    global font_name
    font_name = input("원하시는 폰트를 입력해 주세요. (PL1718~, oldPL, Serie2021, Laliga1819, Euro2020): ")

font()

while i < 1:

    if font_name == 'PL1718~' or font_name == 'oldPL' or font_name == 'Serie2021'\
            or font_name == 'Laliga1819' or font_name == 'Euro2020':
        if font_name == 'Serie2021':
            font_link = resource_path("font/" + font_name + ".otf")
        else:
            font_link = resource_path("font/" + font_name + ".ttf")

        print('폰트: ' + font_name)
        break

    else:
        print('없는 폰트입니다.')
        font()
        continue

# 선수 이름 물어보기
def player_name():
    global name
    name = input("선수 이름을 입력해 주세요. 한글도 가능: ")

player_name()

while i < 1:

    if name == '':
        print('선수 이름이 입력되지 않았습니다 다시 입력해 주세요.: ')
        player_name()
        continue

    else:
        print('선수 이름: '+name)
        break

#적용시킬 사진 이름 물어보기
def question4():
    global userImg_name
    userImg_name = input("적용시킬 사진 이름을 입력해 주세요.: ")

question4()

#사용자가 말한 사진이 있는지 확인하기
global userImg
while True:
    try:
        print('사진 이름: ' + userImg_name)
        userImg = Image.open(userImg_name + ".png")
        break
    except:
        print(userImg_name + '인 사진이 없거나 확장자가 png가 아닙니다. 다시 입력해 주세요.')
        question4()
        continue

#사용자가 말한 사진 크기 바꾸기
Xdim = 128
Ydim = 128
userImg = userImg.resize((int(Xdim), int(Ydim)))

# 크기를 바꾸고 resize라는 이름으로 저장하고 resize사진 열기
userImg.save("resize.png")
userImg = Image.open("resize.png")

# 그라데이션 사진이랑 포지션 사진을 사용자 사진과 합치기
userImg.paste(gradientImg, (0, 0), gradientImg)
userImg.paste(positionImg, (0, 0), positionImg)


if back_number > 9:
    text_w=2
else:
    text_w=9

if font_name == 'PL1718~':
    text_h = 82

elif font_name == 'oldPL':
    text_h = 89

elif font_name == 'Serie2021':
    text_h = 87

elif font_name == 'Laliga1819':
    text_h = 91

elif font_name == 'Euro2020':
    text_h = 81

txt = Image.new('RGBA',userImg.size, (255,255,255,0))
font = ImageFont.truetype(font_link, 40)
d = ImageDraw.Draw(txt)
d.text((text_w,text_h), str(back_number),(255,255,255,180), font=font)
userImg = Image.alpha_composite(userImg, txt)

txt = Image.new('RGBA',userImg.size, (255,255,255,0))
font = ImageFont.truetype(resource_path("font/Daum_SemiBold.ttf"), int(12.8))
draw = ImageDraw.Draw(txt)
w, h = draw.textsize(name,font)
draw.text(((128/2-w/2),110), name,(255,255,255,220), font=font, align='center')
draw.text(((128/2-w/2),110), name,(255,255,255,220), font=font, align='center')
userImg = Image.alpha_composite(userImg, txt)

def question5():
    global saveImg_name
    saveImg_name = input("저장될 사진의 이름을 정해 주세요.: ")
question5()

while i < 1:

    if saveImg_name == '':
        print('입력되지 않았습니다. 다시 입력해 주세요.')
        question5()
        continue
    else:
        print('저장될 사진 이름: '+saveImg_name)
        break

userImg.save(saveImg_name+'.png')