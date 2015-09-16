#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class PluginMngr(QtGui.QDialog):
    def __init__(self, manager, parent = None):
        super(PluginMngr, self).__init__(parent)
        self.setWindowTitle('Extension manager')
        self.manager = manager
        self.parent = parent

        self.treeviewA = QtGui.QListView()
        self.treemodelA = QtGui.QStandardItemModel()
        self.treeviewA.setModel(self.treemodelA)

        self.treeviewB = QtGui.QListView()
        self.treemodelB = QtGui.QStandardItemModel()
        self.treeviewB.setModel(self.treemodelB)

        AddButton = QtGui.QPushButton(">>")
        RemButton = QtGui.QPushButton("<<")
        Vbox_button = QtGui.QVBoxLayout()
        Vbox_button.addStretch(1)
        Vbox_button.addWidget(AddButton)
        Vbox_button.addWidget(RemButton)
        Vbox_button.addStretch(1)

        okButton = QtGui.QPushButton("OK")
        #cancelButton = QtGui.QPushButton("Cancel")
        
        hbox_list = QtGui.QHBoxLayout()
        hbox_list.addWidget(self.treeviewA)
        hbox_list.addLayout(Vbox_button)
        hbox_list.addWidget(self.treeviewB)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        #hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox_list)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        self.show()

        for plugin in manager.getAllPlugins():
            item = QtGui.QStandardItem(plugin.name)#self.manager.activatePluginByName(plugin.name)
            self.treemodelA.appendRow(item)            #def NewExtension(self, type = 0, class = None, Name = None, UserName = None, Loaded = False):
            try:
                self.manager.activatePluginByName(plugin.name)
            except Exception, e:
                raise e

        self.treeviewB.clicked.connect(self.PluginAdd)
        AddButton.clicked.connect(lambda: self.PluginAdd(type=1))
        RemButton.clicked.connect(lambda: self.PluginAdd(type=2))

    def PluginAdd(self, item = None, type = None):
        print "aaaaa", item, type
        if type == 1:
            print "add", self.treeviewA.selectedIndexes()
            #self.parent.extension.NewExtension(None, 0, plugin.name, "test", False)
            self.parent.MainTabs.addTab(ProjectTab(self.parent), "ahok")

        if type == 2:
            print "rem", self.treeviewB.selectedIndexes()
