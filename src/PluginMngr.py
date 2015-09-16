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

        self.ExtensionsClass = {}
        self.ExtensionsClassNames = []
        self.ExtensionsClassToLoad = {}

        for plugin in manager.getAllPlugins():
            print plugin
            item = QtGui.QStandardItem(plugin.plugin_object.name)
            self.treemodelA.appendRow(item)
            self.ExtensionsClass[plugin.plugin_object.name] = (plugin.plugin_object)
            self.ExtensionsClassNames.append(plugin.plugin_object.name)

        #self.treeviewA.clicked.connect(lambda: self.PluginAdd())
        #self.treeviewA.doubleclicked.connect(lambda: self.PluginAdd())
        AddButton.clicked.connect(lambda: self.PluginAdd(type=1))
        RemButton.clicked.connect(lambda: self.PluginAdd(type=2))
        okButton.clicked.connect(lambda: self.save())

    def PluginAdd(self, item = None, type = None):
        print "aaaaa", item, type
        if type == 1:
            row = self.treeviewA.selectedIndexes()[0].row()
            print self.ExtensionsClass[self.ExtensionsClassNames[row]].getName()
            self.ExtensionsClassToLoad[self.ExtensionsClass[self.ExtensionsClassNames[row]].name] = self.ExtensionsClass[self.ExtensionsClassNames[row]]


        if type == 2:
            print "rem", self.treeviewB.selectedIndexes()

        #self.treeviewB.clear()
        for name in self.ExtensionsClassToLoad:
            item = QtGui.QStandardItem(self.ExtensionsClass[name].name)
            self.treemodelB.appendRow(item)



    def save(self):
        for x in self.ExtensionsClassToLoad:
            print x, ": ", self.ExtensionsClass[x]
            self.parent.MainTabs.addTab(self.ExtensionsClass[x].show(), str(x))


