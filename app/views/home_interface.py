from PySide6.QtWidgets import QMainWindow

from app.gui.ui_home import Ui_MainWindow


class HomeInterface(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(HomeInterface, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = HomeInterface()
    window.show()
    sys.exit(app.exec())
