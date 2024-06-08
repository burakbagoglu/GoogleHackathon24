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

def CreateID():
    im.execute(f"SELECT COUNT(*) FROM users")
    sutun = im.fetchone()[0]

    x = random.randint(11111111,99999999)
    im.execute(f"SELECT id FROM users")
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
            elif ihtiyacsahibi_veri == 1:
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

        kvkk_deger = ctk.IntVar()


        kvkk_check=CTkCheckBox(self.register_page_two_bagisci,
                               text="",
                               fg_color="#528b8b",
                               checkbox_height=18,
                               checkbox_width=18,
                               corner_radius=36,
                               variable=kvkk_deger)
        
        kvkk_check.place(relx=0.81,rely=0.72)

        canvas = ctk.CTkCanvas(self.register_page_two_bagisci,width=0.05,height=260)
        canvas.place(x=320,y=20)

        
        combobox_var = ctk.StringVar(value="Eskişehir")

        sehir = None
        ilce = None

        def sehircbox_callback(choice):
            global sehir
            sehir = str(choice).lower()
            def ilceler_cbox_callback(choice):
                global ilce
                ilce = str(choice).lower()

            ilceler_list = getIlceler(choice)
            ilceler_cbox = ctk.CTkComboBox(self.register_page_two_bagisci,
                                           values=ilceler_list,
                                           state="readonly",
                                           variable=ilceler_list[0],
                                           command=ilceler_cbox_callback)
            ilceler_cbox.place(x=340,y=50)
            



        sehirler_cbox = ctk.CTkComboBox(self.register_page_two_bagisci,
                                        values=getSehirler(),
                                        state="readonly",
                                        command=sehircbox_callback,
                                        variable=combobox_var)
        sehirler_cbox.place(x=340,y=10)

        def bagisci_register():
            global sehir,ilce
            isim = bagisci_entry.get()
            soyisim = bagisci_soyisim_entry.get()
            eposta = bagisci_eposta_entry.get()
            tc = bagisci_tc_entry.get()
            sifre = bagisci_sifre_entry.get()
            tekrar_sifre = bagisci_tekrar_sifre_entry.get()
            kvkk = kvkk_deger.get()
            
            if bool(isim) == True and bool(soyisim) == True and bool(eposta) == True and bool(tc) == True and sifre == tekrar_sifre:
                im.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?)",(CreateID(),isim,soyisim,eposta,Encrypte(sifre),tc,1,sehir,ilce,None,))
                vt.commit()
            

        register_button = ctk.CTkButton(self.register_page_two_bagisci,text="Kaydı Tamamla",command=bagisci_register)
        register_button.place(x=420,y=310)
        

        
        ###KAYIT 2. SAYFA İHTİYAÇ SAHİBİ
        self.register_page_two_ihtiyacsahibi = ctk.CTkFrame(self, width=self.register_page_width, height=self.register_page_height)

        #ihtiyacsahibi isim
        ihtiyacsahibi_isim= CTkLabel(self.register_page_two_ihtiyacsahibi,text="Ad: ",font=("Arial",13))
        ihtiyacsahibi_isim.place(x=10,y=10)

        ihtiyacsahibi_entry= CTkEntry(self.register_page_two_ihtiyacsahibi)
        ihtiyacsahibi_entry.place(x=90,y=10)


        #ihtiyacsahibi soyisim
        ihtiyacsahibi_soyisim= CTkLabel(self.register_page_two_ihtiyacsahibi,text="Soyisim:",font=("Arial",13))
        ihtiyacsahibi_soyisim.place(x=10,y=50)

        ihtiyacsahibi_soyisim_entry= CTkEntry(self.register_page_two_ihtiyacsahibi)
        ihtiyacsahibi_soyisim_entry.place(x=90,y=50)


        #ihtiyacsahibi eposta
        ihtiyacsahibi_eposta= CTkLabel(self.register_page_two_ihtiyacsahibi,text="E-posta",font=("Arial",13))
        ihtiyacsahibi_eposta.place(x=10,y=90)


        ihtiyacsahibi_eposta_entry= CTkEntry(self.register_page_two_ihtiyacsahibi)
        ihtiyacsahibi_eposta_entry.place(x=90,y=90)

        #bagışçı tc
        ihtiyacsahibi_tc= CTkLabel(self.register_page_two_ihtiyacsahibi,text="TC No.:",font=("Arial",13))
        ihtiyacsahibi_tc.place(x=10,y=130)


        ihtiyacsahibi_tc_entry= CTkEntry(self.register_page_two_ihtiyacsahibi)
        ihtiyacsahibi_tc_entry.place(x=90,y=130)


        #ihtiyacsahibi sifre
        ihtiyacsahibi_sifre= CTkLabel(self.register_page_two_ihtiyacsahibi,text="Şifre:",font=("Arial",13))
        ihtiyacsahibi_sifre.place(x=10,y=170)


        ihtiyacsahibi_sifre_entry= CTkEntry(self.register_page_two_ihtiyacsahibi, show="*")
        ihtiyacsahibi_sifre_entry.place(x=90,y=170)

        #ihtiyacsahibi tekrar sifre
        ihtiyacsahibi_tekrar_sifre= CTkLabel(self.register_page_two_ihtiyacsahibi,text="Tekrar Şifre:",font=("Arial",13))
        ihtiyacsahibi_tekrar_sifre.place(x=10,y=210)


        ihtiyacsahibi_tekrar_sifre_entry= CTkEntry(self.register_page_two_ihtiyacsahibi, show="*")
        ihtiyacsahibi_tekrar_sifre_entry.place(x=90,y=210)

        #kvkk onay
        kvkk= CTkLabel(self.register_page_two_ihtiyacsahibi,text="Kullanım şartlarını ve KVKK metnini okuduğumu onaylıyorum",font=("Arial",15 ))
        kvkk.place(relx=0.02,rely=0.71)

        kvkkkk = ctk.IntVar()


        kvkk_checkk=CTkCheckBox(self.register_page_two_ihtiyacsahibi,
                               text="",
                               fg_color="#528b8b",
                               checkbox_height=18,
                               checkbox_width=18,
                               corner_radius=36,
                               variable=kvkkkk)
        
        kvkk_checkk.place(relx=0.81,rely=0.72)

        canvas = ctk.CTkCanvas(self.register_page_two_ihtiyacsahibi,width=0.05,height=260)
        canvas.place(x=320,y=20)

        
        combobox_var = ctk.StringVar(value="Eskişehir")

        sehir = None
        ilce = None

        def sehircbox_callback(choice):
            global sehir
            sehir = str(choice).lower()
            def ilceler_cbox_callback(choice):
                global ilce
                ilce = str(choice).lower()

            ilceler_list = getIlceler(choice)
            ilceler_cbox = ctk.CTkComboBox(self.register_page_two_ihtiyacsahibi,
                                           values=ilceler_list,
                                           state="readonly",
                                           variable=ilceler_list[0],
                                           command=ilceler_cbox_callback)
            ilceler_cbox.place(x=340,y=50)
            



        sehirler_cbox = ctk.CTkComboBox(self.register_page_two_ihtiyacsahibi,
                                        values=getSehirler(),
                                        state="readonly",
                                        command=sehircbox_callback,
                                        variable=combobox_var)
        sehirler_cbox.place(x=340,y=10)

        id = CreateID()
        def ihtiyacsahibi_register():
            global sehir,ilce
            isim = ihtiyacsahibi_entry.get()
            soyisim = ihtiyacsahibi_soyisim_entry.get()
            eposta = ihtiyacsahibi_eposta_entry.get()
            tc = ihtiyacsahibi_tc_entry.get()
            sifre = ihtiyacsahibi_sifre_entry.get()
            tekrar_sifre = ihtiyacsahibi_tekrar_sifre_entry.get()
            kvkk = kvkkkk.get()
            if bool(isim) == True and bool(soyisim) == True and bool(eposta) == True and bool(tc) == True and sifre == tekrar_sifre:
                im.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?)",(id,isim,soyisim,eposta,Encrypte(sifre),tc,0,sehir,ilce,None,))
                vt.commit()
                
                self.ihtiyacsahibi_page1_to_page2()


        register_button = ctk.CTkButton(self.register_page_two_ihtiyacsahibi,text="İleri",command=ihtiyacsahibi_register)
        register_button.place(x=420,y=310)
        
        
        #######İHTİYAÇ SAHİBİ KAYIT SAYFA 2########
        self.register_page_three_ihtiyacsahibi = ctk.CTkFrame(self, width=self.register_page_width, height=self.register_page_height)
        print(id)
        aylık_gelir_soru= CTkLabel(self.register_page_three_ihtiyacsahibi,text="⁕ Aylık gelirinizi çizelgede işaretleyiniz.",font=("Arial",17 ))
        aylık_gelir_soru.place(relx=0.03,rely=0.07)
        aylik_gelir_veri = ctk.IntVar()
        aylık_gelir_soru_slider=CTkSlider(self.register_page_three_ihtiyacsahibi,
                                          from_=0,
                                          to= 50000,
                                          width=240,
                                          number_of_steps=5,
                                          button_color="#528b8b",
                                          progress_color="#ffffff",
                                          variable=aylik_gelir_veri)
        
        aylık_gelir_soru_slider.place(relx=0.6 ,rely=0.08)

        kac_kisi_yasıyor_soru= CTkLabel(self.register_page_three_ihtiyacsahibi,text="⁕ Hanenizde kaç kişi yaşıyor?",font=("Arial",17 ))
        kac_kisi_yasıyor_soru.place(relx=0.03,rely=0.16)

        kac_kisi_yasıyor_cevap=CTkEntry(self.register_page_three_ihtiyacsahibi)
        kac_kisi_yasıyor_cevap.place(relx=0.67,rely=0.15)

        sıfır_label=CTkLabel(self.register_page_three_ihtiyacsahibi,text="0",font= ("Arial",16))
        sıfır_label.place(relx=0.61 ,rely=0.01 )

        onbin_label=CTkLabel(self.register_page_three_ihtiyacsahibi,text="10k",font= ("Arial",13))
        onbin_label.place(relx=0.67 ,rely=0.01 )

        yirmibin_label=CTkLabel(self.register_page_three_ihtiyacsahibi,text="20k",font= ("Arial",13))
        yirmibin_label.place(relx=0.75 ,rely=0.01 )

        otuzbin_label=CTkLabel(self.register_page_three_ihtiyacsahibi,text="30k",font= ("Arial",13))
        otuzbin_label.place(relx=0.82 ,rely=0.01 )

        kırkbin_label=CTkLabel(self.register_page_three_ihtiyacsahibi,text="40k",font= ("Arial",13))
        kırkbin_label.place(relx=0.89 ,rely=0.01 )

        ellibin_label=CTkLabel(self.register_page_three_ihtiyacsahibi,text="50k",font= ("Arial",13))
        ellibin_label.place(relx=0.95 ,rely=0.01 )

        ev_soru=CTkLabel(self.register_page_three_ihtiyacsahibi,text="⁕ Oturduğunuz evin durumu nedir?",font=("Arial",17))
        ev_soru.place(relx=0.03,rely=0.26)

        evtipi = ctk.StringVar()

        ev_soru_cevap=CTkComboBox(self.register_page_three_ihtiyacsahibi,
                                  values=["Kendi Evim","Miras","Kira","Hibe",],
                                  state="readonly",
                                  variable=evtipi)
        
        ev_soru_cevap.place(relx=0.67,rely=0.26)

        engel_hastalık_soru=CTkLabel(self.register_page_three_ihtiyacsahibi,text="⁕ Engeliniz veya hastalığınız var mı?",font=("Arial",17))
        engel_hastalık_soru.place(relx=0.03,rely=0.35)

        hastalik_var = ctk.IntVar()


        hastalık_checkbox=CTkCheckBox(self.register_page_three_ihtiyacsahibi,text="",
                                      fg_color="#528b8b",
                                      checkbox_height=25,
                                      checkbox_width=25,
                                      corner_radius=36,
                                      variable=hastalik_var)
        hastalık_checkbox.place(relx=0.78 ,rely=0.36)

        def complete_register():
            aylik_gelir = aylik_gelir_veri.get()
            hanede_yasayan_kisi_sayisi = kac_kisi_yasıyor_cevap.get()
            hastalik = hastalik_var.get()
            ev_tipi = evtipi.get()

            
            
        register_button2 = ctk.CTkButton(self.register_page_three_ihtiyacsahibi,text="Kaydı Tamamla",command=complete_register)
        register_button2.place(x=420,y=310)
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
        elif page == 0:
            self.title("Kayıt Sayfası | İhtiyaç Sahibi")
            self.register_page_two_ihtiyacsahibi.pack(fill="both", expand=True)

    #KAYITTAN LOGİN SAYFASI GEÇİŞ
    def login_page_after_registered(self):
        self.register_page_two_bagisci.pack_forget()
        self.geometry(f"{self.login_page_width}x{self.login_page_height}")
        self.login_frame.pack(fill="both", expand=True)

    #İHTİYAÇ SAHİBİ SAYFA 1 -> SAYFA
    def ihtiyacsahibi_page1_to_page2(self):
        self.register_page_two_ihtiyacsahibi.pack_forget()
        self.geometry(f"{self.register_page_width}x{self.register_page_height}")
        self.register_page_three_ihtiyacsahibi.pack(fill="both", expand=True)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
