# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nbCasClasseAgeDialog.ui'
#
# Created: Mon Oct 29 18:44:32 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(477, 256)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Nombre de cas par classes d\'ages", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(240, 200, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Dialog", "Couche", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Champ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBoxCouche = QtGui.QComboBox(Dialog)
        self.comboBoxCouche.setGeometry(QtCore.QRect(110, 10, 201, 27))
        self.comboBoxCouche.setObjectName(_fromUtf8("comboBoxCouche"))
        self.comboBoxChamp = QtGui.QComboBox(Dialog)
        self.comboBoxChamp.setGeometry(QtCore.QRect(110, 120, 201, 27))
        self.comboBoxChamp.setObjectName(_fromUtf8("comboBoxChamp"))
        self.BEnregistrer = QtGui.QPushButton(Dialog)
        self.BEnregistrer.setGeometry(QtCore.QRect(20, 200, 151, 27))
        self.BEnregistrer.setText(QtGui.QApplication.translate("Dialog", "Enregistrer sous...", None, QtGui.QApplication.UnicodeUTF8))
        self.BEnregistrer.setObjectName(_fromUtf8("BEnregistrer"))
        self.checkBoxSelection = QtGui.QCheckBox(Dialog)
        self.checkBoxSelection.setGeometry(QtCore.QRect(10, 50, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxSelection.setFont(font)
        self.checkBoxSelection.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxSelection.setText(QtGui.QApplication.translate("Dialog", "ou utiliser la selection", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSelection.setObjectName(_fromUtf8("checkBoxSelection"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 90, 441, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass
        
        
class NbCCADialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)  

