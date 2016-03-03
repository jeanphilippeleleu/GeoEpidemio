# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'casAttendu.ui'
#
# Created: Wed Jan  9 10:03:48 2013
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
        Dialog.resize(421, 227)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Nombre de cas attendu", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonBox = QtGui.QDialogButtonBox(Dialog)
        self.ButtonBox.setGeometry(QtCore.QRect(220, 170, 181, 32))
        self.ButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.ButtonBox.setObjectName(_fromUtf8("ButtonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 201, 17))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Taux d\'incidence à appliquer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 211, 17))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Nombre de personnes années", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.BNbPAOuvrir = QtGui.QPushButton(Dialog)
        self.BNbPAOuvrir.setGeometry(QtCore.QRect(300, 20, 97, 27))
        self.BNbPAOuvrir.setText(QtGui.QApplication.translate("Dialog", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))
        self.BNbPAOuvrir.setObjectName(_fromUtf8("BNbPAOuvrir"))
        self.BTIOuvrir = QtGui.QPushButton(Dialog)
        self.BTIOuvrir.setGeometry(QtCore.QRect(300, 70, 97, 27))
        self.BTIOuvrir.setText(QtGui.QApplication.translate("Dialog", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))
        self.BTIOuvrir.setObjectName(_fromUtf8("BTIOuvrir"))
        self.CB = QtGui.QCheckBox(Dialog)
        self.CB.setGeometry(QtCore.QRect(10, 120, 251, 22))
        self.CB.setText(QtGui.QApplication.translate("Dialog", "Importer les données dans QGIS", None, QtGui.QApplication.UnicodeUTF8))
        self.CB.setObjectName(_fromUtf8("CB"))
        self.BEnregistrer = QtGui.QPushButton(Dialog)
        self.BEnregistrer.setGeometry(QtCore.QRect(10, 170, 151, 27))
        self.BEnregistrer.setText(QtGui.QApplication.translate("Dialog", "Enregistrer sous...", None, QtGui.QApplication.UnicodeUTF8))
        self.BEnregistrer.setObjectName(_fromUtf8("BEnregistrer"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.ButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.ButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

class CasAttenduDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self) 
