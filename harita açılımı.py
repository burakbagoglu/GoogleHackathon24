from customtkinter import*
import webbrowser

app=CTk()
app.geometry("400x500")



def open_link():
    link = "https://www.google.com.tr/maps/@41.1026599,29.0273161,16.5z?hl=tr&entry=ttu"
    webbrowser.open_new_tab(link)








button =CTkButton(master=app, text="Linke Git", command=open_link)
button.pack()

app.mainloop()