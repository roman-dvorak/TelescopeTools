#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from yapsy.PluginManager import PluginManager
import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)
log = logging.getLogger('yapsy')

class NonePlugin(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "Plugin is not exist", (40,40))


class MainFrame(wx.Frame):

    def __init__(self):
        #wx.Frame.__init__(self, None, title="Telescope tools", size=(300,200))
        self.loaders = []
        self.aligments = []
        self.pointers = []
        self.mounts = []
        self.cameras = []
        self.workers = []
        self.exporters = []

        self.manager = PluginManager()
        self.manager.setPluginPlaces(["plugins"])
        self.manager.collectPlugins()

        print "Available plugins",
        for plugin in self.manager.getAllPlugins():
            self.manager.activatePluginByName(plugin.name)
            print plugin.name, ", ",
            type = plugin.plugin_object.getType()
            if type == 1:
                self.loaders.append(plugin.name)
            if type == 2:
                self.aligments.append(plugin.name)
            if type == 3:
                self.pointers.append(plugin.name)
            if type == 4:
                self.mounts.append(plugin.name)
            if type == 5:
                self.cameras.append(plugin.name)
            if type == 6:
                self.workers.append(plugin.name)
            if type == 7:
                self.exporters.append(plugin.name)


    def Display(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800,600))
        #self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()
        filemenu.Append(wx.ID_NEW,"C&reate project"," Create new project ")
        filemenu.Append(wx.ID_OPEN,"O&pen"," Open project ")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        self.Bind(wx.EVT_BUTTON, self.OnClicked)

        helpmenu = wx.Menu()
        helpmenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        
        self.loadermenu = wx.Menu()
        for loaderName in self.loaders:
            loader = self.manager.getPluginByName(loaderName)
            self.loadermenu.AppendRadioItem(wx.NewId(), loader.plugin_object.getUserName(), "")

        self.aligmentmenu = wx.Menu()
        for loaderName in self.aligments:
            loader = self.manager.getPluginByName(loaderName)
            self.aligmentmenu.AppendRadioItem(wx.NewId(), loader.plugin_object.getUserName(), "")

        self.pointermenu = wx.Menu()
        for loaderName in self.pointers:
            loader = self.manager.getPluginByName(loaderName)
            self.pointermenu.AppendRadioItem(wx.NewId(), loader.plugin_object.getUserName(), "")

        self.mountmenu = wx.Menu()
        for loaderName in self.mounts:
            loader = self.manager.getPluginByName(loaderName)
            self.mountmenu.AppendRadioItem(wx.NewId(), loader.plugin_object.getUserName(), "")

        self.cameramenu = wx.Menu()
        for loaderName in self.cameras:
            loader = self.manager.getPluginByName(loaderName)
            self.cameramenu.AppendRadioItem(wx.NewId(), loader.plugin_object.getUserName(), "")
            
        self.workermenu = wx.Menu()
        for loaderName in self.workers:
            loader = self.manager.getPluginByName(loaderName)
            self.workermenu.AppendRadioItem(wx.NewId(), loader.plugin_object.getUserName(), "")
            
        self.exportmenu = wx.Menu()
        for loaderName in self.exporters:
            loader = self.manager.getPluginByName(loaderName)
            self.exportmenu.AppendRadioItem(wx.NewId(), loader.plugin_object.getUserName(), "")
            
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(filemenu,"&File")
        self.menuBar.Append(self.loadermenu,"&Loader")
        self.menuBar.Append(self.aligmentmenu,"&Aligment")
        self.menuBar.Append(self.pointermenu,"&Pointer")
        self.menuBar.Append(self.mountmenu,"&Mount")
        self.menuBar.Append(self.cameramenu,"&Camera")
        self.menuBar.Append(self.workermenu,"&Processor")
        self.menuBar.Append(self.exportmenu,"&Export")
        self.menuBar.Append(helpmenu,"&Help")
        self.SetMenuBar(self.menuBar)

        self.Bind(wx.EVT_MENU, self.OnClicked, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnClicked, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)
        wx.EVT_MENU(self, wx.ID_EXIT, self.Exit)


        self.notebook = wx.Notebook(self, -1, style=wx.NB_LEFT)


        self.backgroundProject =  wx.BoxSizer(wx.HORIZONTAL)
        self.backgroundLoader  =  wx.BoxSizer(wx.HORIZONTAL)
        self.backgroundAligment = wx.BoxSizer(wx.HORIZONTAL)
        self.backgroundPointer =  wx.BoxSizer(wx.HORIZONTAL)
        self.backgroundMount  =   wx.BoxSizer(wx.HORIZONTAL)
        self.backgroundCamera  =  wx.BoxSizer(wx.HORIZONTAL)
        self.backgroundProcessor =wx.BoxSizer(wx.HORIZONTAL)
        self.backgroundExport  =  wx.BoxSizer(wx.HORIZONTAL)

        '''
        self.notebook.AddPage(NonePlugin, "Project", select=False)
        self.notebook.AddPage(NonePlugin, "Loader", select=False)
        self.notebook.AddPage(NonePlugin, "Aligment", select=True)
        self.notebook.AddPage(NonePlugin, "Pointer", select=False)
        self.notebook.AddPage(NonePlugin, "Mount", select=False)
        self.notebook.AddPage(NonePlugin, "Camera", select=False)
        self.notebook.AddPage(NonePlugin, "Processor", select=False)
        self.notebook.AddPage(NonePlugin, "Export", select=False)
        '''

        wx.EVT_MENU(self, 5006, self.Exit)
        

    def OnClicked(self, event):
        print event, event.GetId()

    def OnAbout(self, event):
        print "about"
        dlg = wx.MessageDialog(self, 'TelescopeTools, Roman Dvořák', 'Aboute', wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def Exit(self, event):
        print "exit", event, event.GetId(), event
        self.Close()

class TelescopeTools(object):
    def __init__(self, arg):
        self.arg = arg

    def init(self):
        self.app = wx.App(False)
        self.frame = MainFrame()
        self.frame.Display("Ahoj")
        self.frame.Show(True)
        self.app.MainLoop()


    def show(self):
        pass
        

def  main():
    TT = TelescopeTools(None)
    TT.init()
   # TT.show()
