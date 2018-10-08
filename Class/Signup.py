#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:52:16 2018

@author: victor
"""

from tkinter import *
from MySQLdb import *

class Signup:

    ## CONSTRUCTOR
    def __init__(self, master):
        self.master = master

        self.frame = Frame(self.master.frame)
        self.frame["bg"] = ("#000")
        self.frame.pack(expand=1, ipady=50)
        
        ## Set Title
        self.title = Label(self.frame)
        self.title["text"] = "Sign-up"
        self.title["font"] = ("Georgia", "15")
        self.title["fg"] = "#ff0"
        self.title["bg"] = "#000"
        self.title.grid(row=0, column=0, columnspan=3, pady=30)
        
        ## NAME
        ## Set label
        self.name = Label(self.frame)
        self.name["text"] = "Name"
        self.name["bg"] = "#000"
        self.name["fg"] = "#fff"
        self.name.grid(row=1, column=0, sticky=W)
        
        self.nameIn = Entry(self.frame)
        self.nameIn.grid(row=1, column=1, pady=10)
        
        ## E-MAIL
        self.email = Label(self.frame)
        self.email["text"] = "E-mail"
        self.email["bg"] = "#000"
        self.email["fg"] = "#fff"
        self.email.grid(row=2, column=0, sticky=W)
        
        self.emailIn = Entry(self.frame)
        self.emailIn.grid(row=2, column=1, pady=10)
        
        ## PASSWORD
        self.password = Label(self.frame)
        self.password["text"] = "Password"
        self.password["bg"] = "#000"
        self.password["fg"] = "#fff"
        self.password.grid(row=3, column=0, sticky=W)
        
        self.passwordIn = Entry(self.frame)
        self.passwordIn["show"] = "*"
        self.passwordIn.grid(row=3, column=1, pady=10)
        
        ## CONFIRM PASSWORD
        self.confirmPw = Label(self.frame)
        self.confirmPw["text"] = "Confirm password"
        self.confirmPw["bg"] = "#000"
        self.confirmPw["fg"] = "#fff"
        self.confirmPw.grid(row=4, column=0, sticky=W)
        
        self.confirmPwIn = Entry(self.frame)
        self.confirmPwIn["show"] = "*"
        self.confirmPwIn.grid(row=4, column=1, pady=10)
        
        ## SUBMIT BUTTON
        self.button = Button(self.frame)
        self.button["text"] = "Sign Up"
        self.button["width"] = 10
        self.button["bg"] = "#fff"
        self.button["fg"] = "#000"
        self.button["command"] = self.verification
        self.button.grid(row=5, column=0, pady=30)

        ## LOGIN BUTTON
        self.btnLogin = Button(self.frame)
        self.btnLogin["text"] = "Login"
        self.btnLogin["width"] = 10
        self.btnLogin["bg"] = "#fff"
        self.btnLogin["fg"] = "#000"
        self.btnLogin["command"] = self.openLogin
        self.btnLogin.grid(row=5, column=2, pady=30)
        
        ## WARNING MESSAGE
        self.warning = Label(self.frame)
        self.warning["bg"] = "#000"
        self.warning.grid(row=6, column=0, columnspan=3, pady=20)
        
        ## TITLE OF SEX FRAME
        ##  I need to fix these radios, and the frame 
        self.sex = LabelFrame(self.frame)
        self.sex["text"] = "Sex"
        self.sex["bg"] = "#000"
        self.sex["fg"] = "#fff"
        self.sex.grid(row=1, column=2, rowspan=4, padx=30, sticky=N+S+E+W)
        
        # Variable that stores the user Sex
        self.sexVar = StringVar()
        
        ## SEX BUTTON
        Radiobutton(self.sex, text="Male", bg="#000", fg="#fff", variable=self.sexVar, value="M").pack(fill=BOTH, expand=1)
        Radiobutton(self.sex, text="Female", bg="#000", fg="#fff", variable=self.sexVar, value="F").pack(fill=BOTH, expand=1)
        
    ## VERIFY IF THE ENTRIES WAS FILLED CORRECTLY
    def verification(self):
        ## Array to save informations about Name entry
        nm = []
        nm.append(self.nameIn.get())
        nm.append(len(self.nameIn.get()))

        ## Variable to save informations about Email entry
        em = self.emailIn.get()

        ## Array to save informations about Password entry
        pw = []
        pw.append(len(self.passwordIn.get()))
        pw.append(self.passwordIn.get())
        pw.append(self.confirmPwIn.get())
        
        ## Variable to save the user Sex
        sx = self.sexVar.get()
        
        ## Set the style of warning message
        error = self.warning["fg"] = self.title["fg"] = self.master.header["bg"] = "#f00"
        
        if nm[1] < 5:
            self.warning["text"] = "Please type your full name"
            error
            
        elif self.emailExists(em):
            self.warning["text"] = "This e-mail already exists, choose another"
            error
            
        elif '@' not in em or '.com' not in em:
            self.warning["text"] = "E-mail invalid"
            error
            
        elif pw[0] < 5:
            self.warning["text"] = "The password must be at least 5 characters"
            error
            
        elif pw[1] != pw[2]:
            self.warning["text"] = "The passwords need to be equals"
            error
            
        elif not sx:
            self.warning["text"] = "Please select your sex"
            error
        
        else:
            self.register(nm[0], sx, em, pw[1])
            
    ## VERIFY IF THE EMAIL ALREADY EXISTS IN DATABASE   
    def emailExists(self, email):
        ## Try to connect in database and execute the 'select'
        try:
            db = connect("127.0.0.1", "root", "", "python")

            cursor = db.cursor()
            cursor.execute("select exists (select * from signup where email = '{}')".format(email))
            data = cursor.fetchone()
        
        except:
            self.warning["text"] = "Error trying to connect to server"
        
        db.close()

        if data[0]:
            return True
        
        else:
            return False
            
    ## INSERTS THE USER INTO DATABASE
    def register(self, name, sex, email, password):
        ## Try to connect in database and insert the new user
        try:
            db = connect("127.0.0.1", "root", "", "python")
            
            try:               
                cursor = db.cursor()
                    
                cursor.execute("insert into signup (name, sex, email, password) values ('{}', '{}', '{}', '{}');".format(name, sex, email, password))
                db.commit()
                
                self.warning["text"] = "Your register was successful"
                self.warning["fg"] = "#0f0"
                self.title["fg"] = "#0f0"
                self.master.header["bg"] = "#0f0"
                    
            except:
                self.warning["text"] = "Erro in insert the values in database"
                self.warning["fg"] = "#f00"
                self.title["fg"] = "#f00"
                self.master.header["bg"] = "#f00"
                db.roolback()
                db.close()
                return
                
        except:
            self.warning["text"] = "Error trying to connect to server"
            
        db.close()

    ## OPEN THE LOGIN FORM
    def openLogin(self):
        from Class.Login import Login

        self.master.header["bg"] = "#ff0"
        login = Login(self.master)
        self.frame.destroy()
