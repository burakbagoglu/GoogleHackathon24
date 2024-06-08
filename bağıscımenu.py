from customtkinter import*

app=CTk()
app.geometry("500x400")


yemek_ekle_buton=CTkButton(master=app,text="Yemek Ekle",command=ope)
yemek_ekle_buton.place(relx=0.02,rely=0.05)




app.mainloop()