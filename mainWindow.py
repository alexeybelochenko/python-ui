import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QInputDialog, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QSize


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(QSize(1240, 840))
        self.title = 'Atom Security Panel'
        self.left = 10
        self.top = 10
        self.width = 1240
        self.height = 860

        #init def
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('data/favicon.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.ImageButton()
        #self.openFileNameDialog()
        #self.saveFileDialog()

        self.button = QPushButton('PyQt5 button', self)
        self.button.setToolTip('This is an example button')
        self.button.move(100,70)
        self.button.clicked.connect(self.on_click)

    '''def ImageButton(self):
        button = QPushButton('Choose an image')
        button.move(50, 50)
        button.clicked.connect(self.on_click)'''



    def on_click(self):
        self.openFileNameDialog()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py);;PNG image (*.png);;JPG image(*.jpg)", options=options)
        if fileName:
            print(fileName)

    '''def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)'''






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
