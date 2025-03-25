# coding:utf-8
from enum import Enum
from typing import Union

from PySide6.QtCore import QFile
from PySide6.QtWidgets import QWidget

from app.common import QSS_PATH


class Theme(Enum):
    LIGHT = "Light"
    DARK = "Dark"
    AUTO = "Auto"


def getStyleSheetFromFile(file: Union[str, QFile]):
    """ get style sheet from qss file """
    f = QFile(file)
    f.open(QFile.ReadOnly)
    qss = str(f.readAll(), encoding='utf-8')
    f.close()
    return qss



class StyleSheetBase:
    """ Style sheet base class """

    def path(self, theme=Theme.AUTO):
        """ get the path of style sheet """
        raise NotImplementedError

    def content(self, theme=Theme.AUTO):
        """ get the content of style sheet """
        return getStyleSheetFromFile(self.path(theme))

    def apply(self, widget: QWidget, theme=Theme.AUTO):
        """ apply style sheet to widget """
        setStyleSheet(widget, self, theme)


class StyleSheetFile(StyleSheetBase):
    """ Style sheet file """

    def __init__(self, path: str):
        super().__init__()
        self.filePath = path

    def path(self, theme=Theme.AUTO):
        return self.filePath


def getStyleSheet(source: Union[str, StyleSheetBase], theme=Theme.AUTO):
    if isinstance(source, str):
        source = StyleSheetFile(source)

    return source.content(theme)


def setStyleSheet(widget: QWidget, source: Union[str, StyleSheetBase], theme=Theme.AUTO):
    widget.setStyleSheet(getStyleSheet(source, theme))


class StyleSheet(StyleSheetBase, Enum):
    """ Style sheet  """

    TOP_FRAME = 'top_frame'
    BOTTOM_FRAME = 'bottom_frame'

    def path(self, theme=Theme.AUTO):
        theme = Theme.DARK if theme == Theme.AUTO else theme
        return QSS_PATH/f"{theme.value.lower()}"/f"{self.value}.qss"
