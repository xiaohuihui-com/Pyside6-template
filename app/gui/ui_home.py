# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(976, 663)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    color: white;\n"
"}\n"
"\n"
"#appBox {\n"
"    background-color: qlineargradient(x0:0,\n"
"    y0: 1,\n"
"    x1: 1,\n"
"    y1: 1,\n"
"    stop: 0.4 rgb(107, 128, 210),\n"
"    stop: 1 rgb(180, 140, 255));\n"
"    border: 2px solid #02a6b5;\n"
"    border-radius: 30px\n"
"}\n"
"\n"
"#center *{\n"
"    background-color: qlineargradient(x0:0,\n"
"    y0: 1,\n"
"    x1: 1,\n"
"    y1: 1,\n"
"    stop: 0.4 rgb(107, 128, 210),\n"
"    stop: 1 rgb(180, 140, 255));\n"
"    border: 1px solid white;\n"
"}\n"
"#bottom .QPushButton {\n"
"	border: 2px solid white;\n"
"    border-radius: 15px;\n"
"	text-align: center;\n"
"}\n"
"#bottom .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottom .QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#top .QPushButton {\n"
"	border: 2px solid white;\n"
"    border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"#top QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
""
                        "}\n"
"#top QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.appBox = QFrame(self.centralwidget)
        self.appBox.setObjectName(u"appBox")
        self.appBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.appBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.appBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.appBox)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 50))
        self.top.setMaximumSize(QSize(16777215, 50))
        self.top.setFrameShape(QFrame.Shape.NoFrame)
        self.top.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.top)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 0, 6, 0)
        self.t_logoframe = QFrame(self.top)
        self.t_logoframe.setObjectName(u"t_logoframe")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_logoframe.sizePolicy().hasHeightForWidth())
        self.t_logoframe.setSizePolicy(sizePolicy)
        self.t_logoframe.setMinimumSize(QSize(50, 50))
        self.t_logoframe.setMaximumSize(QSize(50, 50))
        self.t_logoframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.t_logoframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.t_logoframe)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.t_logoframe)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(45, 45))
        self.frame.setMaximumSize(QSize(45, 45))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout_8.addWidget(self.t_logoframe)

        self.t_titleframe = QFrame(self.top)
        self.t_titleframe.setObjectName(u"t_titleframe")
        self.t_titleframe.setFrameShape(QFrame.Shape.NoFrame)
        self.t_titleframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.t_titleframe)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.t_titleframe)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 45))
        self.label.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_8.addWidget(self.t_titleframe)

        self.frame_2 = QFrame(self.top)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 25))
        self.frame_3.setMaximumSize(QSize(16777215, 25))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 25))
        self.frame_7.setMaximumSize(QSize(16777215, 25))
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton_2.setFont(font2)

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 25))
        self.pushButton_3.setFont(font2)

        self.horizontalLayout_7.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 25))
        self.pushButton.setFont(font2)

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout.addWidget(self.top)

        self.center = QFrame(self.appBox)
        self.center.setObjectName(u"center")
        self.center.setFrameShape(QFrame.Shape.NoFrame)
        self.center.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.center)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(6, 6, 6, 6)
        self.content = QFrame(self.center)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.content)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.content)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.p1 = QWidget()
        self.p1.setObjectName(u"p1")
        self.horizontalLayout_13 = QHBoxLayout(self.p1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_6 = QLabel(self.p1)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(60)
        self.label_6.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_6)

        self.stackedWidget_3.addWidget(self.p1)
        self.p2 = QWidget()
        self.p2.setObjectName(u"p2")
        self.horizontalLayout_17 = QHBoxLayout(self.p2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_7 = QLabel(self.p2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.stackedWidget_3.addWidget(self.p2)
        self.p3 = QWidget()
        self.p3.setObjectName(u"p3")
        self.horizontalLayout_16 = QHBoxLayout(self.p3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.p3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.horizontalLayout_16.addWidget(self.label_8)

        self.stackedWidget_3.addWidget(self.p3)
        self.p4 = QWidget()
        self.p4.setObjectName(u"p4")
        self.horizontalLayout_15 = QHBoxLayout(self.p4)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_4 = QLabel(self.p4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.horizontalLayout_15.addWidget(self.label_4)

        self.stackedWidget_3.addWidget(self.p4)
        self.p5 = QWidget()
        self.p5.setObjectName(u"p5")
        self.horizontalLayout_14 = QHBoxLayout(self.p5)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.p5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.horizontalLayout_14.addWidget(self.label_5)

        self.stackedWidget_3.addWidget(self.p5)

        self.horizontalLayout_11.addWidget(self.stackedWidget_3)


        self.horizontalLayout_12.addWidget(self.content)


        self.verticalLayout.addWidget(self.center)

        self.bottom = QFrame(self.appBox)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 40))
        self.bottom.setMaximumSize(QSize(16777215, 40))
        self.bottom.setFrameShape(QFrame.Shape.NoFrame)
        self.bottom.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.bottom)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.toogleframe = QFrame(self.bottom)
        self.toogleframe.setObjectName(u"toogleframe")
        self.toogleframe.setFrameShape(QFrame.Shape.NoFrame)
        self.toogleframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.toogleframe)
        self.horizontalLayout_9.setSpacing(30)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(30, 0, 30, 0)
        self.btn1 = QPushButton(self.toogleframe)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMinimumSize(QSize(0, 40))
        self.btn1.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.btn1.setFont(font4)

        self.horizontalLayout_9.addWidget(self.btn1)

        self.btn2 = QPushButton(self.toogleframe)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(0, 40))
        self.btn2.setMaximumSize(QSize(16777215, 40))
        self.btn2.setFont(font4)

        self.horizontalLayout_9.addWidget(self.btn2)

        self.btn3 = QPushButton(self.toogleframe)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMinimumSize(QSize(0, 40))
        self.btn3.setMaximumSize(QSize(16777215, 40))
        self.btn3.setFont(font4)

        self.horizontalLayout_9.addWidget(self.btn3)

        self.btn4 = QPushButton(self.toogleframe)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setMinimumSize(QSize(0, 40))
        self.btn4.setMaximumSize(QSize(16777215, 40))
        self.btn4.setFont(font4)

        self.horizontalLayout_9.addWidget(self.btn4)

        self.btn5 = QPushButton(self.toogleframe)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setMinimumSize(QSize(0, 40))
        self.btn5.setMaximumSize(QSize(16777215, 40))
        self.btn5.setFont(font4)

        self.horizontalLayout_9.addWidget(self.btn5)


        self.horizontalLayout_10.addWidget(self.toogleframe)

        self.horizontalLayout_10.setStretch(0, 1)

        self.verticalLayout.addWidget(self.bottom)


        self.horizontalLayout.addWidget(self.appBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u56db\u5ddd\u7701\u4e2d\u5c0f\u578b\u6c34\u5e93\u5927\u575d\u667a\u80fd\u4e2d\u5fc3\u7ad9", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"2025-3-20 10:10:55", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9898", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7b2c1\u9875", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u7b2c2\u9875", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u7b2c3\u9875", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7b2c4\u9875", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7b2c5\u9875", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u9996\u9875", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u7ad9\u6570\u636e", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u63a7\u5236", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u7ba1\u7406", None))
        self.btn5.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u7ba1\u7406", None))
    # retranslateUi

