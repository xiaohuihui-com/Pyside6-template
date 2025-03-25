# coding:utf-8
import os
import sys

from PySide6.QtWidgets import QApplication

from app.views import HomeInterface
from app.common import THEME_PATH, getStyleSheetFromFile
from app.resources import resource_rc

if __name__ == '__main__':
    os.environ["QT_SCALE_FACTOR"] = "Auto"
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"

    app = QApplication(sys.argv)
    qss = getStyleSheetFromFile(THEME_PATH)
    app.setStyleSheet(qss)
    window = HomeInterface()
    window.show()
    sys.exit(app.exec())
