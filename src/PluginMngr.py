#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import logging

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
        #self.ExtensionsClassNames = []
        self.ExtensionsClassToLoad = {}
        self.ExtensionsClassLoaded = {}
        self.ExtensionsClassLoaded = self.parent.Extensions

        for plugin in self.manager.getAllPlugins():
            print "Exists: ", plugin
            item = QtGui.QStandardItem(plugin.plugin_object.name)
            self.treemodelA.appendRow(item)
            self.ExtensionsClass[plugin.plugin_object.name] = (plugin.plugin_object)

        for index in self.ExtensionsClassLoaded:
            print "Loaded: ",plugin
            plugin = self.ExtensionsClassLoaded[index]
            item = QtGui.QStandardItem(plugin.name)
            self.treemodelB.appendRow(item)

        AddButton.clicked.connect(lambda: self.PluginAdd(type=1))
        RemButton.clicked.connect(lambda: self.PluginAdd(type=2))
        okButton.clicked.connect(lambda: self.save())

    def PluginAdd(self, item = None, type = None):
        if type == 1:
            row = self.treeviewA.selectedIndexes()[0].row()                                         # vybrany radek v QListView
            index = self.manager.getAllPlugins()[row]                                               # YAPSY trida s rozsirenim
            # print "00A:", row, index, index.name, index.plugin_object.name #####>>> 0 <yapsy.PluginInfo.PluginInfo object at 0x7fa999420110> RA_HBSTEP_driver MLAB RA driver
            number = 1
            if index.plugin_object.name in self.ExtensionsClassToLoad:
                print "Jednou to tam uz je.."
                while index.plugin_object.name+str(number) in self.ExtensionsClassToLoad:
                    number += 1
                self.ExtensionsClassToLoad[index.plugin_object.name+str(number)] = index
            else:
                self.ExtensionsClassToLoad[index.plugin_object.name] = index

        if type == 2:
            row = self.treeviewB.selectedIndexes()[0].row()
            index = self.ExtensionsClassLoaded[row]
            print "2>00A", row, index, index.name, index.plugin_object.name
            self.ExtensionsClassToLoad.pop(index.plugin_object.name)

        self.treemodelB.clear()
        for name in self.ExtensionsClassToLoad:
            item = QtGui.QStandardItem(self.ExtensionsClass[name].name)
            self.treemodelB.appendRow(item)
        for name in self.ExtensionsClassLoaded:
            item = QtGui.QStandardItem(self.ExtensionsClass[name].name)
            self.treemodelB.appendRow(item)


    def save(self):
        for x in self.ExtensionsClassToLoad:
            print x, ": ", self.ExtensionsClass[x]
            self.parent.MainTabs.addTab(self.ExtensionsClass[x].show(self.parent), str(x))
            self.parent.Extensions[x] = self.ExtensionsClass[x]
        self.close()
