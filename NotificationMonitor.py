import threading
import webbrowser
import praw
import time

import wx
from Login import *
TRAY_TOOLTIP = 'System Tray Demo'
TRAY_ICON = 'icon.png'
r = praw.Reddit('Reminds user when he has a notification'
                'by /u/echocage')
username = 'echocage'
r.login(username = username,password = Login(username))
already_done = []


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item
class TaskBarIcon(wx.TaskBarIcon):
    def work(self):
        while True:
            for i in r.get_unread(limit = None):
                if not already_done.__contains__(i):
                    if i.was_comment :
                        self.ShowBalloon("Comment",i.author.__str__() + ": " + i.__str__())
                    else:
                        self.ShowBalloon("Message",i.__str__())
                    already_done.append(i)
            time.sleep(10)
    def __init__(self):
        threading.Timer(0.25, self.work).start()
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Get Notifications', self.on_hello)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):
        webbrowser.open('http://www.reddit.com/message/inbox/')

    def on_hello(self, event):
        for i in r.get_unread(limit = None):
                    if i.was_comment :
                        self.ShowBalloon("Comment",i.author.__str__() + ": " + i.__str__())
                    else:
                        self.ShowBalloon("Message",i.__str__())
        time.sleep(2)

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)


app = wx.PySimpleApp()
TaskBarIcon()
app.MainLoop()

