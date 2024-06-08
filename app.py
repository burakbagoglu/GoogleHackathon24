from customtkinter import *
import customtkinter as ctk
from tkinter import *
import tkinter as tk
import sqlite3 as sql
import hashlib
from PIL import Image

##CREATE DATABASE AND TABLES
vt = sql.connect("database.db")
im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS users ('id','ad','soyad','durum','ulke','sehir','ilce','oncelik_puanı')")

app = CTk()

def Encrypte(sifre):
    sha256 = hashlib.sha256()
    sha256.update(sifre.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.login_page_width = 500
        self.login_page_height = 400
        self.register_page_width = 600
        self.register_page_height = 400
        self.main_page_width = 700
        self.main_page_height = 500

        self.resizable(False,False)

        self.geometry(f"{self.login_page_width}x{self.login_page_height}")
        self.title("Giriş Sayfası")

        self.login_frame = ctk.CTkFrame(self, width=self.login_page_width, height=self.login_page_height)
        self.login_frame.pack(fill="both", expand=True)

        self.login_text = ctk.CTkLabel(self.login_frame, text="Giriş Yap", font=('Bebas',24,"bold"),text_color="#D7BDE2")
        self.login_text.pack()

        self.login_email_label = ctk.CTkLabel(self.login_frame, text="E-posta: ")
        self.login_email_label.place(x=120,y=50)
        self.login_email_entry = ctk.CTkEntry(self.login_frame)
        self.login_email_entry.place(x=200,y=50)

        self.login_password_label = ctk.CTkLabel(self.login_frame, text="Şifre: ")
        self.login_password_label.place(x=120,y=90)
        self.login_password_entry = ctk.CTkEntry(self.login_frame, show="*")
        self.login_password_entry.place(x=200,y=90)

        self.login_button = ctk.CTkButton(self.login_frame,text="Giriş",corner_radius=35,fg_color="#528b8b",hover_color="#4158D0",border_color="#FFCC70", border_width=2,width=100,command=self.login)
        self.login_button.place(x=120,y=130)

        self.register_button = ctk.CTkButton(self.login_frame,text="Giriş",corner_radius=35,fg_color="#528b8b",hover_color="#4158D0",border_color="#FFCC70", border_width=2,width=100)
        self.register_button.place(x=240,y=130)

        ####################################################
        #Menü
        ####################################################
        self.main_manu_frame = ctk.CTkFrame(self,width=self.main_page_width,height=self.main_page_height)

        
    def login(self):
        email = self.login_email_entry.get()
        password = self.login_password_entry.get()

        giris = False
        im.execute("SELECT COUNT(*) FROM users")
        satirsayisi = im.fetchone()[0]
        im.execute("SELECT email FROM users")

        for i in range(satirsayisi):
            a = im.fetchone()[0]
            if a == email:
                giris = True
        if giris == True:
            im.execute("SELECT password FROM users WHERE email = ?",(email,))
            hashed_password = im.fetchone()[0]
            if hashed_password == Encrypte(password):
                self.login_frame.pack_forget()
                self.geometry(f"{self.main_page_width}x{self.main_page_height}")
                self.main_manu_frame.pack(fill="both", expand=True)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
