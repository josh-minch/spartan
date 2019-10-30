pyside2-uic ui/ui_mainwindow.ui > ui/ui_mainwindow.py
pyside2-uic ui/ui_optimumdietwindow.ui > ui/ui_optimumdietwindow.py

pyside2-rcc images/images.qrc -o images_rc.py

python main.py
