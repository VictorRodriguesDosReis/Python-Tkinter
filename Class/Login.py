#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:04:06 2018

@author: victor
"""

from tkinter import *
from MySQLdb import *

class Login:

	## CONSTRUCTOR
	def __init__(self, master):
		self.master = master

		self.frame = Frame(self.master.frame)
		self.frame["bg"] = "#000"
		self.frame.pack(expand=1, ipady=50)
		
		## Set title
		self.title = Label(self.frame)
		self.title["text"] = ("Login")
		self.title["font"] = ("Georgia", "15")
		self.title["bg"] = ("#000")
		self.title["fg"] = ("#ff0")
		self.title.grid(row=0, column=0, columnspan=2, pady=30)
		
		## EMAIL
		## Set label
		self.email = Label(self.frame)
		self.email["text"] = "E-Mail"
		self.email["bg"] = "#000"
		self.email["fg"] = "#fff"
		self.email.grid(row=1, column=0, sticky=W)
		
		self.emailIn = Entry(self.frame)
		self.emailIn.grid(row=1, column=1, pady=10)
		
		## PASSWORD
		## Set label
		self.password = Label(self.frame)
		self.password["bg"] = "#000"
		self.password["fg"] = "#fff"
		self.password["text"] = "Password"
		self.password.grid(row=2, column=0, sticky=W)
		
		self.passwordIn = Entry(self.frame)
		self.passwordIn["show"] = "*"
		self.passwordIn.grid(row=2, column=1, pady=10)
		
		## SUBMIT BUTTON
		self.button = Button(self.frame)
		self.button["width"] = 10
		self.button["text"] = "Submit"
		self.button["bg"] = "#fff"
		self.button["fg"] = "#000"
		self.button["command"] = self.verification
		self.button.grid(row=3, column=0, pady=30)

		## SIGN UP BUTTON
		self.btnSignUp = Button(self.frame)
		self.btnSignUp["text"] = "Sign Up"
		self.btnSignUp["width"] = 10
		self.btnSignUp["bg"] = "#fff"
		self.btnSignUp["fg"] = "#000"
		self.btnSignUp["command"] = self.openSignUp
		self.btnSignUp.grid(row=3, column=1, pady=30, sticky=E)
		
		## WARNING MESSAGE
		self.warning = Label(self.frame)
		self.warning["bg"] = "#000"
		self.warning.grid(columnspan=2, pady=20)
		
	## VERIFY IF THE USER EXISTS IN DATABASE
	def verification(self):
		## Get email and password typed
		email = self.emailIn.get()
		password = self.passwordIn.get()

		## Set the style of warning message
		error = self.warning["fg"] = self.title["fg"] = self.master.header["bg"] = "#f00"
		
		## Try to connect in database and execute the 'select'
		try:
			db = connect("127.0.0.1", "root", "", "python")
			
			cursor = db.cursor()
			
		
			cursor.execute("select email, password, name, sex, id from signup where email = '{}'".format(email))
			em_pw_sx = cursor.fetchone()


		except:
			self.warning["text"] = "Connection error"
			error
			db.close()
			return
			
		db.close()
		  
		if em_pw_sx == None:
			self.warning["text"] = "This user not exists"
			error
		
		elif email == em_pw_sx[0] and password == em_pw_sx[1]:
			self.openPerfil(em_pw_sx[0], em_pw_sx[2], em_pw_sx[3], em_pw_sx[4])
		
		else:
			self.warning["text"] = "Password is wrong"
			error

	## OPEN THE SIGN UP FORM
	def openSignUp(self):
		from Class.Signup import Signup

		self.master.header["bg"] = "#ff0"
		signUp = Signup(self.master)
		self.frame.destroy()

	## OPEN THE PERFIL FORM
	def openPerfil(self, email, name, sex, user_id):
		from Class.Perfil import Perfil

		self.master.header["bg"] = "#ff0"
		perfil = Perfil(self.master, name, email, sex, user_id)
		self.frame.destroy()