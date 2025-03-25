# coding: utf-8
from enum import Enum

from PySide6.QtGui import QColor, QIcon

from app.common.style_sheet import Theme

# coding:utf-8
from enum import Enum
from typing import Union

from PySide6.QtXml import QDomDocument
from PySide6.QtCore import QRectF, Qt, QFile, QObject, QRect
from PySide6.QtGui import QIcon, QIconEngine, QColor, QPixmap, QImage, QPainter, QAction
from PySide6.QtSvg import QSvgRenderer

from .overload import singledispatchmethod


def isDarkTheme():
    """ whether the theme is dark mode """
    return True


class FluentIconEngine(QIconEngine):
    """ Fluent icon engine """

    def __init__(self, icon, reverse=False):
        """
        Parameters
        ----------
        icon: QICon | Icon | FluentIconBase
            the icon to be drawn

        reverse: bool
            whether to reverse the theme of icon
        """
        super().__init__()
        self.icon = icon
        self.isThemeReversed = reverse

    def paint(self, painter, rect, mode, state):
        painter.save()

        if mode == QIcon.Disabled:
            painter.setOpacity(0.5)
        elif mode == QIcon.Selected:
            painter.setOpacity(0.7)

        # change icon color according to the theme
        icon = self.icon

        if not self.isThemeReversed:
            theme = Theme.AUTO
        else:
            theme = Theme.LIGHT if isDarkTheme() else Theme.DARK

        if isinstance(self.icon, Icon):
            icon = self.icon.fluentIcon.icon(theme)
        elif isinstance(self.icon, FluentIconBase):
            icon = self.icon.icon(theme)

        if rect.x() == 19:
            rect = rect.adjusted(-1, 0, 0, 0)

        icon.paint(painter, rect, Qt.AlignCenter, QIcon.Normal, state)
        painter.restore()


class SvgIconEngine(QIconEngine):
    """ Svg icon engine """

    def __init__(self, svg: str):
        super().__init__()
        self.svg = svg

    def paint(self, painter, rect, mode, state):
        drawSvgIcon(self.svg.encode(), painter, rect)

    def clone(self) -> QIconEngine:
        return SvgIconEngine(self.svg)

    def pixmap(self, size, mode, state):
        image = QImage(size, QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        pixmap = QPixmap.fromImage(image, Qt.NoFormatConversion)

        painter = QPainter(pixmap)
        rect = QRect(0, 0, size.width(), size.height())
        self.paint(painter, rect, mode, state)
        return pixmap


def getIconColor(theme=Theme.AUTO, reverse=False):
    """ get the color of icon based on theme """
    if not reverse:
        lc, dc = "black", "white"
    else:
        lc, dc = "white", "black"

    if theme == Theme.AUTO:
        color = dc if Theme.DARK else lc
    else:
        color = dc if theme == Theme.DARK else lc

    return color


def drawSvgIcon(icon, painter, rect):
    """ draw svg icon

    Parameters
    ----------
    icon: str | bytes | QByteArray
        the path or code of svg icon

    painter: QPainter
        painter

    rect: QRect | QRectF
        the rect to render icon
    """
    renderer = QSvgRenderer(icon)
    renderer.render(painter, QRectF(rect))


def writeSvg(iconPath: str, indexes=None, **attributes):
    """ write svg with specified attributes

    Parameters
    ----------
    iconPath: str
        svg icon path

    indexes: List[int]
        the path to be filled

    **attributes:
        the attributes of path

    Returns
    -------
    svg: str
        svg code
    """
    if not iconPath.lower().endswith('.svg'):
        return ""

    f = QFile(iconPath)
    f.open(QFile.ReadOnly)

    dom = QDomDocument()
    dom.setContent(f.readAll())

    f.close()

    # change the color of each path
    pathNodes = dom.elementsByTagName('path')
    indexes = range(pathNodes.length()) if not indexes else indexes
    for i in indexes:
        element = pathNodes.at(i).toElement()

        for k, v in attributes.items():
            element.setAttribute(k, v)

    return dom.toString()


def drawIcon(icon, painter, rect, state=QIcon.Off, **attributes):
    """ draw icon

    Parameters
    ----------
    icon: str | QIcon | FluentIconBaseBase
        the icon to be drawn

    painter: QPainter
        painter

    rect: QRect | QRectF
        the rect to render icon

    **attribute:
        the attribute of svg icon
    """
    if isinstance(icon, FluentIconBase):
        icon.render(painter, rect, **attributes)
    elif isinstance(icon, Icon):
        icon.fluentIcon.render(painter, rect, **attributes)
    else:
        icon = QIcon(icon)
        icon.paint(painter, QRectF(rect).toRect(), Qt.AlignCenter, state=state)


class FluentIconBase:
    """ Fluent icon base class """

    def path(self, theme=Theme.AUTO) -> str:
        """ get the path of icon

        Parameters
        ----------
        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`
        """
        raise NotImplementedError

    def icon(self, theme=Theme.AUTO, color: QColor = None) -> QIcon:
        """ create a fluent icon

        Parameters
        ----------
        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `qconfig.theme`

        color: QColor | Qt.GlobalColor | str
            icon color, only applicable to svg icon
        """
        path = self.path(theme)

        if not (path.endswith('.svg') and color):
            return QIcon(self.path(theme))

        color = QColor(color).name()
        return QIcon(SvgIconEngine(writeSvg(path, fill=color)))

    def colored(self, lightColor: QColor, darkColor: QColor) -> "ColoredFluentIcon":
        """ create a colored fluent icon

        Parameters
        ----------
        lightColor: str | QColor | Qt.GlobalColor
            icon color in light mode

        darkColor: str | QColor | Qt.GlobalColor
            icon color in dark mode
        """
        return ColoredFluentIcon(self, lightColor, darkColor)

    def qicon(self, reverse=False) -> QIcon:
        """ convert to QIcon, the theme of icon will be updated synchronously with app

        Parameters
        ----------
        reverse: bool
            whether to reverse the theme of icon
        """
        return QIcon(FluentIconEngine(self, reverse))

    def render(self, painter, rect, theme=Theme.AUTO, indexes=None, **attributes):
        """ draw svg icon

        Parameters
        ----------
        painter: QPainter
            painter

        rect: QRect | QRectF
            the rect to render icon

        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`

        indexes: List[int]
            the svg path to be modified

        **attributes:
            the attributes of modified path
        """
        icon = self.path(theme)

        if icon.endswith('.svg'):
            if attributes:
                icon = writeSvg(icon, indexes, **attributes).encode()

            drawSvgIcon(icon, painter, rect)
        else:
            icon = QIcon(icon)
            rect = QRectF(rect).toRect()
            painter.drawPixmap(rect, icon.pixmap(QRectF(rect).toRect().size()))


class ColoredFluentIcon(FluentIconBase):
    """ Colored fluent icon """

    def __init__(self, icon: FluentIconBase, lightColor, darkColor):
        """
        Parameters
        ----------
        icon: FluentIconBase
            the icon to be colored

        lightColor: str | QColor | Qt.GlobalColor
            icon color in light mode

        darkColor: str | QColor | Qt.GlobalColor
            icon color in dark mode
        """
        super().__init__()
        self.fluentIcon = icon
        self.lightColor = QColor(lightColor)
        self.darkColor = QColor(darkColor)

    def path(self, theme=Theme.AUTO) -> str:
        return self.fluentIcon.path(theme)

    def render(self, painter, rect, theme=Theme.AUTO, indexes=None, **attributes):
        icon = self.path(theme)

        if not icon.endswith('.svg'):
            return self.fluentIcon.render(painter, rect, theme, indexes, attributes)

        if theme == Theme.AUTO:
            color = self.darkColor if isDarkTheme() else self.lightColor
        else:
            color = self.darkColor if theme == Theme.DARK else self.lightColor

        attributes.update(fill=color.name())
        icon = writeSvg(icon, indexes, **attributes).encode()
        drawSvgIcon(icon, painter, rect)


def toQIcon(icon: Union[QIcon, FluentIconBase, str]) -> QIcon:
    """ convet `icon` to `QIcon` """
    if isinstance(icon, str):
        return QIcon(icon)

    if isinstance(icon, FluentIconBase):
        return icon.icon()

    return icon


class Action(QAction):
    """ Fluent action

    Constructors
    ------------
    * Action(`parent`: QWidget = None, `**kwargs`)
    * Action(`text`: str, `parent`: QWidget = None, `**kwargs`)
    * Action(`icon`: QIcon | FluentIconBase, `parent`: QWidget = None, `**kwargs`)
    """

    @singledispatchmethod
    def __init__(self, parent: QObject = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.fluentIcon = None

    @__init__.register
    def _(self, text: str, parent: QObject = None, **kwargs):
        super().__init__(text, parent, **kwargs)
        self.fluentIcon = None

    @__init__.register
    def _(self, icon: QIcon, text: str, parent: QObject = None, **kwargs):
        super().__init__(icon, text, parent, **kwargs)
        self.fluentIcon = None

    @__init__.register
    def _(self, icon: FluentIconBase, text: str, parent: QObject = None, **kwargs):
        super().__init__(icon.icon(), text, parent, **kwargs)
        self.fluentIcon = icon

    def icon(self) -> QIcon:
        if self.fluentIcon:
            return Icon(self.fluentIcon)

        return super().icon()

    def setIcon(self, icon: Union[FluentIconBase, QIcon]):
        if isinstance(icon, FluentIconBase):
            self.fluentIcon = icon
            icon = icon.icon()

        super().setIcon(icon)


class FluentIconBase:
    """ Fluent icon base class """

    def path(self, theme=Theme.AUTO) -> str:
        """ get the path of icon

        Parameters
        ----------
        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`
        """
        raise NotImplementedError

    def icon(self, theme=Theme.AUTO, color: QColor = None) -> QIcon:
        """ create a fluent icon

        Parameters
        ----------
        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `qconfig.theme`

        color: QColor | Qt.GlobalColor | str
            icon color, only applicable to svg icon
        """
        path = self.path(theme)

        if not (path.endswith('.svg') and color):
            return QIcon(self.path(theme))

        color = QColor(color).name()
        return QIcon(SvgIconEngine(writeSvg(path, fill=color)))

    def colored(self, lightColor: QColor, darkColor: QColor) -> "ColoredFluentIcon":
        """ create a colored fluent icon

        Parameters
        ----------
        lightColor: str | QColor | Qt.GlobalColor
            icon color in light mode

        darkColor: str | QColor | Qt.GlobalColor
            icon color in dark mode
        """
        return ColoredFluentIcon(self, lightColor, darkColor)

    def qicon(self, reverse=False) -> QIcon:
        """ convert to QIcon, the theme of icon will be updated synchronously with app

        Parameters
        ----------
        reverse: bool
            whether to reverse the theme of icon
        """
        return QIcon(FluentIconEngine(self, reverse))

    def render(self, painter, rect, theme=Theme.AUTO, indexes=None, **attributes):
        """ draw svg icon

        Parameters
        ----------
        painter: QPainter
            painter

        rect: QRect | QRectF
            the rect to render icon

        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`

        indexes: List[int]
            the svg path to be modified

        **attributes:
            the attributes of modified path
        """
        icon = self.path(theme)

        if icon.endswith('.svg'):
            if attributes:
                icon = writeSvg(icon, indexes, **attributes).encode()

            drawSvgIcon(icon, painter, rect)
        else:
            icon = QIcon(icon)
            rect = QRectF(rect).toRect()
            painter.drawPixmap(rect, icon.pixmap(QRectF(rect).toRect().size()))


class Icon(FluentIconBase, Enum):
    GRID = "Grid"
    MENU = "Menu"
    TEXT = "Text"
    PRICE = "Price"
    EMOJI_TAB_SYMBOLS = "EmojiTabSymbols"

    def path(self, theme=Theme.AUTO):
        return f":/gallery/images/icons/{self.value}_{getIconColor(theme)}.svg"
