from customtkinter import *
import customtkinter as ctk
from tkinter import *
import tkinter as tk
import sqlite3 as sql

##CREATE DATABASE AND TABLES
vt = sql.connect("database.db")
im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS users ('id','ad','soyad','durum','ulke','sehir','ilce','oncelik_puanı')")

app = CTk()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        