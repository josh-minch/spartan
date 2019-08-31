"""**************************************************************************
**
** Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
** All rights reserved.
** Contact: Nokia Corporation (qt-info@nokia.com)
**
** This file is part of the examples of the Qt Toolkit.
**
** You may use this file under the terms of the BSD license as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
**     the names of its contributors may be used to endorse or promote
**     products derived from this software without specific prior written
**     permission.
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
**************************************************************************"""

from PySide2.QtCore import (Qt, QAbstractTableModel, QModelIndex)

from gui_constants import *

class FridgeSelectedModel(QAbstractTableModel):
    def __init__(self, parent=None, foods=None):
        QAbstractTableModel.__init__(self, parent)
        self.foods = foods

    def rowCount(self, index=QModelIndex()):
        return len(self.foods)
        
    def columnCount(self, index=QModelIndex()):
        return len(S_COL_TO_ATTR)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self.foods):
            return None

        if role == Qt.DisplayRole or role == Qt.EditRole:
            name = self.foods[index.row()]["name"]
            amount: float = self.foods[index.row()]["amount"]
            unit = self.foods[index.row()]["unit"]
            calories: float = self.foods[index.row()]["calories"]

            if index.column() == S_NAME_COL:
                return name
            elif index.column() == S_AMOUNT_COL:
                return amount
            elif index.column() == S_UNIT_COL:
                return unit
            elif index.column() == S_CALORIES_COL:
                return calories
          
        # A bug in PySide2 requires that we cast the bitwise 
        # AlignmentFlag to an int before returning
        # https://bugreports.qt.io/browse/PYSIDE-20

        if role == Qt.TextAlignmentRole:
            if index.column() == S_AMOUNT_COL:
                return int(Qt.AlignRight | Qt.AlignVCenter)

        return None
    
    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if section == S_NAME_COL:
                    return "Food"
                elif section == S_AMOUNT_COL:
                    return "Quantity"
                elif section == S_UNIT_COL:
                    return ''
                elif section == S_CALORIES_COL:
                    return 'Calories'
    
        return None

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self.foods.insert(position + row, {"name":"", "amount":"",
                                                   "unit":"", "calories":""})
        self.endInsertRows()
       
        return True
        
    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        del self.foods[position:position+rows]
        self.endRemoveRows()
       
        return True

    def setData(self, index, value, role=Qt.EditRole):
        if role != Qt.EditRole:
            return False

        if index.isValid() and 0 <= index.row() < len(self.foods):
            food = self.foods[index.row()]

            if index.column() == S_NAME_COL:
                food['name'] = value
            elif index.column() == S_AMOUNT_COL:
                food['amount'] = float(value)
            elif index.column() == S_UNIT_COL:
                food['unit'] = value
            elif index.column() == S_CALORIE_COL:
                food['percent'] = float(value)
            else:
                return False

            self.dataChanged.emit(index, index, [])
            return True

        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == S_NAME_COL:
            return Qt.ItemFlags(QAbstractTableModel.flags(self, index) |
                            ~Qt.ItemIsEditable)
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) |
                            Qt.ItemIsEditable)