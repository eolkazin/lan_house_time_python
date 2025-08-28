import tkinter as tk
import os

### tempo em minutos ###
TEMPO_MINUTOS = 1   # exemplo: 1 minuto (troque para 60 p/ 1 hora)

class LanHouseTimer:
    def __init__(self, root, minutos):
        self.root = root
        self.segundos = minutos * 60

        self.root.title("LAN HOUSE - Cronômetro")
        self.root.geometry("400x200")
        self.root.configure(bg="black")

        # Sempre no topo
        self.root.attributes("-topmost", True)

        # Remove botão de fechar (X)
        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)

        # Texto do cronômetro
        self.label = tk.Label(
            root,
            text="",
            font=("Arial", 40, "bold"),
            fg="red",
            bg="black"
        )
        self.label.pack(expand=True)

        self.update_timer()

        # Bloqueia Alt+F4
        self.root.bind("<Alt-F4>", self.disable_event)

    def disable_event(self, *args, **kwargs):
        # Ignora tentativa de fechar
        return "break"

    def update_timer(self):
        if self.segundos > 0:
            m, s = divmod(self.segundos, 60)
            self.label.config(text=f"{m:02d}:{s:02d}")
            self.segundos -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.label.config(text="TEMPO ACABOU!")
            self.bloquear()

    def bloquear(self):
        os.system("rundll32.exe user32.dll,LockWorkStation")  # bloqueia a sessão

if __name__ == "__main__":
    root = tk.Tk()
    app = LanHouseTimer(root, TEMPO_MINUTOS)
    root.mainloop()