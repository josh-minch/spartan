pyside2-uic ui/ui_reqwizwidget.ui > ui/ui_reqwizwidget.py
pyside2-uic ui/ui_welcomewindow.ui > ui/ui_welcomewindow.py

pyside2-rcc images/images.qrc -o images_rc.py

python welcome_window.py
pause