# -*- coding: utf-8 -*-

import win32gui
import webbrowser
from urllib import parse

target = " - foobar2000"

def getFoobar2000(x, y):
    if(str(win32gui.GetWindowText(x)).find(target) >= 0):
        y.append(x)

window = []
win32gui.EnumWindows(getFoobar2000, window)

if(len(window) == 1):
    title = win32gui.GetWindowText(window[0])
    tweet = "Now Playing: {0}".format(str(title).replace(target, ""))
    url = "https://twitter.com/intent/tweet?text={0}".format(parse.quote(tweet))
    webbrowser.open(url)
