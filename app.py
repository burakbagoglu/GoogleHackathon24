from customtkinter import *
import customtkinter as ctk
from tkinter import *
import tkinter as tk
import sqlite3 as sql
import hashlib
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

if __name__ == "__main__":
    app = App()
    app.mainloop()
