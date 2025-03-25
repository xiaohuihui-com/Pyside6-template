# coding: utf-8
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QApplication

from app.common.utils import CustomGrip, apply_shadow_effect
from app.gui.ui_home import Ui_MainWindow


class HomeInterface(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(HomeInterface, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.top.mouseMoveEvent = self.move_window

        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)
        apply_shadow_effect(self.btn1)
        apply_shadow_effect(self.btn2)
        apply_shadow_effect(self.btn3)
        apply_shadow_effect(self.btn4)
        apply_shadow_effect(self.btn5)

        self.initWindow()

    def initWindow(self):
        self.resize(960, 680)
        self.setMinimumWidth(760)

        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()

    def move_window(self, event=None):
        """窗口拖动"""
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos())
            event.accept()

    def resizeEvent(self, event):
        """处理窗口大小调整事件"""
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = HomeInterface()
    window.show()
    sys.exit(app.exec())
