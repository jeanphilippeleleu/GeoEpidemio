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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Geo-epidemiologie"
def description():
    return "calcul du nombre de personne-annees et des taux d'incidences"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load GeoEpidemio class from file GeoEpidemio
    from geoepidemio import GeoEpidemio
    return GeoEpidemio(iface)
