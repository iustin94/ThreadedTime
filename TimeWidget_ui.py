# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TimeWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TimeWidget(object):
    def setupUi(self, TimeWidget):
        if not TimeWidget.objectName():
            TimeWidget.setObjectName(u"TimeWidget")
        TimeWidget.resize(377, 300)
        self.label = QLabel(TimeWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 60, 91, 17))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.lblTime = QLabel(TimeWidget)
        self.lblTime.setObjectName(u"lblTime")
        self.lblTime.setGeometry(QRect(80, 130, 211, 51))
        font1 = QFont()
        font1.setFamily(u"FreeMono")
        font1.setPointSize(30)
        self.lblTime.setFont(font1)
        self.lblTime.setAlignment(Qt.AlignCenter)
        self.btnStart = QPushButton(TimeWidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(70, 220, 95, 27))
        self.btnStop = QPushButton(TimeWidget)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setGeometry(QRect(230, 220, 95, 27))

        self.retranslateUi(TimeWidget)

        QMetaObject.connectSlotsByName(TimeWidget)
    # setupUi

    def retranslateUi(self, TimeWidget):
        TimeWidget.setWindowTitle(QCoreApplication.translate("TimeWidget", u"TimeWidget", None))
        self.label.setText(QCoreApplication.translate("TimeWidget", u"Time is:", None))
        self.lblTime.setText(QCoreApplication.translate("TimeWidget", u"00:00", None))
        self.btnStart.setText(QCoreApplication.translate("TimeWidget", u"Start", None))
        self.btnStop.setText(QCoreApplication.translate("TimeWidget", u"Stop", None))
    # retranslateUi

