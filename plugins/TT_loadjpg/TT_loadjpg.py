#!/usr/bin/python
# -*- coding: utf-8 -*-

from yapsy.IPlugin import IPlugin

class TT_loadjpg(IPlugin):
    def __init__(self):
        self.type = 1   #loader
        self.extensions = ['cr2', 'CR2'] 
        self.UserName = "CANON loader"

    def getType(self):
        return self.type

    def getUserName(self):
        return self.UserName

    def getFilesExtension(self):
        return self.extensions

    def activate(self):
        pass

    def deactivate(self):
        print "Ive been deactivated!"

    def load(self):
        print "loader"