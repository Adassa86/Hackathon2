 
#on va ramener le  module tkinter
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pygame
import numpy
import subprocess

class Login:
     def __init__(self,root):
          self.root=root
          self.root.title("login System")
          self.root.geometry("1199x600+100+50")
          #supprimer la possibilite de reduir la fenetre
          self.root.resizable(False, False)
          self.bg=ImageTk.PhotoImage(file="image.jpg")
          self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1) 

          Frame_login = Frame(self.root, bg="lightgrey")
          Frame_login.place(x=370 , y=180, width = 450, height= 200)

#les titres et sous titre
          title = Label(Frame_login, text="Login Here", font= ("Goudy old style", 20 , "bold"), fg="grey" , bg="lightgrey").place(x=165,y=25)
          subtitle = Label(Frame_login, text="Members Login Area", font= ("Goudy old style", 15 , "bold"), fg="black" , bg="lightgrey").place(x=147,y=65)
#usurname
          lbl_user = Label(Frame_login, text="Username", font= ("Goudy old style", 10 , "bold"), fg="grey" , bg="lightgrey").place(x=110,y=85)
          self.username = Entry(Frame_login, font= ("Goudy old style", 10), bg = "grey")
          self.username.place(x=110, y=105, width=250, height=20)


# password
          lbl_user = Label(Frame_login, text="Password", font= ("Goudy old style", 10 , "bold"), fg="grey" , bg="lightgrey").place(x=110,y=125)
          self.password = Entry(Frame_login, font= ("Goudy old style", 10), bg = "grey")
          self.password.place(x=110, y=145, width=250, height=20)

          forget = Button(Frame_login, text="Forget password?", cursor="hand2", border=0, font= ("Goudy old style", 8 ), fg="grey" , bg="lightgrey").place(x=110,y=165)
          submit = Button(Frame_login,command=self.check_function, cursor="hand2", text="Login?",font= ("Goudy old style", 8 ), fg="grey" , bg="lightgrey").place(x=205,y=165)

     def check_function(self):
          if self.username.get()=="" or self.password.get()=="":
                     messagebox.showerror("Error", "All fields are required", parent=self.root)
          elif self.username.get()!= "Developers" or self.password.get()!="Institut":
                    messagebox.showerror("Error", "Invalide Usurname or Password")
                    subprocess.call(['python', 'jeu.py'])
          else:
                    subprocess.call(['python', 'casinograph.py'])

root = Tk()
obj = Login(root)
root.mainloop()

