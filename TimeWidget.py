from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QObject, QThread, Signal, Slot
from TimeWidget_ui import Ui_TimeWidget
from datetime import datetime
import time
from threading import Lock


class TimeDisplayer(QObject):
    timeUpdated = Signal(str)
    run = False

    def __init__(self, parent=None):
        super(TimeDisplayer, self).__init__(parent)
        self.lock = Lock()

    def run(self):
        self.run = True
        while self.run:
            self.lock.acquire()
            now = datetime.now()
            self.timeUpdated.emit(now.strftime("%H %M %S"))
            time.sleep(0.2)
            now = datetime.now()
            self.timeUpdated.emit(now.strftime("%H:%M:%S"))
            self.lock.release()
            time.sleep(0.8)

    @Slot()
    def stop(self):
        self.lock.acquired()
        self.run = False
        self.lock.release()


class TimeWidget(QWidget, Ui_TimeWidget):
    def __init__(self, parent=None):
        super(TimeWidget, self).__init__(parent)
        self.setupUi(self)
        self.btnStart.clicked.connect(self.start)
        self.btnStop.clicked.connect(self.stop)
        self.setupThread()
        self.show()

    def setupThread(self):
        self.worker = TimeDisplayer()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.worker.timeUpdated.connect(self.lblTime.setText)
        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.worker.stop)

    def start(self):
        self.thread.start()

    def stop(self):
        self.thread.quit()
