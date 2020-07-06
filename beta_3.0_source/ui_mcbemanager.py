# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mcbemanager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_McBeServerManager(object):
    def setupUi(self, McBeServerManager):
        if not McBeServerManager.objectName():
            McBeServerManager.setObjectName(u"McBeServerManager")
        McBeServerManager.resize(526, 305)
        self.centralwidget = QWidget(McBeServerManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.version = QLabel(self.centralwidget)
        self.version.setObjectName(u"version")
        self.version.setGeometry(QRect(480, 290, 41, 9))
        self.Icon = QPushButton(self.centralwidget)
        self.Icon.setObjectName(u"Icon")
        self.Icon.setGeometry(QRect(0, 254, 51, 51))
        icon = QIcon()
        icon.addFile(u"../z001/ss/dev/minecraft.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.Icon.setIcon(icon)
        self.pbtn_st = QPushButton(self.centralwidget)
        self.pbtn_st.setObjectName(u"pbtn_st")
        self.pbtn_st.setGeometry(QRect(1, 2, 521, 41))
        self.pbtn_sc = QPushButton(self.centralwidget)
        self.pbtn_sc.setObjectName(u"pbtn_sc")
        self.pbtn_sc.setGeometry(QRect(0, 50, 521, 41))
        self.pbtn_lv = QPushButton(self.centralwidget)
        self.pbtn_lv.setObjectName(u"pbtn_lv")
        self.pbtn_lv.setGeometry(QRect(0, 150, 521, 41))
        self.update_t = QLabel(self.centralwidget)
        self.update_t.setObjectName(u"update_t")
        self.update_t.setGeometry(QRect(470, 250, 51, 16))
        self.update_1 = QLabel(self.centralwidget)
        self.update_1.setObjectName(u"update_1")
        self.update_1.setGeometry(QRect(470, 270, 41, 9))
        self.pbtn_svst = QPushButton(self.centralwidget)
        self.pbtn_svst.setObjectName(u"pbtn_svst")
        self.pbtn_svst.setGeometry(QRect(0, 100, 521, 41))
        McBeServerManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(McBeServerManager)

        QMetaObject.connectSlotsByName(McBeServerManager)
    # setupUi

    def retranslateUi(self, McBeServerManager):
        McBeServerManager.setWindowTitle(QCoreApplication.translate("McBeServerManager", u"Minecraft Bedrock Editon Server Manager", None))
        self.version.setText(QCoreApplication.translate("McBeServerManager", u"Beta 3.0", None))
        self.Icon.setText("")
        self.pbtn_st.setText(QCoreApplication.translate("McBeServerManager", u"\u542f\u52a8\u670d\u52a1\u5668", None))
        self.pbtn_sc.setText(QCoreApplication.translate("McBeServerManager", u"\u542f\u52a8command\u4ee5\u5bf9\u670d\u52a1\u5668\u8fdb\u884c\u66f4\u590d\u6742\u7684\u64cd\u4f5c", None))
        self.pbtn_lv.setText(QCoreApplication.translate("McBeServerManager", u"\u9000\u51fa\u8f6f\u4ef6", None))
        self.update_t.setText(QCoreApplication.translate("McBeServerManager", u"\u66f4\u65b0\u65e5\u5fd7\uff1a", None))
        self.update_1.setText(QCoreApplication.translate("McBeServerManager", u"\u5185\u6838\u66f4\u6362", None))
        self.pbtn_svst.setText(QCoreApplication.translate("McBeServerManager", u"\u670d\u52a1\u5668\u8bbe\u7f6e", None))
    # retranslateUi

