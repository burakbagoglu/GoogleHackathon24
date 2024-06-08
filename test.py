from customtkinter import *

app = CTk()


app.geometry("500x400")

button = CTkButton(master=app,text="enter",corner_radius=35,fg_color="#528b8b",hover_color="4158D0",border_color="FFCC70")

button.place(relx=0.5, rely=0.5, anchor="center")


app.mainloop()
