from customtkinter import *
import customtkinter as ctk
from tkinter import *
import tkinter as tk
import sqlite3 as sql
import hashlib
from PIL import Image
import random

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

def CreateID(table):
    im.execute(f"SELECT COUNT(*) FROM users")
    sutun = im.fetchone()[0]

    x = random.randint(11111111,99999999)
    im.execute(f"SELECT id FROM {table}")
    for i in range(sutun):
        veri = im.fetchone()
        if veri == x:
            x += 1
    return x

def getSehirler():
    sehirler = []
    im.execute("SELECT name FROM sehirler")
    for i in range(81):
        a = str(im.fetchone()[0])
        sehirler.append(a.capitalize())
    return sehirler

def getIlceler(sehir):
    ilceler = []
    im.execute("SELECT counties FROM sehirler WHERE name = ?",(str(sehir).lower(),))
    ilce = str(im.fetchone()[0]).split(",")    
    for i in ilce:
        ilceler.append(i.capitalize())
    return ilceler
getIlceler("Manisa")
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ########LOGIN PAGE#############
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
        self.login_password_label.place(x=136,y=90)
        self.login_password_entry = ctk.CTkEntry(self.login_frame, show="*")
        self.login_password_entry.place(x=200,y=90)

        self.login_button = ctk.CTkButton(self.login_frame,
                                          text="Giriş",
                                          corner_radius=35,
                                          fg_color="#528b8b",
                                          hover_color="#4158D0",
                                          border_color="#FFCC70",
                                          border_width=2,width=100,
                                          command=self.login)
        self.login_button.place(x=120,y=130)

        self.register_button = ctk.CTkButton(self.login_frame,
                                             text="Kayıt Ol",
                                             corner_radius=35,
                                             fg_color="#528b8b",
                                             hover_color="#4158D0",
                                             border_color="#FFCC70",
                                             border_width=2,width=100,
                                             command=self.show_register_page)
        self.register_button.place(x=240,y=130)

        #############REGISTER PAGE ONE ############
        def checkbox_callback(bagisci, ihtiyacsahibi, id):
            if id == 1:
                ihtiyacsahibi.set(0)
            else:
                bagisci.set(0)

        bagisci = ctk.IntVar()
        ihtiyacsahibi = ctk.IntVar()

        self.register_page_one = ctk.CTkFrame(self, width=self.register_page_width, height=self.register_page_height)
        
        self.bagisci_tik = ctk.CTkCheckBox(self.register_page_one,
                                           text="Bağışçıyım",
                                           variable=bagisci,
                                           font=("Arial",20),
                                           fg_color="#528b8b",
                                           checkbox_height=80,
                                           checkbox_width=80,
                                           corner_radius=36,
                                           command=lambda: checkbox_callback(bagisci,ihtiyacsahibi, 1))
        self.bagisci_tik.place(x=100,y=100)
    
        self.ihtiyacsahibi_tik = ctk.CTkCheckBox(self.register_page_one,
                                                 variable=ihtiyacsahibi,
                                                 text="İhtiyaç Sahibiyim",
                                                 font=("Arial",20),
                                                 fg_color="#528b8b",
                                                 checkbox_height=80,
                                                 checkbox_width=80,
                                                 corner_radius=36,
                                                 command=lambda: checkbox_callback(bagisci,ihtiyacsahibi, 2))
        self.ihtiyacsahibi_tik.place(x=100,y=200)

        #checkbox veri alma 2. sayfaya geçiş
        def get_checkbox_data():
            bagisci_veri = int(bagisci.get())
            ihtiyacsahibi_veri = int(ihtiyacsahibi.get())
            if bagisci_veri == 1:
                self.next_page_to_two(1)
            elif ihtiyacsahibi == 1:
                self.next_page_to_two(0)

        self.next_page_to_two_button = ctk.CTkButton(self.register_page_one,
                                             text="İleri",
                                             corner_radius=35,
                                             fg_color="#528b8b",
                                             hover_color="#4158D0",
                                             border_color="#FFCC70",
                                             border_width=2,
                                             width=100,
                                             command=get_checkbox_data)
        self.next_page_to_two_button.place(x=400,y=350)

        ##############################################KAYIT 2. SAYFA BAĞIŞÇI################################################
        
        self.register_page_two_bagisci = ctk.CTkFrame(self, width=self.register_page_width, height=self.register_page_height)
        
        #bağışçı isim
        bagisci_isim= CTkLabel(self.register_page_two_bagisci,text="Ad: ",font=("Arial",13))
        bagisci_isim.place(x=10,y=10)

        bagisci_entry= CTkEntry(self.register_page_two_bagisci)
        bagisci_entry.place(x=90,y=10)


        #bağışçı soyisim
        bagisci_soyisim= CTkLabel(self.register_page_two_bagisci,text="Soyisim:",font=("Arial",13))
        bagisci_soyisim.place(x=10,y=50)

        bagisci_soyisim_entry= CTkEntry(self.register_page_two_bagisci)
        bagisci_soyisim_entry.place(x=90,y=50)


        #bağışçı eposta
        bagisci_eposta= CTkLabel(self.register_page_two_bagisci,text="E-posta",font=("Arial",13))
        bagisci_eposta.place(x=10,y=90)


        bagisci_eposta_entry= CTkEntry(self.register_page_two_bagisci)
        bagisci_eposta_entry.place(x=90,y=90)

        #bagışçı tc
        bagisci_tc= CTkLabel(self.register_page_two_bagisci,text="TC No.:",font=("Arial",13))
        bagisci_tc.place(x=10,y=130)


        bagisci_tc_entry= CTkEntry(self.register_page_two_bagisci)
        bagisci_tc_entry.place(x=90,y=130)


        #bagisci sifre
        bagisci_sifre= CTkLabel(self.register_page_two_bagisci,text="Şifre:",font=("Arial",13))
        bagisci_sifre.place(x=10,y=170)


        bagisci_sifre_entry= CTkEntry(self.register_page_two_bagisci, show="*")
        bagisci_sifre_entry.place(x=90,y=170)

        #bagisci tekrar sifre
        bagisci_tekrar_sifre= CTkLabel(self.register_page_two_bagisci,text="Tekrar Şifre:",font=("Arial",13))
        bagisci_tekrar_sifre.place(x=10,y=210)


        bagisci_tekrar_sifre_entry= CTkEntry(self.register_page_two_bagisci, show="*")
        bagisci_tekrar_sifre_entry.place(x=90,y=210)

        #kvkk onay
        kvkk= CTkLabel(self.register_page_two_bagisci,text="Kullanım şartlarını ve KVKK metnini okuduğumu onaylıyorum",font=("Arial",15 ))
        kvkk.place(relx=0.02,rely=0.71)

        kvkk_check=CTkCheckBox(self.register_page_two_bagisci,text="",fg_color="#528b8b",checkbox_height=18,checkbox_width=18,corner_radius=36,)
        kvkk_check.place(relx=0.81,rely=0.72)

        canvas = ctk.CTkCanvas(self.register_page_two_bagisci,width=0.05,height=260)
        canvas.place(x=320,y=20)

        
        combobox_var = ctk.StringVar(value="Eskişehir")

        def combobox_callback(choice):
            ilceler_list = getIlceler(choice)
            ilceler_cbox = ctk.CTkComboBox(self.register_page_two_bagisci,
                                           values=ilceler_list,
                                           state="readonly",
                                           variable=ilceler_list[0]
                                           )
            ilceler_cbox.place(x=340,y=50)

        sehirler_cbox = ctk.CTkComboBox(self.register_page_two_bagisci,
                                        values=getSehirler(),
                                        state="readonly",
                                        command=combobox_callback,
                                        variable=combobox_var)
        sehirler_cbox.place(x=340,y=10)
        
        register_button = 
        
        
        ###KAYIT 2. SAYFA İHTİYAÇ SAHİBİ
        self.register_page_two_ihtiyacsahibi = ctk.CTkFrame(self, width=self.register_page_width, height=self.register_page_height)


        #############MAIN MENU PAGE###########
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

    ##KAYIT SAYFASINA GECİŞ
    def show_register_page(self):
        self.login_frame.pack_forget()
        self.geometry(f"{self.register_page_width}x{self.register_page_height}")
        self.title("Kayıt Sayfası")
        self.register_page_one.pack(fill="both", expand=True)

    #2. KAYIT SAYFASINA GEÇİŞ
    def next_page_to_two(self,page):
        self.register_page_one.pack_forget()
        self.geometry(f"{self.register_page_width}x{self.register_page_height}")
        if page == 1:
            self.register_page_two_bagisci.pack(fill="both", expand=True)
            self.title("Kayıt Sayfası | Bağışçı")
        if page == 0:
            self.title("Kayıt Sayfası | İhtiyaç Sahibi")
            self.register_page_two_ihtiyacsahibi.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
