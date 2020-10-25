import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("Timer application")
    app.exec_()
