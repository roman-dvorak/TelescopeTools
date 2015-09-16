#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui


class ProjectTab(QtGui.QWidget):
    def __init__(self, parent):
        super(ProjectTab, self).__init__()
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
        General.addWidget(laImage)
        General.addWidget(QtGui.QLabel("Project:"))
        General.addWidget(btOpenProject)
        General.addWidget(btNewProject)
        General.addWidget(btSaveProject)
        General.addStretch(1)
        General.addWidget(btExtensionManager)
        GeneralGroup.setLayout(General)

        ProjectGroup = QtGui.QGroupBox("MyProject")
        Project = QtGui.QVBoxLayout(self)
        Project.addWidget(QtGui.QLabel("<b>No project opened</b>",self))
        ProjectGroup.setLayout(Project)

        AbouteGroup = QtGui.QGroupBox("Aboute system")
        Aboute = QtGui.QVBoxLayout(self)
        Aboute.addWidget(QtGui.QLabel("system",self))
        AbouteGroup.setLayout(Aboute)

        self.content.addWidget(GeneralGroup)
        self.content.addWidget(ProjectGroup)
        self.content.addWidget(AbouteGroup)
        self.content.addStretch(1)