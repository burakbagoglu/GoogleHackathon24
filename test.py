from customtkinter import *

app = CTk()


app.geometry("500x400")
set_appearance_mode("dark")


button = CTkButton(master=app,text="Giriş",corner_radius=35,fg_color="#528b8b",hover_color="#4158D0",border_color="#FFCC70", border_width=2,)

button.place(relx=0.03, rely=0.7 )

button1 = CTkButton(master=app,text="Hesap Oluştur",corner_radius=35,fg_color="#528b8b",hover_color="#4158D0",border_color="#FFCC70", border_width=2,)

button1.place(relx=0.7, rely=0.7)

label1= CTkLabel(master=app,text="Kullanıcı Adı:",font=("Arial",17 ))
label1.place(relx=0.03,rely=0.07)

entry1= CTkEntry(master=app,fg_color=("#ffffff"))
entry1.place(relx=0.03,rely=0.15)

label2= CTkLabel(master=app,text="Şifre:",font=("Arial",17 ))
label2.place(relx=0.03,rely=0.23)


entry2= CTkEntry(master=app,fg_color=("#ffffff"))
entry2.place(relx=0.03,rely=0.31)


app.mainloop()
