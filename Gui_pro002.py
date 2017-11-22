import wx


# class MyDialog(wx.Dialog):
#     def __init__(self, parent, title):
#         super(MyDialog, self).__init__(parent, title=title, size=(250, 150))
#         panel = wx.Panel(self)
#         self.btn = wx.Button(panel, wx.ID_OK, label="ok", size=(50, 20), pos=(75, 50))
#

class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(500, 250))# размер фрейма

        self.InitUI()

    def InitUI(self):
        nb = wx.Notebook(self)

        nb.AddPage(MyPanel1(nb), "Editor") # nb - это первая строка  nb = wx.Notebook(self) тип панели ноутбук
        nb.AddPage(MyPanel2(nb), "RadioButtons")
        nb.AddPage(MyPanel3(nb), "RadioButtons2")
        self.Centre()
        self.Show(True)


class MyPanel1(wx.Panel):
    def __init__(self, parent):
        super(MyPanel1, self).__init__(parent)
        text = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(500, 250)) # размер едитора


class MyPanel2(wx.Panel):
    def __init__(self, parent):
        super(MyPanel2, self).__init__(parent)
        lblList = ['Value X', 'Value Y', 'Value Z']
        rbox = wx.RadioBox(self, label='RadioBox', pos=(25, 10), choices=lblList,
                           majorDimension=1, style=wx.RA_SPECIFY_ROWS)

class MyPanel3(wx.Panel):
    def __init__(self, parent):
        super(MyPanel3, self).__init__(parent)
        lblList = ['Value X', 'Value Y', 'Value Z']
        rbox = wx.RadioBox(self, label='RadioBox', pos=(25, 10), choices=lblList,
                           majorDimension=1, style=wx.RA_SPECIFY_ROWS)
ex = wx.App()
Mywin(None, 'NoteBook demo')
ex.MainLoop()