#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:57:06 2018

@author: victor
"""

from tkinter import *
from Class.Header import Header
from Class.Login import Login

root = Tk()
#root.title("{} - Project Scorpion".format("""name"""))
screen = Header(root)
perfil = Login(screen)
root.minsize(400,500)
root.geometry("800x500")
root.mainloop()
root.destroy()