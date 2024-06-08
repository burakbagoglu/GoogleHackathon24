from customtkinter import*
import sqlite3 
app=CTk()
app.geometry("500x400")
 
def open_new_window():
    new_window = CTkToplevel(app)
    new_window.title("Yeni Pencere")
    new_window.geometry("400x200")

    yemek_giren_entry = CTkEntry(new_window)
    yemek_giren_entry.pack()
    yemek_giren_entry.place( relx=0.5,rely=0.05)

    yemek_giriniz_label=CTkLabel(new_window,text="» Yemek Giriniz:",font=("Arial",16)) 
    yemek_giriniz_label.pack()   
    yemek_giriniz_label.place(relx=0.15,rely=0.05)


    kac_tabak_giren_entry = CTkEntry(new_window)
    kac_tabak_giren_entry.pack()
    kac_tabak_giren_entry.place( relx=0.5,rely=0.3)

    kac_tabak_label=CTkLabel(new_window,text="» Kaç Tabak Var Giriniz:",font=("Arial",16)) 
    kac_tabak_label.pack()   
    kac_tabak_label.place(relx=0.01,rely=0.3)


    
    def close_window():
        new_window.destroy()
    menuye_don_butonu=CTkButton(new_window,text="Menüye Dön",font=("Arial",16),command=close_window)
    menuye_don_butonu.pack()
    menuye_don_butonu.place(relx=0.5,rely=0.7,anchor="center")
    
        



yemek_ekle_buton=CTkButton(master=app,text="Yemek Ekle",command=open_new_window)
yemek_ekle_buton.pack()
yemek_ekle_buton.place(relx=0.02,rely=0.05)




app.mainloop()