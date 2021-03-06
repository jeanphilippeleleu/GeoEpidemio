# -*- coding:Utf-8 -*-
import sqlite3
import numpy as np
import os
from PyQt4.QtGui import *
class Requete(object):

    def __init__(self,sexe, annee, selection):
        self.sexe=sexe
        self.annee=annee
        self.selection=selection
        self.nomBase=os.path.join(os.environ["HOME"],'.qgis2','python', 'plugins', 'GeoEpidemio', 'data','recensement.sqlite')
        
        self.sql=["SELECT * FROM R"+sexe+str(annee)+" WHERE INSEE = '"+"' OR INSEE = '".join(self.selection[i:i+999]) + "'" for i in range(0, len(selection), 999)]
          
        #self.sql=["SELECT * FROM R"+sexe+str(annee)+" WHERE INSEE = '"+"' OR INSEE = '".join(self.selection) + "' ORDER BY INSEE"]   
        self.donneeBrute=self.connection(self.nomBase, self.sql)
        self.nbPersonne=np.array([x[1:] for x in self.donneeBrute], int)
        self.INSEE=[x[0] for x in self.donneeBrute]
        
    def connection(self, BD, SQL):
        """ conection a la base de donnee, renvois un tableau avec les entetes"""
        entete=[]
        result=[]
        conn=sqlite3.connect(BD)
        c=conn.cursor()
        for req in SQL:
            c.execute(req)
            for ligne in c:
                result.append(list(ligne))
        #for i in c.description:
            #entete.append(i[0])
        #result.append(list(entete))
        c.close()
        conn.close()
        return result
