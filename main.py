from controller import Controller
import sys, wx

if __name__ == "__main__":
    app = wx.App()
    c = Controller()
    sys.stdout = sys.__stdout__
    app.MainLoop()
