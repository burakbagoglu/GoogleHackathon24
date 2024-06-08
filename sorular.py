from customtkinter import*


app = CTk()


app.geometry("500x400")
set_appearance_mode("dark")
app.resizable(False,False)

button = CTkButton(master=app,text="Kayıt Ol",corner_radius=35,fg_color="#528b8b",hover_color="#4158D0",border_color="#FFCC70", border_width=2,)      
button.place(relx=0.5, rely=0.9,anchor="center")

aylık_gelir_soru= CTkLabel(master=app,text="⁕ Aylık gelirinizi çizelgede işaretleyiniz.",font=("Arial",17 ))
aylık_gelir_soru.place(relx=0.03,rely=0.07)


aylık_gelir_soru_slider=CTkSlider(master=app,from_=0, to= 50000,number_of_steps=5, button_color="#528b8b",progress_color="#ffffff")
aylık_gelir_soru_slider.place(relx=0.6 ,rely=0.08)


kac_kisi_yasıyor_soru= CTkLabel(master=app,text="⁕ Hanenizde kaç kişi yaşıyor?",font=("Arial",17 ))
kac_kisi_yasıyor_soru.place(relx=0.03,rely=0.16)


kac_kisi_yasıyor_cevap=CTkEntry(master=app)
kac_kisi_yasıyor_cevap.place(relx=0.67,rely=0.15)


sıfır_label=CTkLabel(master=app,text="0",font= ("Arial",16))
sıfır_label.place(relx=0.61 ,rely=0.01 )





onbin_label=CTkLabel(master=app,text="10k",font= ("Arial",13))
onbin_label.place(relx=0.67 ,rely=0.01 )




yirmibin_label=CTkLabel(master=app,text="20k",font= ("Arial",13))
yirmibin_label.place(relx=0.75 ,rely=0.01 )




otuzbin_label=CTkLabel(master=app,text="30k",font= ("Arial",13))
otuzbin_label.place(relx=0.82 ,rely=0.01 )



kırkbin_label=CTkLabel(master=app,text="40k",font= ("Arial",13))
kırkbin_label.place(relx=0.89 ,rely=0.01 )



ellibin_label=CTkLabel(master=app,text="50k",font= ("Arial",13))
ellibin_label.place(relx=0.96 ,rely=0.01 )




ev_soru=CTkLabel(master=app,text="⁕ Oturduğunuz evin durumu nedir?",font=("Arial",17))
ev_soru.place(relx=0.03,rely=0.26)



ev_soru_cevap=CTkComboBox(master=app,values=["Kendi Evim","Miras","Kira","Hibe",])
ev_soru_cevap.place(relx=0.67,rely=0.26)


engel_hastalık_soru=CTkLabel(master=app,text="⁕ Engeliniz veya hastalığınız var mı?",font=("Arial",17))
engel_hastalık_soru.place(relx=0.03,rely=0.35)


hastalık_checkbox=CTkCheckBox(master=app,text="",fg_color="#528b8b",checkbox_height=25,checkbox_width=25,corner_radius=36)
hastalık_checkbox.place(relx=0.78 ,rely=0.36)




app.mainloop()