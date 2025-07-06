
import importlib.util, subprocess, sys, secrets, tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

def ensure_module(mod, pip_name=None):
    if importlib.util.find_spec(mod.split('.')[0]) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name or mod.split('.')[0]])

ensure_module("tkinter", "tk")

ASCII_ART = (
    "█████╗ ███████╗███████╗       ██████╗ ███████╗███╗   ██╗\n"
    "██╔══██╗██╔════╝██╔════╝      ██╔════╝ ██╔════╝████╗  ██║\n"
    "███████║█████╗  ███████╗█████╗██║  ███╗█████╗  ██╔██╗ ██║\n"
    "██╔══██║██╔══╝  ╚════██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║\n"
    "██║  ██║███████╗███████║      ╚██████╔╝███████╗██║ ╚████║\n"
    "╚═╝  ╚═╝╚══════╝╚══════╝       ╚═════╝ ╚══════╝╚═╝  ╚═══╝"
)

ROUNDS_MAP = {128: 10, 192: 12, 256: 14}

def generate_hex_keys(count, bits):
    return [secrets.token_hex(bits // 8).upper() for _ in range(count)]

class AESKeyGUI:
    def __init__(self, root):
        self.root = root
        root.title("AES Key Generator")
        root.configure(background="white")
        for col in range(4):
            root.grid_columnconfigure(col, weight=1)
        self._init_styles()
        self._build_ui()

    def _init_styles(self):
        style = ttk.Style()
        style.configure("Red.TLabel", background="white", foreground="red", font=("Courier", 9))
        style.configure("Blue.TLabel", background="white", foreground="blue", font=("Courier", 12, "bold"))
        style.configure("Black.TLabel", background="white", foreground="black", font=("Courier", 9))
        style.configure("Field.TLabel", background="white", foreground="black", font=("Courier", 10))
        style.configure("TButton", font=("Courier", 10))

    def _build_ui(self):
        ttk.Label(self.root, text=ASCII_ART, style="Red.TLabel",
                  justify="center", anchor="center").grid(row=0, column=0, columnspan=4, sticky="ew")
        ttk.Label(self.root, text="A E S   K E Y   G E N E R A T O R",
                  style="Blue.TLabel", justify="center", anchor="center").grid(row=1, column=0, columnspan=4, sticky="ew")
        ttk.Label(self.root, text="Version 1.00", style="Red.TLabel",
                  justify="center", anchor="center").grid(row=2, column=0, columnspan=4, sticky="ew")
        ttk.Label(self.root, text="By Joshua M Clatney – Ethical Pentesting Enthusiast",
                  style="Black.TLabel", justify="center", anchor="center").grid(row=3, column=0, columnspan=4, sticky="ew", pady=(0, 10))

        key_frame = ttk.Frame(self.root)
        key_frame.grid(row=4, column=0, columnspan=4, sticky="ew", pady=5)
        key_frame.grid_columnconfigure(0, weight=1)

        ttk.Label(key_frame, text="Key size:", style="Field.TLabel").grid(row=0, column=0, sticky="w")
        self.key_size_var = tk.IntVar(value=128)
        for idx, size in enumerate([128, 192, 256], start=1):
            ttk.Radiobutton(key_frame, text=f"{size}-bit",
                            variable=self.key_size_var, value=size).grid(row=0, column=idx, sticky="w", padx=5)

        ttk.Label(key_frame, text="Number of keys (1-1000):",
                  style="Field.TLabel").grid(row=1, column=0, sticky="w", pady=5)
        self.num_var = tk.StringVar(value="1")
        ttk.Spinbox(key_frame, from_=1, to=1000,
                    textvariable=self.num_var, width=10).grid(row=1, column=1, sticky="w")

        ttk.Button(self.root, text="Generate Keys",
                   command=self.generate).grid(row=5, column=0, sticky="w", pady=10, padx=2)
        ttk.Button(self.root, text="Quit",
                   command=self.root.destroy).grid(row=5, column=1, sticky="w", pady=10)

        self.output = scrolledtext.ScrolledText(self.root, width=80, height=20,
                                                font=("Courier", 10), background="white",
                                                foreground="black")
        self.output.grid(row=6, column=0, columnspan=4, pady=5, padx=2, sticky="nsew")
        self.root.grid_rowconfigure(6, weight=1)

    def generate(self):
        try:
            count = int(self.num_var.get())
            if count < 1 or count > 1000:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid number", "Enter a value between 1 and 1000.")
            return
        bits = self.key_size_var.get()
        rounds = ROUNDS_MAP[bits]
        keys = generate_hex_keys(count, bits)
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, f"AES-{bits} uses {rounds} rounds.\n\n")
        for idx, key in enumerate(keys, 1):
            self.output.insert(tk.END, f"{idx}: {key}\n")
        self.output.insert(tk.END, "\nGeneration complete.\n")

if __name__ == "__main__":
    root = tk.Tk()
    AESKeyGUI(root)
    root.mainloop()