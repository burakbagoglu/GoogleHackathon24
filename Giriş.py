from customtkinter import *
from PIL import Image,ImageTk
app = CTk()


app.geometry("500x400")
set_appearance_mode("dark")
app.resizable(False,False)

giris_buton = CTkButton(master=app,text="Giriş",corner_radius=35,fg_color="#528b8b",hover_color="#4158D0",border_color="#FFCC70", border_width=2,)

giris_buton.place(relx=0.7, rely=0.5)

hesap_olustur_buton = CTkButton(master=app,text="Hesap Oluştur",corner_radius=35,fg_color="#528b8b",hover_color="#4158D0",border_color="#FFCC70", border_width=2,)

hesap_olustur_buton.place(relx=0.7, rely=0.6)

kullanıcı_adı= CTkLabel(master=app,text="Kullanıcı Adı:",font=("Arial",17 ))
kullanıcı_adı.place(relx=0.7,rely=0.07)

kullanıcı_adı_cevap= CTkEntry(master=app,fg_color=("#ffffff"))
kullanıcı_adı_cevap.place(relx=0.7,rely=0.15)

sifre= CTkLabel(master=app,text="Şifre:",font=("Arial",17 ))
sifre.place(relx=0.7,rely=0.23)


sifre_cevap= CTkEntry(master=app,fg_color=("#ffffff"))
sifre_cevap.place(relx=0.7,rely=0.31)


app.mainloop()



