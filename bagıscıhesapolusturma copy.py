from customtkinter import *

app = CTk()


app.geometry("500x400")
set_appearance_mode("dark")
app.resizable(False,False)

button = CTkButton(master=app,text="Kaydol",corner_radius=35,fg_color="#528b8b",hover_color="#4158D0",border_color="#FFCC70", border_width=2,)

button.place(relx=0.5, rely=0.9,anchor="center")

label1= CTkLabel(master=app,text="İsim:",font=("Arial",17 ))
label1.place(relx=0.03,rely=0.07)

entry1= CTkEntry(master=app,fg_color=("#ffffff"))
entry1.place(relx=0.03,rely=0.15)

label2= CTkLabel(master=app,text="Soyisim:",font=("Arial",17 ))
label2.place(relx=0.03,rely=0.23)


entry2= CTkEntry(master=app,fg_color=("#ffffff"))
entry2.place(relx=0.03,rely=0.31)


label3= CTkLabel(master=app,text="Şehir:",font=("Arial",17 ))
label3.place(relx=0.5,rely=0.07)

entry3= CTkEntry(master=app,fg_color=("#ffffff"))
entry3.place(relx=0.5,rely=0.15)


label4= CTkLabel(master=app,text="İlçe:",font=("Arial",17 ))
label4.place(relx=0.5,rely=0.23)


entry4= CTkEntry(master=app,fg_color=("#ffffff"))
entry4.place(relx=0.5,rely=0.31)


label5= CTkLabel(master=app,text="TC Kimlik No:",font=("Arial",17 ))
label5.place(relx=0.03,rely=0.39)


entry5= CTkEntry(master=app,fg_color=("#ffffff"))
entry5.place(relx=0.5,rely=0.39)


label6= CTkLabel(master=app,text="Kullanıcı Adı:",font=("Arial",17 ))
label6.place(relx=0.03,rely=0.47)


entry6= CTkEntry(master=app,fg_color=("#ffffff"))
entry6.place(relx=0.5,rely=0.47)



label7= CTkLabel(master=app,text="Şifre:",font=("Arial",17 ))
label7.place(relx=0.03,rely=0.55)


entry7= CTkEntry(master=app,fg_color=("#ffffff"))
entry7.place(relx=0.5,rely=0.55)



label8= CTkLabel(master=app,text="Mail veya Tel No:",font=("Arial",17 ))
label8.place(relx=0.03,rely=0.63)


entry8= CTkEntry(master=app,fg_color=("#ffffff"))
entry8.place(relx=0.5,rely=0.63)





label9= CTkLabel(master=app,text="Kullanım şartlarını ve KVKK metnini okuduğumu onaylıyorum",font=("Arial",15 ))
label9.place(relx=0.02,rely=0.71)

checkbox=CTkCheckBox(master=app,text="",fg_color="#528b8b",checkbox_height=18,checkbox_width=18,corner_radius=36,)
checkbox.place(relx=0.81,rely=0.72)





app.mainloop()

