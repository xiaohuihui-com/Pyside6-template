# -*- coding: utf-8 -*-
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QGraphicsDropShadowEffect, QWidget)


def apply_shadow_effect(widget, blur_radius=10, x_offset=4, y_offset=4, color=(0, 0, 0, 150)):
    """为指定的小部件应用阴影效果。

    Args:
        widget(QWidget): 要应用阴影效果的小部件.
        blur_radius(int): 阴影的模糊半径.
        x_offset(int): 阴影的X轴偏移量.
        y_offset(int): 阴影的Y轴偏移量.
        color: 表示阴影RGBA颜色的元组.
    """
    shadow = QGraphicsDropShadowEffect(widget)
    shadow.setBlurRadius(blur_radius)
    shadow.setXOffset(x_offset)
    shadow.setYOffset(y_offset)
    shadow.setColor(QColor(*color))
    widget.setGraphicsEffect(shadow)
