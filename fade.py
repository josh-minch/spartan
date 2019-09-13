import sys

from PySide2.QtCore import Qt, QEvent, Slot, QModelIndex, SIGNAL, SLOT, QPropertyAnimation, QTimer, QEasingCurve, QVariantAnimation, QEventLoop
from PySide2.QtGui import QFont, QKeySequence, QPalette, QColor
from PySide2.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QListWidget, QTableWidget,
                               QListWidgetItem, QTableWidgetItem, QAbstractItemView,
                               QHeaderView, QShortcut, QGraphicsOpacityEffect,
                               QLabel, QWidget, QVBoxLayout, QPushButton)

class AnimationLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.animation = QVariantAnimation()
        self.animation.valueChanged.connect(self.changeColor)

    @Slot()
    def changeColor(self, color):
        palette = self.palette()
        palette.setColor(QPalette.WindowText, color)
        self.setPalette(palette)

    def startFadeIn(self):
        self.animation.stop()
        self.animation.setStartValue(QColor(0, 0, 0, 0))
        self.animation.setEndValue(QColor(0, 0, 0, 255))
        self.animation.setDuration(2000)
        self.animation.setEasingCurve(QEasingCurve.InBack)
        self.animation.start()

    def startFadeOut(self):
        self.animation.stop()
        self.animation.setStartValue(QColor(0, 0, 0, 255))
        self.animation.setEndValue(QColor(0, 0, 0, 0))
        self.animation.setDuration(2000)
        self.animation.setEasingCurve(QEasingCurve.OutBack)
        self.animation.start()

    def startAnimation(self):
        self.startFadeIn()
        loop = QEventLoop()
        self.animation.finished.connect(loop.quit)
        loop.exec_()
        QTimer.singleShot(2000, self.startFadeOut)

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        self.greeting_text = AnimationLabel("greeting_text")
        self.greeting_text.setStyleSheet("font : 45px; font : bold; font-family : HelveticaNeue-UltraLight")
        lay.addWidget(self.greeting_text)
        btnFadeIn = QPushButton("fade in")
        btnFadeOut = QPushButton("fade out")
        btnAnimation = QPushButton("animation")
        lay.addWidget(btnFadeIn)
        lay.addWidget(btnFadeOut)
        lay.addWidget(btnAnimation)
        btnFadeIn.clicked.connect(self.greeting_text.startFadeIn)
        btnFadeOut.clicked.connect(self.greeting_text.startFadeOut)
        btnAnimation.clicked.connect(self.greeting_text.startAnimation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())

'''
def fade_in(self):
    self.notification = QLabel()
    self.notification.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
    self.notification.setStyleSheet("border:3px solid gray; border-radius:20px; font: 12pt Segou UI;")
    self.notification.setAlignment(Qt.AlignCenter)
    self.notification.setText("Add foods to your fridge before generating a diet")

    self.effect = QGraphicsOpacityEffect()
    self.notification.setGraphicsEffect(self.effect)
    animation = QPropertyAnimation(self.effect, b"opacity")
    animation.setDuration(3000)
    animation.setStartValue(0)
    animation.setEndValue(1)
    #animation.setEasingCurve(QEasingCurve.Linear)
    animation.start(QPropertyAnimation.DeleteWhenStopped)

    self.notification.show()
    timer = QTimer(self)
    timer.setSingleShot(True)
    timer.timeout.connect(self.fade_out)
    #timer.timeout.connect(self.notification.hide())
    #timer.timeout.connect(self.timer_done)
    timer.start(4000)

 def fade_out(self):
    self.fade_out_effect = QGraphicsOpacityEffect()
    self.notification.setGraphicsEffect(self.fade_out_effect)

    animation = QPropertyAnimation(self.fade_out_effect, b"opacity")
    animation.setDuration(1000) # it will took 1000ms to fade out
    animation.setStartValue(1)
    animation.setEndValue(0)
    animation.setEasingCurve(QEasingCurve.OutBack)
    animation.start(QPropertyAnimation.DeleteWhenStopped)
    #if animation.finished():
    #    self.notification.hide()
    animation.finished.connect(self.notification.hide())
'''