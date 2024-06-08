import tkinter
import customtkinter as ctk


class Frame1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.frame_rot = ctk.CTkFrame(master, height = 100, width = 100, fg_color = 'red').grid(row = 0, column = 0)
        self.label = ctk.CTkLabel(self.frame_rot, text = 'hallo').place(relx = 0.5, rely = 0.5, anchor = 'center')
        
        
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry('500x500')
        self.title('TestApp')
        
        self.frame = Frame1(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()