#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import wx.lib.scrolledpanel as scrolled
from PIL import Image

class HomeScreen(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        print parent
        print self



class TabPanel(wx.Panel):
    """
    This will be the first notebook tab
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)

        self.SetSizer(sizer)

class Listbook(wx.Listbook):
    def __init__(self, parent):
        """Constructor"""
        wx.Listbook.__init__(self, parent, wx.ID_ANY, style=
                            wx.BK_DEFAULT
                            #wx.BK_TOP
                            #wx.BK_BOTTOM
                            #wx.BK_LEFT
                            #wx.BK_RIGHT
                            )
        # make an image list using the LBXX images
        il = wx.ImageList(32, 32)
        #for x in range(3):
        #    obj = getattr(Image, 'LB%02d' % (x+1))
        #    bmp = obj.GetBitmap()
        #    il.Add(bmp)
        self.AssignImageList(il)
 
        pages = [(TabPanel(self), "Panel One"),
                 (TabPanel(self), "Panel Two"),
                 (TabPanel(self), "Panel Three")]
        #imID = 0
        for page, label in pages:
            self.AddPage(page, label)
 
        self.Bind(wx.EVT_LISTBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_LISTBOOK_PAGE_CHANGING, self.OnPageChanging)
 
    #----------------------------------------------------------------------
    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print 'OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel)
        event.Skip()
 
    #----------------------------------------------------------------------
    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print 'OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel)
        event.Skip()
 
class Settings(wx.Frame):
    def __init__(self, setting):
        self.setting = setting
        wx.Frame.__init__(self, setting, title="Second Frame")
        panel = wx.Panel(self)
        #txt = wx.StaticText(panel, label="I'm the second frame!")

        blist = Listbook(panel)

        

    def onCancel(self, e):
        self.EndModal(wx.ID_CANCEL)

    def onOk(self, e):
        for i in range(3):
            self.settings[i] = self.checkboxes[i].GetValue()
        self.EndModal(wx.ID_OK)

    def GetSettings(self):
        return self.settings

'''
class window2(wx.Frame):

title = "new Window"

def __init__(self,parent,id):
    wx.Frame.__init__(self, id,'Window2', size=(1000,700))
    panel=wx.Panel(self, -1)

    self.SetBackgroundColour(wx.Colour(100,100,100))
    self.Centre()
    self.Show()
'''
        

