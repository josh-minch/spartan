import sys
import platform
import ctypes

from PySide2 import QtWidgets, QtGui, QtCore

import storage
import main_window
import welcome_window


def config_taskbar_icon():
    if platform.system() == 'Windows':
        # Necessary to set icon in taskbar
        myappid = u'spartan'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def run_welcome_check():
    try:
        with open('run_wel_check.csv', 'r') as check_file:
            return check_file.read()
    except FileNotFoundError:
        check_file = open('run_wel_check.csv', 'w+')
        check_text = 'run'
        check_file.write(check_text)
        return check_text

def run():
    config_taskbar_icon()

    app = QtWidgets.QApplication(sys.argv)

    check = run_welcome_check()
    if check == 'run':
        window = welcome_window.WelcomeWindow()
    if check == 'skip':
        window = main_window.MainWindow()

    sys.exit(app.exec_())
