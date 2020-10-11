import json
from difflib import get_close_matches

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from glob2.fnmatch import translate
outputconvert = ""
itemconvert = ""
word = ""
data = json.load(open("./assets/data.json"))
yn = ""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 223)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 381, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 150, 51, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.submit)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton_2.clicked.connect(self.textBrowser.clear)
        self.pushButton_3.clicked.connect(self.exit1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "English Dictionary"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Enter a word:"))

        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
    def submit(self):
        global word
        global yn
        word = self.lineEdit.text()
        hello(word)
        try:
            self.textBrowser.append(f"{word} = {itemconvert}")
        except:
            self.textBrowser.setText(outputconvert)
        if yn == "N":
            self.textBrowser.append("word not found, please check spelling")
        else:
            pass
        print(yn)

    def checkdata(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("There Are No Photos To Make A Video!")
        msg.setIcon(self.QMessageBox.Critical)

        x = msg.exec_()



    def exit1(self):
        sys.exit(app.exec_())

        # self check code

def translate(w):
    global yn
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:

        yn = "Y"
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return  "The word doesn't exist. Please double check it."

        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

def hello(word):
    global itemconvert
    global outputconvert
    print(word)

    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
            itemconvert = item

    else:
        print(output)
        outputconvert = output



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('./assets/favicon.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())