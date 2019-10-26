# -*- coding: utf-8 -*-
#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

from __future__ import unicode_literals
from PySide2 import QtCore, QtGui, QtWidgets

import spartan
from widget.req_wiz_widget import ReqWizWidget
from widget.res_wiz_widget import ResWizWidget

class Wizard(QtWidgets.QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.addPage(ReqPage())
        self.addPage(ResPage())
        self.addPage(ConclusionPage())

        self.setWindowTitle("Spartan")

    def accept(self):
        className = self.field('className')
        baseClass = self.field('baseClass')
        macroName = self.field('macroName')
        baseInclude = self.field('baseInclude')

        outputDir = self.field('outputDir')
        header = self.field('header')
        implementation = self.field('implementation')

        block = ''

        if self.field('comment'):
            block += '/*\n'
            block += '    ' + header + '\n'
            block += '*/\n'
            block += '\n'

        if self.field('protect'):
            block += '#ifndef ' + macroName + '\n'
            block += '#define ' + macroName + '\n'
            block += '\n'

        if self.field('includeBase'):
            block += '#include ' + baseInclude + '\n'
            block += '\n'

        block += 'class ' + className
        if baseClass:
            block += ' : public ' + baseClass

        block += '\n'
        block += '{\n'

        if self.field('qobjectMacro'):
            block += '    Q_OBJECT\n'
            block += '\n'

        block += 'public:\n'

        if self.field('qobjectCtor'):
            block += '    ' + className + '(QObject *parent = 0);\n'
        elif self.field('qwidgetCtor'):
            block += '    ' + className + '(QWidget *parent = 0);\n'
        elif self.field('defaultCtor'):
            block += '    ' + className + '();\n'

            if self.field('copyCtor'):
                block += '    ' + className + '(const ' + className + ' &other);\n'
                block += '\n'
                block += '    ' + className + ' &operator=' + '(const ' + className + ' &other);\n'

        block += '};\n'

        if self.field('protect'):
            block += '\n'
            block += '#endif\n'

        headerFile = QtCore.QFile(outputDir + '/' + header)

        if not headerFile.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
            QtWidgets.QMessageBox.warning(None, "Class Wizard",
                    "Cannot write file %s:\n%s" % (headerFile.fileName(), headerFile.errorString()))
            return

        headerFile.write(QtCore.QByteArray(block.encode("utf-8")))

        block = ''

        if self.field('comment'):
            block += '/*\n'
            block += '    ' + implementation + '\n'
            block += '*/\n'
            block += '\n'

        block += '#include "' + header + '"\n'
        block += '\n'

        if self.field('qobjectCtor'):
            block += className + '::' + className + '(QObject *parent)\n'
            block += '    : ' + baseClass + '(parent)\n'
            block += '{\n'
            block += '}\n'
        elif self.field('qwidgetCtor'):
            block += className + '::' + className + '(QWidget *parent)\n'
            block += '    : ' + baseClass + '(parent)\n'
            block += '{\n'
            block += '}\n'
        elif self.field('defaultCtor'):
            block += className + '::' + className + '()\n'
            block += '{\n'
            block += '    // missing code\n'
            block += '}\n'

            if self.field('copyCtor'):
                block += '\n'
                block += className + '::' + className + '(const ' + className + ' &other)\n'
                block += '{\n'
                block += '    *this = other;\n'
                block += '}\n'
                block += '\n'
                block += className + ' &' + className + '::operator=(const ' + className + ' &other)\n'
                block += '{\n'

                if baseClass:
                    block += '    ' + baseClass + '::operator=(other);\n'

                block += '    // missing code\n'
                block += '    return *this;\n'
                block += '}\n'

        implementationFile = QtCore.QFile(outputDir + '/' + implementation)

        if not implementationFile.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
            QtWidgets.QMessageBox.warning(None, "Class Wizard",
                    "Cannot write file %s:\n%s" % (implementationFile.fileName(), implementationFile.errorString()))
            return

        implementationFile.write(QtCore.QByteArray(block.encode("utf-8")))

        super(ClassWizard, self).accept()


class ReqPage(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("Nutritional Requirements")

        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(0)
        self.req_widget = ReqWizWidget()
        layout.addWidget(self.req_widget)
        self.setLayout(layout)

class ResPage(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("Dietary Restrictions")

        layout = QtWidgets.QVBoxLayout()
        self.res_widget = ResWizWidget()
        layout.addWidget(self.res_widget)
        self.setLayout(layout)

class ConclusionPage(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(ConclusionPage, self).__init__(parent)

        self.setTitle("Conclusion")
        self.setPixmap(QtWidgets.QWizard.WatermarkPixmap,
                QtGui.QPixmap(':/images/watermark2.png'))

        self.label = QtWidgets.QLabel()
        self.label.setWordWrap(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def initializePage(self):
        finishText = self.wizard().buttonText(QtWidgets.QWizard.FinishButton)
        finishText.replace('&', '')
        self.label.setText("Click %s to generate the class skeleton." % finishText)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle(QtWidgets.QStyleFactory.create('windows'))
    wizard = Wizard()
    wizard.show()
    sys.exit(app.exec_())
