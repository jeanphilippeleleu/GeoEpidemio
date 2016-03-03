"""
/***************************************************************************
 GeoEpidemio
                                 A QGIS plugin
 calcul du nombre de personne-annees et des taux d'incidences
                              -------------------
        begin                : 2012-10-23
        copyright            : (C) 2012 by leleu jean-philippe
        email                : jean-philippe.leleu2@wanadoo.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import webbrowser
import csv
import numpy as np
import matplotlib.pyplot as plt
from math import *
import os, sys
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from paDialog import PADialog
#from nbPersonneAnnee import Recensement, CalculPersonneAnnee
from nbCasClasseAgeDialog import NbCCADialog
from TIDialog import TIDialog
from casAttenduDialog import CasAttenduDialog
from nbPersAnnee import Requete

class GeoEpidemio:

    def __init__(self, iface): 
        self.iface = iface #reference a l'interface de qgis
        self.pa = PADialog() # fenetre personne annee
        self.nbCCA=NbCCADialog() #fenentre nombre de cas par classes d'age
        self.TIDialog=TIDialog() #fenetre taux d'incidence
        self.casAttDialog=CasAttenduDialog() #fenetre nombre de cas attendu
        
        self.rep_travail=os.environ["HOME"] #repertoire utilisateur en cour linux et windows
        self.nomFichierOuvrir1=''
        self.nomFichierOuvrir2=''
        self.nomFichier='' # utiliser par la boite de dialogue enregistrer sous...
        self.classeAgeItem=['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95et+']
    
    def initGui(self):
        #cree une action
        self.carteAction=QAction(u"Afficher la carte", self.iface.mainWindow())
        self.PAAction=QAction("Nombre de personnes-annees", self.iface.mainWindow())
        self.nbCasClasseAgeAction=QAction("Nombre de cas par classes d'ages", self.iface.mainWindow())
        self.TIAction=QAction("Taux d'incidence", self.iface.mainWindow())
        self.CasAttendusAction=QAction("Nombre de cas attendus", self.iface.mainWindow())
        self.AideAction=QAction("Aide", self.iface.mainWindow())
        self.AproposAction=QAction("A propos", self.iface.mainWindow())

        # connecte l'action a une fonction dans le menu des plugins
        QObject.connect(self.carteAction, SIGNAL("triggered()"), self.carte)
        QObject.connect(self.PAAction, SIGNAL("triggered()"), self.PA)
        QObject.connect(self.nbCasClasseAgeAction, SIGNAL("triggered()"), self.nbCasClasseAge)
        QObject.connect(self.TIAction, SIGNAL("triggered()"), self.TI)
        QObject.connect(self.CasAttendusAction, SIGNAL("triggered()"), self.CasAttendus)
        QObject.connect(self.AideAction, SIGNAL("triggered()"),self.Aide)
        QObject.connect(self.AproposAction, SIGNAL("triggered()"), self.Apropos)
        
        # connecte l'action a une fonction dans les differentes fenetres du plugins
        QObject.connect(self.pa.pushButton, SIGNAL("clicked()"), self.enregistrerSous)
        QObject.connect(self.nbCCA.BEnregistrer, SIGNAL("clicked()"), self.enregistrerSous)
        QObject.connect(self.TIDialog.BNbCasOuvrir, SIGNAL("clicked()"), self.ouvrir1)
        QObject.connect(self.TIDialog.BNbPersOuvrir, SIGNAL("clicked()"), self.ouvrir2)
        QObject.connect(self.TIDialog.BEnregisSous, SIGNAL("clicked()"), self.enregistrerSous)
        QObject.connect(self.casAttDialog.BNbPAOuvrir, SIGNAL("clicked()"), self.ouvrir1)
        QObject.connect(self.casAttDialog.BTIOuvrir, SIGNAL("clicked()"), self.ouvrir2)
        QObject.connect(self.casAttDialog.BEnregistrer, SIGNAL("clicked()"), self.enregistrerSous)
        
        # ajoute l'action a un item ("Geo-epidemiologie") dans le menu des plugins
        self.iface.addPluginToMenu("Geo-epidemiologie", self.carteAction)
        self.iface.addPluginToMenu("Geo-epidemiologie", self.PAAction)
        self.iface.addPluginToMenu("Geo-epidemiologie", self.nbCasClasseAgeAction)
        self.iface.addPluginToMenu("Geo-epidemiologie", self.TIAction)
        self.iface.addPluginToMenu("Geo-epidemiologie", self.CasAttendusAction)
        self.iface.addPluginToMenu("Geo-epidemiologie", self.AideAction)
        self.iface.addPluginToMenu("Geo-epidemiologie", self.AproposAction)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("Geo-epidemiologie", self.carteAction)
        self.iface.removePluginMenu("Geo-epidemiologie", self.PAAction)
        self.iface.removePluginMenu("Geo-epidemiologie", self.nbCasClasseAgeAction)
        self.iface.removePluginMenu("Geo-epidemiologie", self.TIAction)
        self.iface.removePluginMenu("Geo-epidemiologie", self.CasAttendusAction)
        self.iface.removePluginMenu("Geo-epidemiologie", self.AideAction)
        self.iface.removePluginMenu("Geo-epidemiologie", self.AproposAction)
        
        
    #fonction generale#############################################################################       
    def enregistrerSous(self):
        filtre="fichier csv (*.csv)"
        self.nomFichier=QFileDialog.getSaveFileName(None, 'Enregistrer sous', self.rep_travail, filter=filtre)
        self.rep_travail=os.path.dirname(str(self.nomFichier))
        
    def ouvrir1(self):
        self.nomFichierOuvrir1=QFileDialog.getOpenFileName(None, 'Ouverture de fichiers', self.rep_travail)
        self.rep_travail=os.path.dirname(str(self.nomFichierOuvrir1))
        
    def ouvrir2(self):
        self.nomFichierOuvrir2=QFileDialog.getOpenFileName(None, 'Ouverture de fichiers', self.rep_travail)
        self.rep_travail=os.path.dirname(str(self.nomFichierOuvrir2))
             
    def ecriture(self, nomFichier,data, separateur=','):
        """ecrit les donnees au format csv"""
        #mettre .csv a la fin du nom
        f=open(nomFichier+".csv", 'w')
        writer=csv.writer(f, delimiter=separateur)
        writer.writerows(data)
        f.close()
    
    def lectureDeFichier(self, nomFichier):
        """lit et retourne un fichier au format txt"""
        f=open(nomFichier, 'r')
        data=f.readlines()
        f.close()
        return data
        
    def nomCouche(self,nomFichier):
        """renvois le nom du fichier sans le chemin ni l'extention"""
        nom=os.path.basename(str(nomFichier))
        nom=nom.split('.')[0]
        return str(nom) 
       
    def carte(self):
        """ajoute la carte des communes de france au caneva"""
        chemin= os.path.join(os.environ["HOME"], '.qgis2','python', 'plugins', 'GeoEpidemio', 'data','commune.shp')
        self.iface.addVectorLayer(chemin,'',"ogr")
        
    #module personne annee#################################################################
    def PA(self):
    
        self.pa.show()
        result=self.pa.exec_()
        
        if result == 1:
            # recupere le code INSEE a partir de la couche courrante ds qgis
            couche=self.iface.mapCanvas().currentLayer()
            obj=couche.getFeatures()
            nbObj=float(couche.featureCount())
            i=1
            
            INSEE=[]
            if couche.name() == 'commune':
                #INSEE=[x[0] for x in obj]
                for x in obj:
                    INSEE.append(x[0])
                    pc=100*(i/nbObj)
                    self.iface.mainWindow().statusBar().showMessage("Processed {} %".format(int(pc)))
                    i+=1
            else:
                #QMessageBox.information(None, 'Information', 'Aucun objet n\'est selectionne')
                self.iface.messageBar().pushMessage("La couche \'commune\' n\'est la couche active ou n\'est pas presente", level=1)
                return
                
            # recuperation des donnees du formulaire##########################################    
            sexe = self.pa.comboBoxSexe.currentText()
            if sexe == 'Homme':
                sexe=['H']
            elif sexe == 'Femme':
                sexe=['F']
            elif sexe == 'Les deux':
                sexe=['H','F']
            anneeDebut = int(self.pa.cBDebut.currentText())
            anneeFin = int(self.pa.cBFin.currentText())
            annee=range(anneeDebut, anneeFin)
            typeDeSortie = self.pa.comboBox.currentText()
            
            #verifie que les numero INSEE sont identique pour les differentes annees et le sexe
            INSEEcommun=set(INSEE)
            INSEEdiff=[]
            for s in sexe:
                for an in annee:
                    setINSEE=set(Requete(s,an,INSEE).INSEE)
                    INSEEcommun=INSEEcommun & setINSEE
                    self.iface.mainWindow().statusBar().showMessage("verification:"+str(s)+str(an))
                    self.iface.mainWindow().statusBar().clearMessage()
            INSEEdiff=INSEEcommun ^ set(INSEE)
            INSEEcommun=list(INSEEcommun) 
            if INSEEdiff:
                QMessageBox.information(None, 'Information','Probleme avec le(s) code(s) suivant INSEE: '+str(INSEEdiff))
            
            #fait la somme des tableaux de chaque annee#########################################
            def sumAnnee():
                nbPa=np.zeros((len(INSEEcommun),20), dtype=int)
                for s in sexe:
                    for an in annee:
                        nbPa=nbPa+Requete(s,an,INSEEcommun).nbPersonne
                        self.iface.mainWindow().statusBar().showMessage("annee:"+str(an))
                        self.iface.mainWindow().statusBar().clearMessage()
                return nbPa
                
            INSEE=Requete(sexe[0],annee[0],INSEEcommun).INSEE
            if typeDeSortie == "Classes d'ages": 
                self.ecriture(self.nomFichier, [self.classeAgeItem,np.sum(sumAnnee(), axis=0)])
                self.iface.messageBar().pushMessage("Fichier","cree", level=0, duration=3)
                
            if typeDeSortie == "Matrice":
                entete=['INSEE']+self.classeAgeItem
                res=[[code]+list(val) for code, val in zip(INSEE, sumAnnee())]
                res.insert(0, entete)
                self.ecriture(self.nomFichier, res)
                self.iface.messageBar().pushMessage("Fichier","cree", level=0, duration=3)
                
            if typeDeSortie == "Codes INSEE": 
                nbPa=np.sum(sumAnnee(), axis=1)
                resultat=[[x,y] for x,y in zip(INSEE, nbPa)] 
                resultat.insert(0, ['INSEE', 'valeur'])
                self.ecriture(self.nomFichier, resultat)      
                self.iface.messageBar().pushMessage("Fichier","cree", level=0, duration=3)
                
            if typeDeSortie == "Satscan":
                dictSexe={'H':1, 'F':2}
                ligne=[]
                for s in sexe:
                    for an in annee:
                        tab=Requete(s,an,INSEE).nbPersonne
                        for i in range(0,20):
                            for ind, elem in enumerate(tab):
                                ligne.append([INSEE[ind],an,elem[i],i+1,dictSexe[s]])
                self.ecriture(self.nomFichier, ligne, separateur='\t')
                self.iface.messageBar().pushMessage("Fichier","cree", level=0, duration=3)
                
    
    #module nombre de cas par age##################################################################          
    def nbCasClasseAge(self):
    
        if self.iface.mapCanvas().layer:
            #renvois la liste de couches et l'affiche dans le comboBox
            couches=self.iface.mapCanvas().layers()
            couches=[x.name() for x in couches]
            self.nbCCA.comboBoxCouche.addItems(couches)
        else:
            QMessageBox.information(None, 'Information', 'Aucune couche n\'est presente')
            return
            
        def affichageColonnes(numeroCouche=self.nbCCA.comboBoxCouche.currentIndex()):
            if numeroCouche != -1:
                self.nbCCA.comboBoxChamp.clear()
                couche=self.iface.mapCanvas().layer(numeroCouche)
                provider=couche.dataProvider()
                #colonnes=provider.fields()
                colonnes=provider.fields().toList()
                for champ in colonnes:
                    self.nbCCA.comboBoxChamp.addItem(champ.name())
            else:
                pass
        
        QObject.connect(self.nbCCA.comboBoxCouche, SIGNAL('currentIndexChanged (int)'), affichageColonnes)
        
        def colonneToList(nCouche, nCol):
            #renvois une liste de valeur (un champ) a partir d'un numero de couche et de colonne specifie
            couche=self.iface.mapCanvas().layer(nCouche) 
            obj=couche.getFeatures()
            lCol=[x[nCol] for x in obj ]
            return lCol
            
        
        def nombreDeCas(listeAge):
            #renvois le nombre de cas par classes d'age
            intervalle=[range(0,5), range(5,10), range(10,15), range(15,20),range(20,25),range(25,30),range(30,35),range(35,40),range(40,45),range(45,50),range(50,55),range(55,60),range(60,65),range(65,70),range(70,75),range(75,80),range(80,85),range(85,90),range(90,95),range(95, 130)]
            #listeAge=[int(float(x)) for x in listeAge]
            nombre=[0]*len(intervalle)
            for n in listeAge:
                for i, inter in enumerate(intervalle):
                    if n in inter:
                        nombre[i]+=1
            return nombre
            
        affichageColonnes()
        self.nbCCA.show()
        result=self.nbCCA.exec_()
        
        if result ==1:
            # si la checkboxe 'selection' est cochee
            if self.nbCCA.checkBoxSelection.isChecked():
                selection=self.iface.activeLayer().selectedFeatures()
                
                     #les objet selectionne   [#numero du champ]                      
                valeur=[x[self.nbCCA.comboBoxChamp.currentIndex()] for x in selection]
                colonneTraiter=nombreDeCas(valeur)
            else: 
                colonneaTraiter=colonneToList(self.nbCCA.comboBoxCouche.currentIndex(), self.nbCCA.comboBoxChamp.currentIndex())
                colonneTraiter=nombreDeCas(colonneaTraiter)
            QMessageBox.information(None, 'Information', "Nombre de cas %d" %(sum(colonneTraiter))+"\n"+str(colonneTraiter))
            self.ecriture(self.nomFichier, [self.classeAgeItem, colonneTraiter])   
        else:
            pass
        self.nbCCA.comboBoxCouche.clear()
       
        
    #module taux d'incidence#######################################################################        
    def TI(self):
        self.TIDialog.show()
        
        result=self.TIDialog.exec_()
        if result == 1:
            #recuperer les 2 fichier
            nbCas=self.lectureDeFichier(self.nomFichierOuvrir1)
            nbPers=self.lectureDeFichier(self.nomFichierOuvrir2)
            
            #filtrage de la ligne de resultat
            nbCas=(nbCas[1].rstrip('\r\n')).split(',')
            nbPers=(nbPers[1].rstrip('\r\n')).split(',')
            
            #converti en float
            nbCas=[float(x) for x in nbCas]
            nbPers=[float(x) for x in nbPers]
            
            #divise les 2 listes
            ti=[x/y for x,y in zip(nbCas, nbPers)]
            
            #ecrire le fichier
            self.ecriture(self.nomFichier, [self.classeAgeItem, ti])
            
            #taux brut
            m,n=np.sum(nbCas),np.sum(nbPers)
            p=m/n
            ICsup=p+(1.96*sqrt((p*(1-p))/n))
            ICinf=p-(1.96*sqrt((p*(1-p))/n))
            
            QMessageBox.information(None, 'Information', "Taux d\'incidence brute : %f pour 100 000 pers.an [%f-%f]" % (p*100000, ICinf*100000, ICsup*100000))
            
            #generation du graphique
            if self.TIDialog.CBAffGraph.isChecked():
                plt.plot(np.arange(2.5, 102.5, 5), [x*100000 for x in ti])
                plt.title("Taux d\'incidence")
                plt.xlabel("Age")
                plt.ylabel("Taux pour 100 000 pers. par an")
                plt.show()
                
               
                
        else:
            pass
            
    #module nombre de cas attendu##################################################################  
    def CasAttendus(self):
        self.casAttDialog.show()
        result=self.casAttDialog.exec_()
        if result ==1:
            #recuperer les 2 fichier en entre
            nbPA=self.lectureDeFichier(self.nomFichierOuvrir1)
            ti=self.lectureDeFichier(self.nomFichierOuvrir2)
           
            #filtrage du resultat
                #enleve la fin de ligne et le point virgule
            nbPA=[(x.rstrip('\r\n')).split(',') for x in nbPA]
                #recupere le code insee
            code_insee=[x[0] for x in nbPA]
                #enleve la premiere ligne(classe age) et colonne (code insee) transforme en array pour les calculs
            nbPA=np.array([x[1:] for x in nbPA[1:]], float)
            ti=np.array((ti[1].rstrip('\r\n')).split(','), float)
           
            #calcul
            att=np.sum(ti*nbPA, axis=1)
            attTotal=np.sum(att, axis=0)
            
            #formatage de sortie
            att=list(att)
            att.insert(0,'cas attendu')
            res_format=[[x,y] for x,y in zip(code_insee,att)]
            
            self.ecriture(self.nomFichier, res_format)
            
            # si la checkBox est cocher importe les donnees dans Qgis
            if self.casAttDialog.CB.isChecked():
                self.iface.addVectorLayer(self.nomFichier,self.nomCouche(self.nomFichier),"ogr")
            
            QMessageBox.information(None, 'Information', str(attTotal)+':total cas attendu')
        else:
            pass      
        
    def Aide(self):
        #recherche un fichier html dans le dossier du plugin et l'ouvre dans le browser
        chemin= os.path.join(os.environ["HOME"], '.qgis2','python', 'plugins', 'GeoEpidemio', 'documentation','aide.html')
        webbrowser.open(chemin)
        
        
    def Apropos(self):
        texte="Auteur: Jean-philippe Leleu\n"\
        "mail: jean-philippe.leleu2@wanadoo.fr\n"\
        "Organisation:\n"\
        "Version Python:\n"+str(sys.version)
        
        QMessageBox.information(None, 'A propos de',texte )
        
        
        
