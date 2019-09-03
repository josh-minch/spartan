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

class RequirementsModel(QAbstractTableModel):
    def __init__(self, parent=None, nutrients=None):
        super().__init__(parent)
        self.nutrients = nutrients

    def rowCount(self, index=QModelIndex()):
        return len(self.nutrients)
    
    def columnCount(self, index=QModelIndex()):
        return len(R_COL_TO_ATTR)

    def data(self, index, role):
        if not index.isValid() or not 0 <= index.row() < len(self.nutrients):
            return None

        if role == Qt.DisplayRole or role == Qt.EditRole:
            name = self.nutrients[index.row()]["name"]
            min = self.nutrients[index.row()]["min"]
            #min_unit = self.nutrients[index.row()]["min_unit"]
            #max = self.nutrients[index.row()]["max"]
            #max_unit = self.nutrients[index.row()]["max_unit"]

            if index.column() == R_NAME_COL:
                return name
            elif index.column() == R_MIN_COL:
                return min
            #elif index.column() == R_MIN_UNIT_COL:
            #    return min_unit
         
        # A bug in PySide2 requires that we cast the bitwise 
        # AlignmentFlag to an int before returning
        # https://bugreports.qt.io/browse/PYSIDE-20

        if role == Qt.TextAlignmentRole:
            if index.column() == R_MIN_COL:
                return int(Qt.AlignRight | Qt.AlignVCenter)
      
        return None

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if section == R_NAME_COL:
                    return "Nutrient"
                elif section == R_MIN_COL:
                    return "Recommended"
                elif section == R_MIN_UNIT_COL:
                    return
                
            if role == Qt.TextAlignmentRole:
                if section == R_MIN_COL:
                    return int(Qt.AlignRight | Qt.AlignVCenter)
    
        return None

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self.nutrients.insert(position + row, {"name":"", "min":"",})
                                        
        self.endInsertRows()
       
        return True
        
    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        del self.nutrients[position:position+rows]
        self.endRemoveRows()
       
        return True

    def setData(self, index, value, role=Qt.EditRole):
        if role != Qt.EditRole:
            return False

        if index.isValid() and 0 <= index.row() < len(self.nutrients):
        
            nutrient = self.nutrients[index.row()]

            if index.column() == R_NAME_COL:
                nutrient['name'] = value
            elif index.column() == R_MIN_COL:
                nutrient['min'] = value
            else:
                return False

            self.dataChanged.emit(index, index)
            return True

        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) |
                            ~Qt.ItemIsEditable)