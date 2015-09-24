#!/usr/bin/python
# -*- coding: utf-8 -*-

#from qt import *
from PyQt4 import QtCore, QtGui
from yapsy.PluginManager import PluginManager
import projectFrame
import logging
import sys
from PluginMngr import *
from ProjectTab import *
import time
import datetime
from astropy.time import Time
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)
log = logging.getLogger('yapsy')


class ExtensionAdmin(object):
    def __init__(self):
        self.ExtensionId = []
        self.ExtensionType = []
        self.ExtensionClass = []
        self.ExtensionName = []
        self.ExtensionUserName = []
        self.ExtensionLoaded = []

    def NewExtension(self, Type = 0, Class = None, Name = None, UserName = None, Loaded = False):
        self.ExtensionId.append(len(self.ExtensionId)+1)
        self.ExtensionType.append(Type)
        self.ExtensionClass.append(Class)
        self.ExtensionName.append(Name)
        self.ExtensionUserName.append(UserName)
        self.ExtensionLoaded.append(Loaded)

    def GetByID(self, id):
        return(self.ExtensionType[id],self.ExtensionClass[id],self.ExtensionName[id],self.ExtensionUserName[id],self.ExtensionLoaded[id])


class Communicator(QtCore.QThread):
    def __init__(self, parent = None):
        super(Communicator, self).__init__()
        self.exiting = False
        self.parent= parent

    def __del__(self):
        print "Communicator ukoncovani ..."
        self.exiting = True
        self.wait()

    def run(self):
        n = 0
        while not self.exiting:
            time.sleep(0.5)
            try:
                string = "Local time:" + str(Time.now().iso) + ", Julian date:" + str(Time(datetime.datetime.utcnow(), scale='utc').jd )
                #self.parent.statusBar.showMessage(string)
            except Exception, e:
                print "merrer", e
        print "Communicator ukoncen"



class MainWindow(QtGui.QMainWindow):
    def __init__(self, arg, app):
        super(QtGui.QMainWindow, self).__init__(arg)
        self.mainThread = Communicator(self)

        self.LoadedExtensions = []
        self.AvialibleExtensions = []
        self.ExtensionsClass = {}
        self.Extensions = {}

        self.manager = PluginManager()
        self.manager.setPluginPlaces(["extensions"])
        self.manager.collectPlugins()

        self.extension = ExtensionAdmin()

        self.setWindowTitle("TelescopeTools")
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.resizeEvent = self.onResize
        self.setGeometry(QtCore.QRect(20, 40, 950, 700))
        app_icon = QtGui.QIcon()
        app_icon.addFile('media/icon.png', QtCore.QSize(48,48))
    #   app_icon.addFile('gui/icons/24x24.png', QtCore.QSize(24,24))
    #   app_icon.addFile('gui/icons/32x32.png', QtCore.QSize(32,32))
    #   app_icon.addFile('gui/icons/48x48.png', QtCore.QSize(48,48))
    #   app_icon.addFile('gui/icons/256x256.png', QtCore.QSize(256,256))
        app.setWindowIcon(app_icon)

        self.statusBar = self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.MenuItemPluginsMng())
        fileMenu.addAction(self.MenuItemExitApp())

        MainLayout = QtGui.QHBoxLayout(self)
        self.MainTabs=QtGui.QTabWidget(self)
        self.MainTabs.setEnabled(True)
        self.MainTabs.setTabPosition(QtGui.QTabWidget.North)
        self.MainTabs.addTab(ProjectTab(self),"Project")

        MainLayout.addWidget(self.MainTabs,1)
        self.setLayout(MainLayout)
        self.show()
        self.mainThread.start()



    def ToggleFS(self):
        if self.windowState() & QtCore.Qt.WindowFullScreen:
            self.showNormal()
        else:
            self.showFullScreen()

    def MenuItemExitApp(self):
        Item = QtGui.QAction(QtGui.QIcon(''), '&Exit', self)
        Item.setShortcut('Ctrl+Q')
        Item.setStatusTip('Exit application')
        Item.triggered.connect(QtGui.qApp.quit)
        return Item

    def MenuItemPluginsMng(self):
        print self
        Item = QtGui.QAction(QtGui.QIcon(''), '&Plugins', self)
        Item.setShortcut('Ctrl+M')
        Item.setStatusTip('Open plugin manager')
        Item.triggered.connect(lambda: PluginMngr(self.manager, self))
        return Item

    def  onResize(self, widget):
        self.MainTabs.setGeometry(2, 2, widget.size().width()-5, widget.size().height()-25)
        print 2, 2, widget.size().height()-2, widget.size().width()-2
        for x in self.Extensions:
            print " e:", x, self.Extensions[x], self.Extensions[x].name
            try:
                self.Extensions[x].scrollArea.resize(widget.size().width()-5, widget.size().height()-5)
            except Exception, e:
                self.Extensions[x].contentWidget.resize(widget.size().width()-5, widget.size().height()-5)

class TelescopeTools(object):
    def __init__(self, arg):
        app = QtGui.QApplication(sys.argv)
        sshFile="media/night.style"
        with open(sshFile,"r") as fh:
            app.setStyleSheet(fh.read())
        mWindow = MainWindow(arg, app)
        sys.exit(app.exec_())
        

def  main():
    TT = TelescopeTools(None)
    #TT.init()
   # TT.show()
