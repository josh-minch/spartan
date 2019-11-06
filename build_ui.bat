pyside2-uic spartan/ui/ui_mainwindow.ui > spartan/ui/ui_mainwindow.py
pyside2-uic spartan/ui/ui_searchwindow.ui > spartan/ui/ui_searchwindow.py
pyside2-uic spartan/ui/ui_optimumdietwindow.ui > spartan/ui/ui_optimumdietwindow.py
pyside2-uic spartan/ui/ui_prefwidget.ui > spartan/ui/ui_prefwidget.py
pyside2-uic spartan/ui/ui_reqwidget.ui > spartan/ui/ui_reqwidget.py
pyside2-uic spartan/ui/ui_reswidget.ui > spartan/ui/ui_reswidget.py
pyside2-uic spartan/ui/ui_prefwindow.ui > spartan/ui/ui_prefwindow.py
pyside2-uic spartan/ui/ui_reqwizwidget.ui > spartan/ui/ui_reqwizwidget.py
pyside2-uic spartan/ui/ui_welcomewindow.ui > spartan/ui/ui_welcomewindow.py

pyside2-rcc spartan/icon/icon.qrc -o spartan/icon/icon_rc.py

python spartan/main.py
