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

from spartan import Food
from gui_constants import *

class FridgeModel(QAbstractTableModel):
    def __init__(self, parent=None, foods=None):
        QAbstractTableModel.__init__(self, parent)
        self.foods = foods

    def rowCount(self, index=QModelIndex()):
        return len(self.foods)
        
    def columnCount(self, index=QModelIndex()):
        return len(col_to_attr)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self.foods):
            return None

        # Hide units unless corresponding attribute has a value
        if role in (Qt.DisplayRole, Qt.EditRole):
            if index.column() == PRICE_UNIT_COL and self.foods[index.row()].price is None:
                return None
            if index.column() == MIN_UNIT_COL and self.foods[index.row()].min is None:
                return None
            if index.column() == MAX_UNIT_COL and self.foods[index.row()].max is None:
                return None
            if index.column() == TARGET_UNIT_COL and self.foods[index.row()].target is None:
                return None

            attr_str = col_to_attr[index.column()]
            return getattr(self.foods[index.row()], attr_str)

        if role == Qt.TextAlignmentRole:
            if index.column() in (PRICE_COL, MIN_COL, MAX_COL, TARGET_COL):
                return int(Qt.AlignRight | Qt.AlignVCenter)
            #if index.column() == PRICE_UNIT_COL or MIN_UNIT_COL or MAX_UNIT_COL or TARGET_UNIT_COL:
            #    return int(Qt.AlignLeft | Qt.AlignVCenter)
            
        return None
    
    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):

        if orientation == Qt.Horizontal:

            if role == Qt.DisplayRole:
                if section == FOOD_ID_COL:
                    return "Id"
                elif section == NAME_COL:
                    return " Food"
                elif section == PRICE_COL:
                    return "Price"
                elif section == MIN_COL:
                    return "At least"
                elif section == MAX_COL:
                    return "At most"
                elif section == TARGET_COL:
                    return "Equal to"
                elif section in (PRICE_UNIT_COL, MIN_UNIT_COL, MAX_UNIT_COL, TARGET_UNIT_COL):
                    return ""

            if role == Qt.TextAlignmentRole:
                if section == NAME_COL:
                    return int(Qt.AlignLeft | Qt.AlignVCenter)
                if section == PRICE_COL or MIN_COL or MAX_COL or TARGET_COL:
                    return int(Qt.AlignRight | Qt.AlignVCenter)

        return None

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self.foods.insert(position + row, Food())
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

            if index.column() == FOOD_ID_COL:
                food.food_id = value
            elif index.column() == NAME_COL:
                food.name = value
            elif index.column() == PRICE_COL:
                food.price = value
            elif index.column() == MIN_COL:
                food.min = value
            elif index.column() == MAX_COL:
                food.max = value
            elif index.column() == TARGET_COL:
                food.target = value
            else:
                return False

            self.dataChanged.emit(index, index)
            return True

        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == NAME_COL:
            return Qt.ItemFlags(QAbstractTableModel.flags(self, index) |
                            ~Qt.ItemIsEditable)
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) |
                            Qt.ItemIsEditable)