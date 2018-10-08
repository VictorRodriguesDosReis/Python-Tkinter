#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 1 05:11:21 2018

@author: victor
"""

from tkinter import *
from tkinter import messagebox
from MySQLdb import *
import tkinter.ttk as ttk

class Perfil:

	## CONSTRUCTOR
	def __init__(self, master, name, email, sex, user_id):
		self.master = master
		self.name = name
		self.email = email
		self.sex = sex
		self.id = user_id

		self.frame = Frame(master.frame)
		self.frame["bg"] = "#000"
		self.frame.pack(expand=1, ipady=50)
		
		## Set title
		self.title = Label(self.frame)
		self.title["text"] = ("Welcome Sr.{}".format(name)) if sex == "M" else ("Welcome Sra.{}".format(name))
		self.title["font"] = ("Georgia", "15")
		self.title["bg"] = ("#000")
		self.title["fg"] = ("#ff0")
		self.title.grid(row=0, column=0, columnspan=2, pady=30)
		
		## COLUMN 1 (INFORMATION)
		## Frame column 1
		self.frameColumn1 = Frame(self.frame)
		self.frameColumn1["bg"] = "#000"
		self.frameColumn1.grid(row=1, column=0, padx=40)

		## Set subtitle
		self.lblInformation = Label(self.frameColumn1)
		self.lblInformation["text"] = ("Information");
		self.lblInformation["font"] = ("Georgia", "13")
		self.lblInformation["bg"] = "#000";
		self.lblInformation["fg"] = "#ff0";
		self.lblInformation.pack(fill=BOTH, expand=1, pady=10)

		## NAME
		## Set label
		self.lblName = Label(self.frameColumn1)
		self.lblName["text"] = "Name"
		self.lblName["bg"] = "#000"
		self.lblName["fg"] = "#fff"
		self.lblName.pack(anchor=W)
		
		self.name = StringVar()
		self.name.set(name)

		self.txtName = Entry(self.frameColumn1)
		self.txtName["textvariable"] = self.name
		self.txtName.pack(fill=BOTH, expand=1, anchor=W)

		## EMAIL
		## Set label
		self.lblEmail = Label(self.frameColumn1)
		self.lblEmail["text"] = "E-Mail"
		self.lblEmail["bg"] = "#000"
		self.lblEmail["fg"] = "#fff"
		self.lblEmail.pack(anchor=W)
		
		self.email = StringVar()
		self.email.set(email)

		self.txtEmail = Entry(self.frameColumn1)
		self.txtEmail["textvariable"] = self.email
		self.txtEmail.pack(fill=BOTH, expand=1, anchor=W)

		## SEX
		## Set label
		self.lblSex = Label(self.frameColumn1)
		self.lblSex["text"] = "Sex"
		self.lblSex["bg"] = "#000"
		self.lblSex["fg"] = "#fff"
		self.lblSex.pack(anchor=W)

		## Set Combobox
		self.cmbSex = ttk.Combobox(self.frameColumn1)
		self.cmbSex["values"] = ("Male", "Female")
		self.cmbSex.set("Male")
		self.cmbSex.pack(fill=BOTH, expand=1, anchor=W)

		## COLUMN 2 (PASSWORD)
		## Frame column 2
		self.frameColumn2 = Frame(self.frame)
		self.frameColumn2["bg"] = "#000"
		self.frameColumn2.grid(row=1, column=1, padx=40)

		## Set subtitle
		self.lblChangePassword = Label(self.frameColumn2)
		self.lblChangePassword["text"] = ("Change Password");
		self.lblChangePassword["font"] = ("Georgia", "13")
		self.lblChangePassword["bg"] = "#000";
		self.lblChangePassword["fg"] = "#ff0";
		self.lblChangePassword.pack(fill=BOTH, expand=1, pady=10)

		## CURRENT PASSWORD
		## Set label
		self.lblCurrentPassword = Label(self.frameColumn2)
		self.lblCurrentPassword["bg"] = "#000"
		self.lblCurrentPassword["fg"] = "#fff"
		self.lblCurrentPassword["text"] = " Current Password"
		self.lblCurrentPassword.pack(anchor=E)
		
		self.txtCurrentPassword = Entry(self.frameColumn2)
		self.txtCurrentPassword["show"] = "*"
		self.txtCurrentPassword.pack(fill=BOTH, expand=1, anchor=E)

		## NEW PASSWORD 
		## Set label
		self.lblNewPassword = Label(self.frameColumn2)
		self.lblNewPassword["bg"] = "#000"
		self.lblNewPassword["fg"] = "#fff"
		self.lblNewPassword["text"] = "New Password"
		self.lblNewPassword.pack(anchor=E)
		
		self.txtNewPassword = Entry(self.frameColumn2)
		self.txtNewPassword["show"] = "*"
		self.txtNewPassword.pack(fill=BOTH, expand=1, anchor=E)

		## CONFIRM NEW PASSWORD 
		## Set label
		self.lblConfirmNewPassword = Label(self.frameColumn2)
		self.lblConfirmNewPassword["bg"] = "#000"
		self.lblConfirmNewPassword["fg"] = "#fff"
		self.lblConfirmNewPassword["text"] = "Confirm New Password"
		self.lblConfirmNewPassword.pack(anchor=E)
		
		self.txtConfirmNewPassword = Entry(self.frameColumn2)
		self.txtConfirmNewPassword["show"] = "*"
		self.txtConfirmNewPassword.pack(fill=BOTH, expand=1, anchor=E)

		## Set button update account information
		self.btnUpdate = Button(self.frame)
		self.btnUpdate["text"] = "Update information"
		self.btnUpdate["width"] = 20
		self.btnUpdate["bg"] = "#fff"
		self.btnUpdate["fg"] = "#000"
		self.btnUpdate["command"] = self.verifyInformation
		self.btnUpdate.grid(row=2, column=0, pady=30)

		## Set button change current password
		self.btnChangePassword = Button(self.frame)
		self.btnChangePassword["text"] = "Update password"
		self.btnChangePassword["width"] = 20
		self.btnChangePassword["bg"] = "#fff"
		self.btnChangePassword["fg"] = "#000"
		self.btnChangePassword["command"] = self.verifyPassword
		self.btnChangePassword.grid(row=2, column=1, pady=30)

		## WARNING MESSAGE
		self.lblWarning = Label(self.frame)
		self.lblWarning["bg"] = "#000"
		self.lblWarning["fg"] = "#000"
		self.lblWarning.grid(row=3, column=0, columnspan=2)

		## Set button logout
		self.btnDeslogar = Button(self.frame)
		self.btnDeslogar["text"] = "Deslogar"
		self.btnDeslogar["width"] = 20
		self.btnDeslogar["bg"] = "#fff"
		self.btnDeslogar["fg"] = "#000"
		self.btnDeslogar["command"] = self.deslogar
		self.btnDeslogar.grid(row=4, column=0, pady=30)

		## Set button that erase account
		self.btnDeleteAccount = Button(self.frame)
		self.btnDeleteAccount["text"] = "Delete Account"
		self.btnDeleteAccount["width"] = 20
		self.btnDeleteAccount["bg"] = "#fff"
		self.btnDeleteAccount["fg"] = "#000"
		self.btnDeleteAccount["command"] = self.deleteAccount
		self.btnDeleteAccount.grid(row=4, column=1, pady=30)

	## VERIFY IF THE USER EXISTS IN DATABASE
	def verifyInformation(self):
		## Array to save informations about Name entry
		nm = []
		nm.append(self.txtName.get())
		nm.append(len(self.txtName.get()))

		## Variable to save the user Email
		em = self.txtEmail.get()

		## Variable to save procedure that verify if exists email
		query = "call p_SelectEmail('{}')".format(em)
		
		## Variable to save the user Sex
		sx = self.cmbSex.get()

		## Set the style of lblWarning message
		error = self.lblWarning["fg"] = self.title["fg"] = self.master.header["bg"] = self.lblInformation["fg"] = self.lblChangePassword["fg"] = "#f00"

		if nm[1] < 5:
			self.lblWarning["text"] = "Please type your full name"
			error
			
		elif em != self.email:
			if self.select(query):
				self.lblWarning["text"] = "This e-mail already exists, choose another"
				error
			
		elif '@' not in em or '.com' not in em:
			self.lblWarning["text"] = "E-mail invalid"
			error

		else:
			query = "p_UpdateUserInformations('{}', '{}', '{}')".format(nm[0], em, sx)
			if self.execute(query):
				self.setUserVariable(self.txtName.get(), self.txtEmail.get(), self.cmbSex.get())

	## VERIFY IF THE PASSWORD WAS FILLED CORRECTLY
	def verifyPassword(self):
		## Array to save informations about Password entry
		pw = []
		pw.append(len(self.txtNewPassword.get()))
		pw.append(self.txtNewPassword.get())
		pw.append(self.txtConfirmNewPassword.get())

		## Variable that save the procedure that verify password
		query = "p_SelectPassword('{}', '{}')".format(self.txtCurrentPassword.get(), self.id)

		## Set the style of warning message
		error = self.lblWarning["fg"] = self.title["fg"] = self.master.header["bg"] = self.lblInformation["fg"] = self.lblChangePassword["fg"] = "#f00"

		if pw[0] < 5:
			self.lblWarning["text"] = "The password must be at least 5 characters"
			error
			
		elif pw[1] != pw[2]:
			self.lblWarning["text"] = "The passwords need to be equals"
			error

		elif not self.select(query):
			self.lblWarning["text"] = "The current password is wrong"
			error

		else:
			query = "p_UpdateUserPassword('{}', '{}', '{}')".format(pw[1])
			if self.execute(query):
				self.setUserVariable(self.txtName.get(), self.txtEmail.get(), self.cmbSex.get())


	## LOGOUT
	def deslogar(self):
		from Class.Login import Login

		self.master.header["bg"] = "#ff0"
		login = Login(self.master)
		self.frame.destroy()

	## DELETE ACCOUNT IN DATABASE
	def deleteAccount(self):
		if messagebox.askyesno("WARNING", "Do You really want to delete your account ?"):
			query = "p_DeleteAccount('{}')".format(self.id)
			self.execute(query)
			self.deslogar()

	def setUserVariable(self, name, email, sex):
		self.name = name
		self.email = email
		self.sex = sex

	## EXECUTE COMMANDS IN DATABASE
	def execute(self, query):
		## Try to connect in database and execute the 'select'
		try:
			db = connect("127.0.0.1", "root", "", "python")

			cursor = db.cursor()
			cursor.execute(query)
			db.commit()
			db.close()
			
			return True

		except:
			self.lblWarning["text"] = "Error trying to connect to server"
			return False
		

	## VERIFY IF THE EMAIL ALREADY EXISTS IN DATABASE   
	def select(self, query):
		## Try to connect in database and execute the 'select'
		try:
			db = connect("127.0.0.1", "root", "", "python")

			cursor = db.cursor()
			cursor.execute(query)
			data = cursor.fetchone()
		
		except:
			self.lblWarning["text"] = "Error trying to connect to server"
		
		db.close()

		if data[0]:
			return True
		
		else:
			return False
