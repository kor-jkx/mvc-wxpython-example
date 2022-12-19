import wx
from pubsub import pub


class View(wx.Frame):
    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, -1, "Main View")

        sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(self, -1, "My Money")
        ctrl = wx.TextCtrl(self, -1, "")
        sizer.Add(text, 0, wx.EXPAND | wx.ALL)
        sizer.Add(ctrl, 0, wx.EXPAND | wx.ALL)

        self.moneyCtrl = ctrl
        ctrl.SetEditable(False)
        self.SetSizer(sizer)

        # subscribe to all "MONEY CHANGED" messages from the Model
        # to subscribe to ALL messages (topics), omit the second argument below
        pub.subscribe(self.setMoney, "money_changed")

    def setMoney(self, money):
        self.moneyCtrl.SetValue(str(money))


class ChangerWidget(wx.Frame):
    CHANGE = 10  # by how much money changes every time click

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, -1, "Changer View")

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.add = wx.Button(self, -1, "Add Money")
        self.remove = wx.Button(self, -1, "Remove Money")
        sizer.Add(self.add, 0, wx.EXPAND | wx.ALL)
        sizer.Add(self.remove, 0, wx.EXPAND | wx.ALL)
        self.SetSizer(sizer)

        self.add.Bind(wx.EVT_BUTTON, self.onAdd)
        self.remove.Bind(wx.EVT_BUTTON, self.onRemove)

    def onAdd(self, evt):
        pub.sendMessage("money_changing", amount=self.CHANGE)

    def onRemove(self, evt):
        pub.sendMessage("money_changing", amount=- self.CHANGE)
