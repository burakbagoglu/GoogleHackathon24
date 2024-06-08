import tkinter as tk
import customtkinter as ctk
import sqlite3
def on_select(event):
    
    selected_item = listbox.get(listbox.curselection())
    selected_label.config(text=f"Seçilen Öğe: {selected_item}")


app = ctk.CTk()
app.title("CustomTkinter Liste Arayüzü")
app.geometry("400x400")
app.resizable(False,False)


ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)


scrollbar = ctk.CTkScrollbar(frame, orientation=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE, bg="#2A2D2E", fg="white", highlightcolor="#3D3D3D", selectbackground="#565B5E", relief=tk.FLAT, borderwidth=0)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


scrollbar.configure(command=listbox.yview)


items = ["Öğe 1", "Öğe 2", "Öğe 3", "Öğe 4", "Öğe 5"]
for item in items:
    listbox.insert(tk.END, item)


listbox.bind("<<ListboxSelect>>", on_select)


selected_label = ctk.CTkLabel(app, text="Seçilen Öğe: ")
selected_label.pack(pady=20)


app.mainloop()
