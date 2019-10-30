import sys
import platform
import ctypes

from PySide2 import QtWidgets, QtGui, QtCore

import storage
import main_window
import welcome_window

def run():
    if platform.system() == 'Windows':
        myappid = u'spartan'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QtWidgets.QApplication(sys.argv)

    with open('run_wel_check.csv', 'r') as check_file:
        check = check_file.read()
        if check == 'run':
            storage.create_spartan_db()
            window = welcome_window.WelcomeWindow()
        if check == 'skip':
            window = main_window.MainWindow()

    sys.exit(app.exec_())
