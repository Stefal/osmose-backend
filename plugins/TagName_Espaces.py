#-*- coding: utf-8 -*-

###########################################################################
##                                                                       ##
## Copyrights Etienne Chové <chove@crans.org> 2009                       ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see <http://www.gnu.org/licenses/>. ##
##                                                                       ##
###########################################################################

from plugins.Plugin import Plugin


class TagName_Espaces(Plugin):
    
    err_903    = 5010
    err_903_fr = u"Espace surnuméraire"
    err_903_en = u"Too many spaces"
    
    def way(self, data, tags, nds):
        
        err = []
        
        if "name" in tags:
            
            name = tags[u"name"]
            
            if u"  " in name:
                err.append((903, 0, {}))
                
            if name.endswith(u" "):
                err.append((903, 1, {"fr": u"espace à la fin du nom", "en": u"ends with space"}))
                
            if name.startswith(" "):
                err.append((903, 2, {"fr": u"espace au début du nom", "en": u"starts with space"}))

        return err
