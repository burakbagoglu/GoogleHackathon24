
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.login_width = 400
        self.login_height = 300
        self.menu_width = 600
        self.menu_height = 400

        self.geometry(f"{self.login_width}x{self.login_height}")
        self.title("Giriş ve Ana Menü")

        # Giriş Sayfası
        self.login_frame = ctk.CTkFrame(self, width=self.login_width, height=self.login_height)
        self.login_frame.pack(fill="both", expand=True)

        self.username_label = ctk.CTkLabel(self.login_frame, text="Kullanıcı Adı:")
        self.username_label.pack(pady=10)
        self.username_entry = ctk.CTkEntry(self.login_frame)
        self.username_entry.pack(pady=10)

        self.password_label = ctk.CTkLabel(self.login_frame, text="Şifre:")
        self.password_label.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self.login_frame, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self.login_frame, text="Giriş Yap", command=self.login)
        self.login_button.pack(pady=20)

        # Ana Menü
        self.menu_frame = ctk.CTkFrame(self, width=self.menu_width, height=self.menu_height)

        self.menu_label = ctk.CTkLabel(self.menu_frame, text="Ana Menü")
        self.menu_label.pack(pady=20)

        self.logout_button = ctk.CTkButton(self.menu_frame, text="Çıkış Yap", command=self.logout)
        self.logout_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Basit bir kullanıcı adı ve şifre kontrolü
        if username == "admin" and password == "password":
            self.login_frame.pack_forget()
            self.geometry(f"{self.menu_width}x{self.menu_height}")
            self.menu_frame.pack(fill="both", expand=True)
        else:
            self.error_label = ctk.CTkLabel(self.login_frame, text="Geçersiz kullanıcı adı veya şifre", text_color="red")
            self.error_label.pack(pady=10)

    def logout(self):
        self.menu_frame.pack_forget()
        self.geometry(f"{self.login_width}x{self.login_height}")
        self.login_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
