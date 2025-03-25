import darkdetect
from PySide6.QtCore import Qt, Signal, QEvent, QTimer, QPoint, QRectF
from PySide6.QtGui import QColor, QPen, QPainter, QLinearGradient
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGraphicsBlurEffect, \
    QScrollArea

from app.common.database import DBInitializer, DatabaseThread
from app.common.style_sheet import Theme, StyleSheet
from app.common.utils import apply_shadow_effect, CustomGrip


class ToogleButton(QPushButton):
    def __init__(self):
        super(ToogleButton, self).__init__()
        self.btn_state = "on"
        self.setFixedSize(60, 20)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(Qt.NoPen)
        painter.setPen(pen)

        if self.btn_state == "on":
            painter.setBrush(QColor(96, 202, 91))
            rect = QRectF(0, 0, self.width(), self.height())
            painter.drawRoundedRect(rect, self.height() / 2, self.height() / 2)

            painter.setBrush(Qt.white)
            rect = QRectF(self.width() / 2 - 5, 5, self.width() / 2, self.height() - 5 * 2)
            painter.drawRoundedRect(rect, (self.height() - 5 * 2) / 2, (self.height() - 5 * 2) / 2)

        else:
            painter.setBrush(QColor(220, 220, 220))
            rect = QRectF(0, 0, self.width(), self.height())
            painter.drawRoundedRect(rect, self.height() / 2, self.height() / 2)

            painter.setBrush(Qt.white)
            rect = QRectF(5, 5, self.width() / 2, self.height() - 5 * 2)
            painter.drawRoundedRect(rect, (self.height() - 5 * 2) / 2, (self.height() - 5 * 2) / 2)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
            if self.btn_state == "on":
                self.btn_state = "off"
            else:
                self.btn_state = "on"


class TopFrame(QFrame):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("top_frame")
        StyleSheet.TOP_FRAME.apply(self)

        self.__initWindow()

    def __initWindow(self):
        self.setFixedHeight(60)
        self.setMinimumWidth(800)
        self.__initWidget()
        self.__initLayout()

    def __initWidget(self):
        self.title = QLabel("四川省中小型水库大坝智能中心站", self)
        self.title.setObjectName("title")
        self.time = QLabel("2058-10-10 00:00:00", self)
        self.time.setObjectName("time")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn_minimize = ToogleButton()
        self.btn_minimize.setCheckable(True)
        self.btn_maximize = QPushButton('Maximize', self)
        self.btn_close = QPushButton('Close', self)
        self.btn_minimize.setFixedHeight(30)
        self.btn_maximize.setFixedHeight(30)
        self.btn_close.setFixedHeight(30)

    def __initLayout(self):
        self.hbox = QHBoxLayout(self)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setSpacing(0)
        self.top_right_layout = QHBoxLayout()
        self.top_right_layout.addWidget(self.btn_minimize)
        self.top_right_layout.addWidget(self.btn_maximize)
        self.top_right_layout.addWidget(self.btn_close)
        self.top_right_layout.setContentsMargins(0, 0, 0, 0)
        self.top_right_layout.setSpacing(0)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.time)
        self.vbox.addLayout(self.top_right_layout)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setSpacing(0)

        self.hbox.addWidget(self.title, 1, Qt.AlignmentFlag.AlignCenter)
        self.hbox.addLayout(self.vbox)


class BottomFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("bottom_frame")
        StyleSheet.BOTTOM_FRAME.apply(self)
        self.__initWindow()

    def __initWindow(self):
        self.setFixedHeight(45)
        self.__initWidget()
        self.__initLayout()

    def __initWidget(self):
        self.btn1 = QPushButton("按钮1")
        self.btn2 = QPushButton("按钮2")
        self.btn3 = QPushButton("按钮3")
        self.btn4 = QPushButton("按钮4")
        self.btn5 = QPushButton("按钮5")
        self.btn1.setFixedHeight(42)
        self.btn2.setFixedHeight(42)
        self.btn3.setFixedHeight(42)
        self.btn4.setFixedHeight(42)
        self.btn5.setFixedHeight(42)

    def __initLayout(self):
        self.hbox = QHBoxLayout(self)
        self.hbox.setContentsMargins(30, 0, 30, 0)
        self.hbox.setSpacing(30)
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)
        self.hbox.addWidget(self.btn3)
        self.hbox.addWidget(self.btn4)
        self.hbox.addWidget(self.btn5)


class Example(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setContentsMargins(6, 6, 6, 6)
        self.setObjectName("main")
        self.setMinimumSize(800, 600)
        self.is_maximum_size = False
        self.move_position = QPoint(0, 0)

        self.top_frame = TopFrame()
        self.top_frame.btn_close.clicked.connect(self.close)
        self.top_frame.btn_maximize.clicked.connect(self.maximize_restore)
        self.top_frame.btn_minimize.clicked.connect(self.tooggle_theme)
        self.view = QWidget(self)
        self.top_frame1 = BottomFrame()

        self.vbox = QVBoxLayout(self)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setSpacing(0)
        self.vbox.addWidget(self.top_frame, 0, Qt.AlignmentFlag.AlignTop)
        # self.vbox.addWidget(self.view, 1)
        self.vbox.addWidget(self.top_frame1, 0, Qt.AlignmentFlag.AlignBottom)
        self.setWidget(self.view)
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)
        apply_shadow_effect(self.top_frame)
        apply_shadow_effect(self.top_frame1)
        # self.initDatabase()
        self.top_frame.mouseMoveEvent = self.move_window
        self.top_frame.mouseDoubleClickEvent = self.double_click_maximize_restore

    def initDatabase(self):
        """ initialize song library """
        DBInitializer.init()

        self.databaseThread = DatabaseThread(
            QSqlDatabase.database(DBInitializer.CONNECTION_NAME), self)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        gradient = QLinearGradient(0, 0, self.width(), self.height())  # 创建一个从左上到右下的线性渐变
        gradient.setColorAt(0.0, Qt.white)  # 渐变开始颜色
        gradient.setColorAt(1.0, Qt.black)  # 渐变结束颜色
        painter.setBrush(gradient)
        painter.drawRoundedRect(self.rect(), 20, 20)

    def tooggle_theme(self):
        """设置主题"""
        theme = Theme.DARK if self.top_frame.btn_minimize.btn_state == 'off' else Theme.LIGHT
        StyleSheet.TOP_FRAME.apply(self.top_frame,theme)
        StyleSheet.BOTTOM_FRAME.apply(self.top_frame1,theme)

    def maximize_restore(self):
        """最大化窗口和还原"""
        if not self.is_maximum_size:
            self.showMaximized()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            self.showNormal()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()
        self.is_maximum_size = not self.is_maximum_size

    def double_click_maximize_restore(self, event):
        """双击标题控件事件"""
        # IF DOUBLE CLICK CHANGE STATUS
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, self.maximize_restore)

    def move_window(self, event=None):
        """窗口拖动"""
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.move_position)
            event.accept()

    def resizeEvent(self, event):
        """处理窗口大小调整事件"""
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)


if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dome = Example()
    dome.show()
    app.exec()
