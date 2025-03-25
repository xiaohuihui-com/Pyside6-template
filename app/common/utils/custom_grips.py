from PySide6.QtCore import Qt, QRect, QSize
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget, QSizeGrip, QFrame, QHBoxLayout


class CustomGrip(QWidget):
    def __init__(self, parent, position, disable_color=False):
        # 初始化父类QWidget
        QWidget.__init__(self)
        # 设置父部件
        self.parent = parent
        self.setParent(parent)
        # 创建一个Widgets对象用于管理子部件
        self.wi = Widgets()

        # 根据position参数显示不同的边缘调整器
        # 显示顶部边缘调整器
        if position == Qt.TopEdge:
            # 调用Widgets对象的top方法设置顶部边缘调整器
            self.wi.top(self)
            # 设置几何位置和大小
            self.setGeometry(0, 0, self.parent.width(), 10)
            self.setMaximumHeight(10)

            # 创建左上角和右上角的QSizeGrip控件
            top_left = QSizeGrip(self.wi.top_left)
            top_right = QSizeGrip(self.wi.top_right)

            # 定义鼠标移动事件处理函数以调整窗口高度
            def resize_top(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())
                geo = self.parent.geometry()
                geo.setTop(geo.bottom() - height)
                self.parent.setGeometry(geo)
                event.accept()

            # 将鼠标移动事件处理函数绑定到顶部框架
            self.wi.top.mouseMoveEvent = resize_top

            # 如果disable_color为True，则将背景颜色设为透明
            if disable_color:
                self.wi.top_left.setStyleSheet("background: transparent")
                self.wi.top_right.setStyleSheet("background: transparent")
                self.wi.top.setStyleSheet("background: transparent")

        # 显示底部边缘调整器
        elif position == Qt.BottomEdge:
            # 调用Widgets对象的bottom方法设置底部边缘调整器
            self.wi.bottom(self)
            # 设置几何位置和大小
            self.setGeometry(0, self.parent.height() - 10, self.parent.width(), 10)
            self.setMaximumHeight(10)

            # 创建左下角和右下角的QSizeGrip控件
            self.bottom_left = QSizeGrip(self.wi.bottom_left)
            self.bottom_right = QSizeGrip(self.wi.bottom_right)

            # 定义鼠标移动事件处理函数以调整窗口高度
            def resize_bottom(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())
                self.parent.resize(self.parent.width(), height)
                event.accept()

            # 将鼠标移动事件处理函数绑定到底部框架
            self.wi.bottom.mouseMoveEvent = resize_bottom

            # 如果disable_color为True，则将背景颜色设为透明
            if disable_color:
                self.wi.bottom_left.setStyleSheet("background: transparent")
                self.wi.bottom_right.setStyleSheet("background: transparent")
                self.wi.bottom.setStyleSheet("background: transparent")

        # 显示左侧边缘调整器
        elif position == Qt.LeftEdge:
            # 调用Widgets对象的left方法设置左侧边缘调整器
            self.wi.left(self)
            # 设置几何位置和大小
            self.setGeometry(0, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            # 定义鼠标移动事件处理函数以调整窗口宽度
            def resize_left(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())
                geo = self.parent.geometry()
                geo.setLeft(geo.right() - width)
                self.parent.setGeometry(geo)
                event.accept()

            # 将鼠标移动事件处理函数绑定到左侧框架
            self.wi.leftgrip.mouseMoveEvent = resize_left

            # 如果disable_color为True，则将背景颜色设为透明
            if disable_color:
                self.wi.leftgrip.setStyleSheet("background: transparent")

        # 显示右侧边缘调整器
        elif position == Qt.RightEdge:
            # 调用Widgets对象的right方法设置右侧边缘调整器
            self.wi.right(self)
            # 设置几何位置和大小
            self.setGeometry(self.parent.width() - 10, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            # 定义鼠标移动事件处理函数以调整窗口宽度
            def resize_right(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(), self.parent.width() + delta.x())
                self.parent.resize(width, self.parent.height())
                event.accept()

            # 将鼠标移动事件处理函数绑定到右侧框架
            self.wi.rightgrip.mouseMoveEvent = resize_right

            # 如果disable_color为True，则将背景颜色设为透明
            if disable_color:
                self.wi.rightgrip.setStyleSheet("background: transparent")

    def mouseReleaseEvent(self, event):
        # 鼠标释放事件处理函数，清空mousePos变量
        self.mousePos = None

    def resizeEvent(self, event):
        # 窗口大小改变事件处理函数，根据新的窗口大小调整边缘调整器的位置
        if hasattr(self.wi, 'container_top'):
            self.wi.container_top.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'container_bottom'):
            self.wi.container_bottom.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'leftgrip'):
            self.wi.leftgrip.setGeometry(0, 0, 10, self.height() - 20)

        elif hasattr(self.wi, 'rightgrip'):
            self.wi.rightgrip.setGeometry(0, 0, 10, self.height() - 20)


class Widgets(object):
    def top(self, Form):
        # 检查Form是否有objectName属性，如果没有则设置默认值
        if not Form.objectName():
            Form.setObjectName(u"Form")
        # 创建一个QFrame作为容器，并设置其属性
        self.container_top = QFrame(Form)
        self.container_top.setObjectName(u"container_top")
        self.container_top.setGeometry(QRect(0, 0, 500, 10))
        self.container_top.setMinimumSize(QSize(0, 10))
        self.container_top.setMaximumSize(QSize(16777215, 10))
        self.container_top.setFrameShape(QFrame.NoFrame)
        self.container_top.setFrameShadow(QFrame.Raised)
        # 创建水平布局并将其添加到容器中
        self.top_layout = QHBoxLayout(self.container_top)
        self.top_layout.setSpacing(0)
        self.top_layout.setObjectName(u"top_layout")
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        # 创建左上角的小方块，并设置其属性
        self.top_left = QFrame(self.container_top)
        self.top_left.setObjectName(u"top_left")
        self.top_left.setMinimumSize(QSize(10, 10))
        self.top_left.setMaximumSize(QSize(10, 10))
        self.top_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.top_left.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.top_left.setFrameShape(QFrame.NoFrame)
        self.top_left.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_left)
        # 创建顶部中间的部分，并设置其属性
        self.top = QFrame(self.container_top)
        self.top.setObjectName(u"top")
        self.top.setCursor(QCursor(Qt.SizeVerCursor))
        self.top.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top)
        # 创建右上角的小方块，并设置其属性
        self.top_right = QFrame(self.container_top)
        self.top_right.setObjectName(u"top_right")
        self.top_right.setMinimumSize(QSize(10, 10))
        self.top_right.setMaximumSize(QSize(10, 10))
        self.top_right.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.top_right.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.top_right.setFrameShape(QFrame.NoFrame)
        self.top_right.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_right)

    def bottom(self, Form):
        # 检查Form是否有objectName属性，如果没有则设置默认值
        if not Form.objectName():
            Form.setObjectName(u"Form")
        # 创建一个QFrame作为容器，并设置其属性
        self.container_bottom = QFrame(Form)
        self.container_bottom.setObjectName(u"container_bottom")
        self.container_bottom.setGeometry(QRect(0, 0, 500, 10))
        self.container_bottom.setMinimumSize(QSize(0, 10))
        self.container_bottom.setMaximumSize(QSize(16777215, 10))
        self.container_bottom.setFrameShape(QFrame.NoFrame)
        self.container_bottom.setFrameShadow(QFrame.Raised)
        # 创建水平布局并将其添加到容器中
        self.bottom_layout = QHBoxLayout(self.container_bottom)
        self.bottom_layout.setSpacing(0)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        # 创建左下角的小方块，并设置其属性
        self.bottom_left = QFrame(self.container_bottom)
        self.bottom_left.setObjectName(u"bottom_left")
        self.bottom_left.setMinimumSize(QSize(10, 10))
        self.bottom_left.setMaximumSize(QSize(10, 10))
        self.bottom_left.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.bottom_left.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.bottom_left.setFrameShape(QFrame.NoFrame)
        self.bottom_left.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_left)
        # 创建底部中间的部分，并设置其属性
        self.bottom = QFrame(self.container_bottom)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setCursor(QCursor(Qt.SizeVerCursor))
        self.bottom.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom)
        # 创建右下角的小方块，并设置其属性
        self.bottom_right = QFrame(self.container_bottom)
        self.bottom_right.setObjectName(u"bottom_right")
        self.bottom_right.setMinimumSize(QSize(10, 10))
        self.bottom_right.setMaximumSize(QSize(10, 10))
        self.bottom_right.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.bottom_right.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.bottom_right.setFrameShape(QFrame.NoFrame)
        self.bottom_right.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_right)

    def left(self, Form):
        # 检查Form是否有objectName属性，如果没有则设置默认值
        if not Form.objectName():
            Form.setObjectName(u"Form")
        # 创建一个QFrame作为左侧边缘调整器，并设置其属性
        self.leftgrip = QFrame(Form)
        self.leftgrip.setObjectName(u"left")
        self.leftgrip.setGeometry(QRect(0, 10, 10, 480))
        self.leftgrip.setMinimumSize(QSize(10, 0))
        self.leftgrip.setCursor(QCursor(Qt.SizeHorCursor))
        self.leftgrip.setStyleSheet(u"background-color: rgb(255, 121, 198);")
        self.leftgrip.setFrameShape(QFrame.NoFrame)
        self.leftgrip.setFrameShadow(QFrame.Raised)

    def right(self, Form):
        # 检查Form是否有objectName属性，如果没有则设置默认值
        if not Form.objectName():
            Form.setObjectName(u"Form")
        # 设置表单的初始大小
        Form.resize(500, 500)
        # 创建一个QFrame作为右侧边缘调整器，并设置其属性
        self.rightgrip = QFrame(Form)
        self.rightgrip.setObjectName(u"right")
        self.rightgrip.setGeometry(QRect(0, 0, 10, 500))
        self.rightgrip.setMinimumSize(QSize(10, 0))
        self.rightgrip.setCursor(QCursor(Qt.SizeHorCursor))
        self.rightgrip.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.rightgrip.setFrameShape(QFrame.NoFrame)
        self.rightgrip.setFrameShadow(QFrame.Raised)


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.resize(600, 400)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

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
    top_frame = Example()
    top_frame.show()
    app.exec()
