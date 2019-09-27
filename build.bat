pyside2-uic ui/ui_mainwindow.ui > ui/ui_mainwindow.py
pyside2-uic ui/ui_searchwindow.ui > ui/ui_searchwindow.py
pyside2-uic ui/ui_optimumdietwindow.ui > ui/ui_optimumdietwindow.py
pyside2-uic ui/ui_prefwidget.ui > ui/ui_prefwidget.py
pyside2-uic ui/ui_reqwidget.ui > ui/ui_reqwidget.py
pyside2-uic ui/ui_reswidget.ui > ui/ui_reswidget.py
pyside2-uic ui/ui_prefwindow.ui > ui/ui_prefwindow.py

pyside2-rcc images/images.qrc -o images_rc.py

python gui.py
