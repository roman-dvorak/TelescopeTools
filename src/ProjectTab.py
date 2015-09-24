#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PluginMngr import *


class ProjectTab(QtGui.QWidget):
    def __init__(self, parent):
        super(ProjectTab, self).__init__()
        self.parent = parent
        self.horizontalLayout = QtGui.QVBoxLayout(self)
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.contentWidet = QtGui.QWidget()
        self.content = QtGui.QHBoxLayout(self.contentWidet)
        self.scrollArea.setWidget(self.contentWidet)
        self.horizontalLayout.addWidget(self.scrollArea)

        GeneralGroup = QtGui.QGroupBox("TelescopeTools")
        General = QtGui.QVBoxLayout(self)
        General.addWidget(QtGui.QLabel("ahoj",self))
        laImage = QtGui.QLabel("bla", self)
        laImage.setPixmap(QtGui.QPixmap('media/Header.png').scaled(400, 400, QtCore.Qt.KeepAspectRatio))
        btOpenProject = QtGui.QPushButton("Open")
        btNewProject = QtGui.QPushButton("New")
        btSaveProject = QtGui.QPushButton("Save")
        btExtensionManager = QtGui.QPushButton("Extension manager")
        btFullScreen = QtGui.QPushButton("Full screen")
        General.addWidget(laImage)
        General.addWidget(QtGui.QLabel("Project:"))
        General.addWidget(btOpenProject)
        General.addWidget(btNewProject)
        General.addWidget(btSaveProject)
        General.addStretch(1)
        General.addWidget(btExtensionManager)
        General.addWidget(btFullScreen)
        GeneralGroup.setLayout(General)

        ProjectGroup = QtGui.QGroupBox("MyProject")
        Project = QtGui.QVBoxLayout(self)
        Project.addWidget(QtGui.QLabel("<b>No project opened</b>",self))
        ProjectGroup.setLayout(Project)

        AbouteGroup = QtGui.QGroupBox("Aboute system")
        Aboute = QtGui.QVBoxLayout(self)
        Aboute.addWidget(QtGui.QLabel("system",self))
        AbouteGroup.setLayout(Aboute)

       # btn = QtGui.QPushButton("Ahoj Tlacitko")
       # Nbx = QtGui.Q

        self.content.addWidget(GeneralGroup)
        self.content.addWidget(ProjectGroup)
        self.content.addWidget(AbouteGroup)
        self.content.addStretch(1)

        btExtensionManager.clicked.connect(lambda: PluginMngr(parent.manager, parent))
        btOpenProject.clicked.connect(lambda: self.ProjectFile("open"))
        btNewProject.clicked.connect(lambda: self.ProjectFile("new"))
        btFullScreen.clicked.connect(parent.ToggleFS)

    def ProjectFile(self, type):
        if type == "new":
            #fname = QtGui.QFileDialog.getOpenFileName(self, 'New project file', '/home')
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '/home', "TTdata (*.tt *.ttp *.ttd)")
            f = open(fname, 'r')
            print f
            with f:        
                data = f.read()
                print data
                #self.textEdit.setText(data)
