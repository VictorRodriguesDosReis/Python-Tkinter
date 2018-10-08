#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:03:38 2018

@author: victor
"""

from tkinter import *

class Header:

    ## CONSTRUCTOR
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame["bg"] = ("black")
        self.frame.pack(fill=BOTH, expand=1)
    
        self.header = Label(self.frame)
        self.header["text"] = ("Project Python")
        self.header["font"] = ("Helvatica", "20", "italic", "bold")
        self.header["fg"] = ("#000")
        self.header["bg"] = ("#ff0")
        self.header.pack(fill=X)   