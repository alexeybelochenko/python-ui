import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QSize


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(QSize(1240, 640))
        self.setWindowIcon(QIcon('data/favicon.png'))
        self.title = "Atom Login"
        self.left = 10
        self.top = 10
        self.width = 1240
        self.height = 640
        self.initUI()
        self.InputLabels()
        self.LoginButton()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #create widget image
        label = QLabel(self)
        pixmap = QPixmap("data/image/darkly_logo_resize.png")
        label.setPixmap(pixmap)
        label.resize(600, 133)
        label.move(300, 130)

    def InputLabels(self):
        #create login textbox
        self.loginLabel = QLabel(self)
        self.loginLabel.setText('User Name:')
        self.loginInput = QLineEdit(self)
        self.loginInput.move(520, 400)
        self.loginInput.resize(200, 32)
        self.loginLabel.move(440, 400)
        self.loginInput.setPlaceholderText("Your login")

        #create password textboxValue
        self.passLabel = QLabel(self)
        self.passLabel.setText("Password:")
        self.passInput = QLineEdit(self)
        self.passInput.setEchoMode(QLineEdit.Password)
        self.passInput.move(520, 435)
        self.passInput.resize(200, 32)
        self.passLabel.move(440, 435)
        self.passInput.setPlaceholderText("Your password")

        self.wordLabel = QLabel(self)
        self.wordLabel.setText("Secret Word:")
        self.wordInput = QLineEdit(self)
        self.wordInput.setEchoMode(QLineEdit.Password)
        self.wordInput.move(520, 470)
        self.wordInput.resize(200, 32)
        self.wordLabel.move(440, 470)
        self.wordInput.setPlaceholderText('High-Level Permission Key')

    def LoginButton(self):
        self.button = QPushButton('Sign in', self)
        self.button.move(570, 520)
        #connect button to func on_click
        #button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
