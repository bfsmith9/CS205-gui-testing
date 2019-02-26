#! /anaconda3/bin/python

import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size = (350,200))
# Create a new app; don't redirect stdout/stderr to a window
app = wx.App(redirect=True)
# A Frame is a top-level window
top = Frame("Hello world!")
# Show the frame
top.Show()
app.MainLoop()
