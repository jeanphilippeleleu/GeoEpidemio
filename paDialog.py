# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_geoepidemio.ui'
#
# Created: Tue Oct 23 16:49:24 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PADialog(object):
    def setupUi(self, PADialog):
        listAnnee=["1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
        PADialog.setObjectName(_fromUtf8("PA"))
        PADialog.resize(666, 200)
        PADialog.setWindowTitle(QtGui.QApplication.translate("Calcul du nombre de personnes-années", "Calcul du nombre de personnes-années", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(PADialog)
        self.buttonBox.setGeometry(QtCore.QRect(310, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.comboBoxSexe = QtGui.QComboBox(PADialog)
        self.comboBoxSexe.setGeometry(QtCore.QRect(21, 36, 89, 27))
        self.comboBoxSexe.setObjectName(_fromUtf8("comboBoxSexe"))
        self.comboBoxSexe.addItem(_fromUtf8(""))
        self.comboBoxSexe.setItemText(0, QtGui.QApplication.translate("dialog", "Homme", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxSexe.addItem(_fromUtf8(""))
        self.comboBoxSexe.setItemText(1, QtGui.QApplication.translate("dialog", "Femme", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxSexe.addItem(_fromUtf8(""))
        self.comboBoxSexe.setItemText(2, QtGui.QApplication.translate("dialog", "Les deux", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSexe = QtGui.QLabel(PADialog)
        self.labelSexe.setGeometry(QtCore.QRect(21, 11, 36, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSexe.setFont(font)
        self.labelSexe.setText(QtGui.QApplication.translate("dialog", "Sexe", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSexe.setObjectName(_fromUtf8("labelSexe"))
        self.labelAnnee = QtGui.QLabel(PADialog)
        self.labelAnnee.setGeometry(QtCore.QRect(250, 10, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelAnnee.setFont(font)
        self.labelAnnee.setText(QtGui.QApplication.translate("dialog", "Année", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAnnee.setObjectName(_fromUtf8("labelAnnee"))
        self.label_3 = QtGui.QLabel(PADialog)
        self.label_3.setGeometry(QtCore.QRect(180, 30, 67, 17))
        self.label_3.setText(QtGui.QApplication.translate("dialog", "Début", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(PADialog)
        self.label_4.setGeometry(QtCore.QRect(180, 60, 67, 17))
        self.label_4.setText(QtGui.QApplication.translate("dialog", "Fin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(PADialog)
        self.label_5.setGeometry(QtCore.QRect(350, 30, 67, 17))
        self.label_5.setText(QtGui.QApplication.translate("dialog", "(inclu)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(PADialog)
        self.label_6.setGeometry(QtCore.QRect(350, 60, 67, 17))
        self.label_6.setText(QtGui.QApplication.translate("dialog", "(exclu)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        #self.lineEditDebut = QtGui.QLineEdit(PADialog)
        #self.lineEditDebut.setGeometry(QtCore.QRect(230, 30, 113, 27))
        #self.lineEditDebut.setObjectName(_fromUtf8("lineEditDebut"))
        #self.lineEditDebut.setMaxLength(4)
        #self.lineEditFin = QtGui.QLineEdit(PADialog)
        #self.lineEditFin.setGeometry(QtCore.QRect(230, 60, 113, 27))
        #self.lineEditFin.setObjectName(_fromUtf8("lineEditFin"))
        #self.lineEditFin.setMaxLength(4)
        self.cBDebut = QtGui.QComboBox(PADialog)
        self.cBDebut.setGeometry(QtCore.QRect(230, 30, 113, 27))
        self.cBDebut.addItems(_fromUtf8(listAnnee))
        self.cBFin = QtGui.QComboBox(PADialog)
        self.cBFin.setGeometry(QtCore.QRect(230, 60, 113, 27))
        self.cBFin.addItems(_fromUtf8(listAnnee))
        self.label = QtGui.QLabel(PADialog)
        self.label.setGeometry(QtCore.QRect(450, 10, 110, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("dialog", "Type de sortie", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(PADialog)
        self.comboBox.setGeometry(QtCore.QRect(450, 40, 131, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("dialog", "Classes d\'ages", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("dialog", "Codes INSEE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("dialog", "Matrice", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("dialog", "Satscan", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton = QtGui.QPushButton(PADialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 160, 131, 27))
        self.pushButton.setText(QtGui.QApplication.translate("dialog", "Enregistrer sous", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.retranslateUi(PADialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PADialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PADialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PADialog)

    def retranslateUi(self, PADialog):
        pass 
            
class PADialog(QtGui.QDialog, Ui_PADialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

