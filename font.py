import platform

from PySide2.QtGui import QFont

family_title = QFont.SansSerif
family_subtitle = QFont.SansSerif
family_header = QFont.SansSerif
family_body = QFont.SansSerif
family_symbol = QFont.SansSerif

px_title = 24
px_subtitle = 18
px_body = 14
px_header = px_body
px_symbol = px_body

weight_title = QFont.Light
weight_subtitle = QFont.Normal
weight_header = QFont.DemiBold
weight_body = QFont.Normal
weight_symbol = QFont.Normal


if platform.system() == 'Windows':
    # We must set the title family explicitly to the Semilight weight
    # of Segoe UI. Setting the weight through Qt does not give the correct font.
    family_title = 'Segoe UI Semilight'
    weight_title = QFont.Normal

    family_body = family_subtitle = family_header = 'Courier New'
    fmaily_symbol = 'Segoe UI Symbol'

elif platform.system() == 'Darwin':
    family_body = family_subtitle = family_header = family_symbol = 'SF Pro Text'
    family_title = 'SF Pro Display'

def set_font(widget, family, px, weight):
    font = QFont()
    font.setFamily(family)
    font.setPixelSize(px)
    font.setWeight(weight)
    widget.setFont(font)

def set_font_body(widget):
    set_font(widget, family_body, px_body, weight_body)

def set_font_title(widget):
    set_font(widget, family_title, px_title, weight_title)

def set_font_subtitle(widget):
    set_font(widget, family_subtitle, px_subtitle, weight_subtitle)

def set_font_header(widget):
    set_font(widget, family_header, px_header, weight_header)

def set_font_symbol(widget):
    set_font(widget, family_symbol, px_symbol, weight_symbol)
