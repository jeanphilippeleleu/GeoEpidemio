# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TIDialog.ui'
#
# Created: Thu Jan 10 15:46:08 2013
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
        Dialog.resize(520, 255)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Taux incidence", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(320, 200, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lNbCas = QtGui.QLabel(Dialog)
        self.lNbCas.setGeometry(QtCore.QRect(30, 40, 241, 17))
        self.lNbCas.setText(QtGui.QApplication.translate("Dialog", "Nombre de cas (par classes d\'age)", None, QtGui.QApplication.UnicodeUTF8))
        self.lNbCas.setObjectName(_fromUtf8("lNbCas"))
        self.lNbPersAnne = QtGui.QLabel(Dialog)
        self.lNbPersAnne.setGeometry(QtCore.QRect(30, 90, 331, 17))
        self.lNbPersAnne.setText(QtGui.QApplication.translate("Dialog", "Nombre de personnes années (par classes d\'age)", None, QtGui.QApplication.UnicodeUTF8))
        self.lNbPersAnne.setObjectName(_fromUtf8("lNbPersAnne"))
        self.BNbCasOuvrir = QtGui.QPushButton(Dialog)
        self.BNbCasOuvrir.setGeometry(QtCore.QRect(390, 30, 97, 27))
        self.BNbCasOuvrir.setText(QtGui.QApplication.translate("Dialog", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))
        self.BNbCasOuvrir.setObjectName(_fromUtf8("BNbCasOuvrir"))
        self.BNbPersOuvrir = QtGui.QPushButton(Dialog)
        self.BNbPersOuvrir.setGeometry(QtCore.QRect(390, 90, 97, 27))
        self.BNbPersOuvrir.setText(QtGui.QApplication.translate("Dialog", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))
        self.BNbPersOuvrir.setObjectName(_fromUtf8("BNbPersOuvrir"))
        self.CBAffGraph = QtGui.QCheckBox(Dialog)
        self.CBAffGraph.setGeometry(QtCore.QRect(30, 140, 171, 22))
        self.CBAffGraph.setText(QtGui.QApplication.translate("Dialog", "Afficher le graphique", None, QtGui.QApplication.UnicodeUTF8))
        self.CBAffGraph.setObjectName(_fromUtf8("CBAffGraph"))
        self.BEnregisSous = QtGui.QPushButton(Dialog)
        self.BEnregisSous.setGeometry(QtCore.QRect(30, 200, 161, 27))
        self.BEnregisSous.setText(QtGui.QApplication.translate("Dialog", "Enregistrer sous ...", None, QtGui.QApplication.UnicodeUTF8))
        self.BEnregisSous.setObjectName(_fromUtf8("BEnregisSous"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass
class TIDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
