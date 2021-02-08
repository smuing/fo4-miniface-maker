import os
from PIL import Image, ImageDraw, ImageFont
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QFileDialog, QRadioButton, QLabel, QVBoxLayout, QComboBox, QLineEdit, QMessageBox, QGroupBox, QGridLayout, QCheckBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def initUI(self):

        grid = QGridLayout()
        grid.addWidget(self.gradientGroup(), 0, 0)
        grid.addWidget(self.positionGroup(), 1, 0)
        grid.addWidget(self.backNumberGroup(), 0, 1)
        grid.addWidget(self.playerNameGroup(), 1, 1)
        grid.addWidget(self.saveInfoGroup(), 2, 0)
        grid.addWidget(self.saveBtn(), 2, 1)
        grid.addWidget(self.openwebBtn(), 2, 1)
        grid.addWidget(self.previewBtn(), 2, 2)

        self.setLayout(grid)

        self.setWindowIcon(QIcon(self.resource_path('./images/icon.png')))
        self.setWindowTitle('미니 페이스온')
        self.resize(480, 400)
        self.center()
        self.show()

    def gradientGroup(self):
        global black_btn1, blue_btn1, red_btn1, yellow_btn1, gradient_check, gradient_name

        groupbox = QGroupBox('그라데이션')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)
        groupbox.clicked.connect(lambda: self.gradientCheck(groupbox))
        gradient_check = groupbox.isChecked()

        black_btn1 = QRadioButton('Black')
        black_btn1.clicked.connect(self.gradientBtn)
        blue_btn1 = QRadioButton('Blue')
        blue_btn1.clicked.connect(self.gradientBtn)
        red_btn1 = QRadioButton('Red')
        red_btn1.clicked.connect(self.gradientBtn)
        yellow_btn1 = QRadioButton('Yellow')
        yellow_btn1.clicked.connect(self.gradientBtn)

        black_btn1.setChecked(True)
        gradient_name = 'black'

        vbox = QVBoxLayout()
        vbox.addWidget(black_btn1)
        vbox.addWidget(blue_btn1)
        vbox.addWidget(red_btn1)
        vbox.addWidget(yellow_btn1)
        groupbox.setLayout(vbox)

        return groupbox

    def positionGroup(self):
        global FW_btn2, MF_btn2, DF_btn2, GK_btn2, position_check, position_name

        groupbox = QGroupBox('포지션')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)
        groupbox.clicked.connect(lambda: self.positionCheck(groupbox))
        position_check = groupbox.isChecked()

        FW_btn2 = QRadioButton('FW')
        FW_btn2.clicked.connect(self.positionBtn)
        MF_btn2 = QRadioButton('MF')
        MF_btn2.clicked.connect(self.positionBtn)
        DF_btn2 = QRadioButton('DF')
        DF_btn2.clicked.connect(self.positionBtn)
        GK_btn2 = QRadioButton('GK')
        GK_btn2.clicked.connect(self.positionBtn)

        FW_btn2.setChecked(True)
        position_name = 'FW'

        vbox = QVBoxLayout()
        vbox.addWidget(FW_btn2)
        vbox.addWidget(MF_btn2)
        vbox.addWidget(DF_btn2)
        vbox.addWidget(GK_btn2)
        groupbox.setLayout(vbox)

        return groupbox

    def backNumberGroup(self):
        global f1btn4, f2btn4, f3btn4, f4btn4, B_F_check, font_name, back_number
        back_number = ''

        groupbox = QGroupBox('등번호 | 폰트')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)
        groupbox.clicked.connect(lambda: self.B_FCheck(groupbox))
        B_F_check = groupbox.isChecked()

        back_num = QLineEdit(self)
        back_num.setMaxLength(2)
        back_num.setPlaceholderText('!숫자만 입력!')
        back_num.textChanged.connect(self.back)

        f1btn4 = QRadioButton('PL1718~')
        f1btn4.clicked.connect(self.userFont)
        f2btn4 = QRadioButton('oldPL')
        f2btn4.clicked.connect(self.userFont)
        f3btn4 = QRadioButton('Serie2021')
        f3btn4.clicked.connect(self.userFont)
        f4btn4 = QRadioButton('Laliga1819')
        f4btn4.clicked.connect(self.userFont)

        f1btn4.setChecked(True)
        font_name = 'PL1718~'

        vbox = QVBoxLayout()
        vbox.addWidget(back_num)
        vbox.addWidget(f1btn4)
        vbox.addWidget(f2btn4)
        vbox.addWidget(f3btn4)
        vbox.addWidget(f4btn4)
        groupbox.setLayout(vbox)

        return groupbox

    def playerNameGroup(self):
        global player_check, name
        name = ''

        groupbox = QGroupBox('선수 이름')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)
        groupbox.clicked.connect(lambda: self.playerCheck(groupbox))
        player_check = groupbox.isChecked()

        qle5 = QLineEdit(self)
        qle5.setMaxLength(18)
        qle5.setPlaceholderText('!최대 18글자! (한글도OK)')
        qle5.textChanged[str].connect(self.player_name)

        vbox = QVBoxLayout()
        vbox.addWidget(qle5)
        groupbox.setLayout(vbox)

        return groupbox

    def saveInfoGroup(self):
        global saveImg_name
        saveImg_name = ''
        groupbox = QGroupBox('저장 설정')

        btn1 = QPushButton("적용할 이미지", self)
        btn1.move(20, 220)
        btn1.clicked.connect(self.openFileNameDialog)

        qle6 = QLineEdit(self)
        qle6.move(140, 255)
        qle6.setPlaceholderText('!저장될 이미지 이름!')
        qle6.textChanged.connect(self.save_name)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(qle6)
        groupbox.setLayout(vbox)

        return groupbox

    def saveBtn(self):
        save_btn = QPushButton("저장하기", self)
        save_btn.setGeometry(243, 284, 227, 77)
        save_btn.clicked.connect(self.save)

    def openwebBtn(self):
        global web
        web = QWebEngineView()
        web.setWindowIcon(QIcon(self.resource_path('./images/icon.png')))
        web.setWindowTitle("자동미페제작 사용법")
        web.resize(1000,900)
        web_btn =QPushButton("사용법 보기", self)
        web_btn.setGeometry(243, 363, 112, 25)
        web_btn.clicked.connect(self.openweb)

    def previewBtn(self):
        preview_btn = QPushButton("미리보기", self)
        preview_btn.setGeometry(358, 363, 112, 25)
        preview_btn.clicked.connect(self.preview)

    def openweb(self):
        web.load(QUrl("https://www.fmkorea.com/?mid=game_fifa&category=1059687763&document_srl=3375602511"))
        web.show()


    def openFileNameDialog(self):
        global userImg, prevImg

        fileName, _ = QFileDialog.getOpenFileName(self, "적용할 이미지를 선택하세요.", "",
                                                  "PNG Files (*.png)")

        if fileName:
            userImg = Image.open(fileName)
            prevImg = Image.open(fileName)
            Xdim = 128
            Ydim = 128
            userImg = userImg.resize((int(Xdim), int(Ydim)))
            prevImg = userImg.resize((int(Xdim), int(Ydim)))
            userImg.save("resize.png")
            prevImg.save("preview.png")

    def gradientCheck(self, groupbox):
        global gradient_check
        gradient_check = groupbox.isChecked()

    def gradientBtn(self):
        global gradient_name
        if black_btn1.isChecked():
            gradient_name = 'Black'
        elif blue_btn1.isChecked():
            gradient_name = 'Blue'
        elif red_btn1.isChecked():
            gradient_name = 'Red'
        elif yellow_btn1.isChecked():
            gradient_name = 'Yellow'

        print(gradient_name)

    def positionCheck(self, groupbox):
        global position_check
        position_check = groupbox.isChecked()

    def positionBtn(self):
        global position_name
        if FW_btn2.isChecked():
            position_name = 'FW'
        elif MF_btn2.isChecked():
            position_name = 'MF'
        elif DF_btn2.isChecked():
            position_name = 'DF'
        elif GK_btn2.isChecked():
            position_name = 'GK'

        print(position_name)

    def B_FCheck(self, groupbox):
        global B_F_check
        B_F_check = groupbox.isChecked()

    def userFont(self):
        global font_name, font_link

        if f1btn4.isChecked():
            font_name = 'PL1718~'
        elif f2btn4.isChecked():
            font_name = 'oldPL'
        elif f3btn4.isChecked():
            font_name = 'Serie2021'
        elif f4btn4.isChecked():
            font_name = 'Laliga1819'

        print(font_name)

    def back(self, text):
        global back_number
        back_number = text

        print(back_number)

    def playerCheck(self, groupbox):
        global player_check
        player_check = groupbox.isChecked()

    def player_name(self, text):
        global name
        name = text

        print(name)

    def save_name(self, text):
        global saveImg_name
        saveImg_name = text

        print(saveImg_name)

    def preview(self):
        try:
            prevImg = Image.open("preview.png")
        except:
            QMessageBox.critical(self, 'Message', '적용할 이미지를 선택해 주세요.',
                                     QMessageBox.Yes)
            return
        print(gradient_check)
        if str(gradient_check) == 'True':
            gradientImg = Image.open(self.resource_path('./images/Gradient/' + gradient_name + '.png'))
            print(gradientImg)
            print(gradient_name)
            prevImg.paste(gradientImg, (0, 0), gradientImg)

        if str(position_check) == 'True':
            positionImg = Image.open(self.resource_path('./images/position/' + position_name + '.png'))
            prevImg.paste(positionImg, (0, 0), positionImg)
            print(positionImg)
            print(position_name)

        if str(B_F_check) == 'True':

            if font_name == 'PL1718~' or font_name == 'oldPL' or font_name == 'Laliga1819' or font_name == 'Euro2020':
                font_link = self.resource_path("font/" + font_name + ".ttf")
            else:
                font_link = self.resource_path("font/" + font_name + ".otf")

            if back_number == '':
                QMessageBox.critical(self, 'Message', "등번호를 입력하거나 '등번호 | 폰트' 탭에 체크를 해제해 주세요.",
                                     QMessageBox.Yes)
                return
            else:
                if int(back_number) > 9:
                    text_w = 2
                else:
                    text_w = 9
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
                txt = Image.new('RGBA', prevImg.size, (255, 255, 255, 0))
                fontstyle = ImageFont.truetype(font_link, 40)
                d = ImageDraw.Draw(txt)
                d.text((text_w, text_h), str(back_number), (255, 255, 255, 180), font=fontstyle)
                prevImg = Image.alpha_composite(prevImg, txt)

        if str(player_check) == 'True':
            if str(name) == '':
                QMessageBox.critical(self, 'Message', "선수 이름을 입력하거나 '선수 이름' 탭에 체크를 해제해 주세요.",
                                     QMessageBox.Yes)
                return
            else:
                if 'a' <= name[0] <= "z" or 'A' <= name[0] <= 'Z':
                    print("It is an alphabet")
                    fontSize = int(12.8)
                else:
                    print("It is not an alphabet")
                    fontSize = int(10)

                txt = Image.new('RGBA', prevImg.size, (255, 255, 255, 0))
                font = ImageFont.truetype(self.resource_path("font/Daum_SemiBold.ttf"), fontSize)
                draw = ImageDraw.Draw(txt)
                w, h = draw.textsize(name, font)
                draw.text(((128 / 2 - w / 2), 110), name, (255, 255, 255, 220), font=font, align='center')
                draw.text(((128 / 2 - w / 2), 110), name, (255, 255, 255, 220), font=font, align='center')
                prevImg = Image.alpha_composite(prevImg, txt)

        prevImg.show()

    def save(self):
        if saveImg_name == '':
            QMessageBox.critical(self, 'Message', '저장될 이미지의 이름을 입력해 주세요.',
                                 QMessageBox.Yes)
            return
        else:
            if saveImg_name == 'resize':
                QMessageBox.critical(self, 'Message', '다른 이름을 입력해 주세요.',
                                     QMessageBox.Yes)
                return
            elif saveImg_name == 'preview':
                QMessageBox.critical(self, 'Message', '다른 이름을 입력해 주세요.',
                                     QMessageBox.Yes)
                return
            else:
                try:
                    userImg = Image.open("resize.png")
                except:
                    QMessageBox.critical(self, 'Message', '적용할 이미지를 선택해 주세요.',
                                        QMessageBox.Yes)
                    return
        print(gradient_check)
        if str(gradient_check) == 'True':
            gradientImg = Image.open(self.resource_path('./images/Gradient/' + gradient_name + '.png'))
            print(gradientImg)
            print(gradient_name)
            userImg.paste(gradientImg, (0, 0), gradientImg)

        if str(position_check) == 'True':
            positionImg = Image.open(self.resource_path('./images/position/' + position_name + '.png'))
            userImg.paste(positionImg, (0, 0), positionImg)
            print(positionImg)
            print(position_name)

        if str(B_F_check) == 'True':

            if font_name == 'PL1718~' or font_name == 'oldPL' or font_name == 'Laliga1819' or font_name == 'Euro2020':
                font_link = self.resource_path("font/" + font_name + ".ttf")
            else:
                font_link = self.resource_path("font/" + font_name + ".otf")

            if back_number == '':
                QMessageBox.critical(self, 'Message', "등번호를 입력하거나 '등번호 | 폰트' 탭에 체크를 해제해 주세요.",
                                     QMessageBox.Yes)
                return
            else:
                if int(back_number) > 9:
                    text_w = 2
                else:
                    text_w = 9
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
                txt = Image.new('RGBA', userImg.size, (255, 255, 255, 0))
                fontstyle = ImageFont.truetype(font_link, 40)
                d = ImageDraw.Draw(txt)
                d.text((text_w, text_h), str(back_number), (255, 255, 255, 180), font=fontstyle)
                userImg = Image.alpha_composite(userImg, txt)

        if str(player_check) == 'True':
            if str(name) == '':
                QMessageBox.critical(self, 'Message', "선수 이름을 입력하거나 '선수 이름' 탭에 체크를 해제해 주세요.",
                                     QMessageBox.Yes)
                return
            else:
                if 'a' <= name[0] <= "z" or 'A' <= name[0] <= 'Z':
                    print("It is an alphabet")
                    fontSize = int(12.8)
                else:
                    print("It is not an alphabet")
                    fontSize = int(10)

                txt = Image.new('RGBA', userImg.size, (255, 255, 255, 0))
                font = ImageFont.truetype(self.resource_path("font/Daum_SemiBold.ttf"), fontSize)
                draw = ImageDraw.Draw(txt)
                w, h = draw.textsize(name, font)
                draw.text(((128 / 2 - w / 2), 110), name, (255, 255, 255, 220), font=font, align='center')
                draw.text(((128 / 2 - w / 2), 110), name, (255, 255, 255, 220), font=font, align='center')
                userImg = Image.alpha_composite(userImg, txt)

        if saveImg_name == '':
            QMessageBox.critical(self, 'Message', '저장될 이미지의 이름을 입력해 주세요.',
                                 QMessageBox.Yes)
            return
        else:
            if saveImg_name == 'resize':
                QMessageBox.critical(self, 'Message', '다른 이름을 입력해 주세요.',
                                     QMessageBox.Yes)
                return
            elif saveImg_name == 'preview':
                QMessageBox.critical(self, 'Message', '다른 이름을 입력해 주세요.',
                                     QMessageBox.Yes)
                return
            else:
                userImg.save(saveImg_name + '.png')
                userImg.show()
                os.remove('resize.png')
                os.remove('preview.png')




    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())