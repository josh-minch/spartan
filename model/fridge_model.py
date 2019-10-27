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
        return F_NUM_COLS

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self.foods):
            return None

        if role in (Qt.DisplayRole, Qt.EditRole):
            if index.column() == PER_COL:
                return 'per'
            attr_str = f_col_to_attr[index.column()]
            attr = getattr(self.foods[index.row()], attr_str)
            return attr

        if role == Qt.ToolTipRole:
            if index.column() == NAME_COL:
                return self.foods[index.row()].name

        if role == Qt.TextAlignmentRole:
            if index.column() in (PRICE_COL, PRICE_QUANTITY_COL, MIN_COL, MAX_COL, TARGET_COL, NUT_QUANT_COL):
                return int(Qt.AlignRight | Qt.AlignVCenter)
            if index.column() == PER_COL:
                return Qt.AlignCenter

        return None

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if section == FOOD_ID_COL:
                    return "Id"
                elif section == NAME_COL:
                    return "Food"
                elif section == PRICE_COL:
                    return "Price"
                elif section == PRICE_QUANTITY_COL:
                    return 'Amount'
                elif section == MIN_COL:
                    return "At least"
                elif section == MAX_COL:
                    return "At most"
                elif section == TARGET_COL:
                    return "Equal to"
                elif section == NUT_QUANT_COL:
                    return "Amount"


            if role == Qt.TextAlignmentRole:
                if section in (NAME_COL, PRICE_UNIT_COL):
                    return int(Qt.AlignLeft | Qt.AlignVCenter)
                if section in (PRICE_COL, PRICE_QUANTITY_COL, MIN_COL, MAX_COL, TARGET_COL, NUT_QUANT_COL):
                    return int(Qt.AlignRight | Qt.AlignVCenter)

        return None

    def insertRows(self, position, food, count=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + count - 1)
        for row in range(count):
            self.foods.append(food)
        self.endInsertRows()

        return True

    def removeRows(self, row, count=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), row, row + count - 1)
        del self.foods[row:row+count]
        self.endRemoveRows()

        return True

    def setData(self, index, value, role=Qt.EditRole):
        if role != Qt.EditRole:
            return False

        if index.isValid() and 0 <= index.row() < len(self.foods):
            food = self.foods[index.row()]
            attr_str = f_col_to_attr[index.column()]
            if attr_str in ('price', 'price_quantity', 'min', 'max', 'target', 'nut_quantity'):
                if value == None:
                    setattr(self.foods[index.row()], attr_str, None)
                else:
                    value = float(value)
            setattr(self.foods[index.row()], attr_str, value)
            self.dataChanged.emit(index, index, [])
            return True

        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        # Cannot edit name, per col
        if index.column() in (NAME_COL, PER_COL):
            return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | ~Qt.ItemIsEditable)
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable)
