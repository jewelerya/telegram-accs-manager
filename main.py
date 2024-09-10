import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
from ttkthemes import ThemedTk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ферма тг")
        self.root.geometry("450x400")
        
        self.processes = {}
        
        style = ttk.Style(root)
        style.theme_use("black")
        
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill='both', expand=True)
        
        title_label = ttk.Label(main_frame, text="Тг ферма", font=("Helvetica", 18, "bold"))
        title_label.pack(pady=10)
        
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=False)
        scrollbar.pack(side="right", fill="both")

        self.button_frame = ttk.Frame(scrollable_frame)
        self.button_frame.pack(fill='both', expand=True, pady=20)
        
        # Список exe-файлов и их путей
        self.exe_files = [
            {"name": "1-2 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "3-4 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "5-6 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "7-8 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "9-10 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "11-12 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "13-14 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "15-16 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "17-18 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "19-20 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "21-22 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "23-24 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "25-26 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "27-28 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "29-30 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "31-32 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "33-34 акк", "path": "F:/path/to/telegram.exe"},
            {"name": "35-36 акк", "path": "F:/path/to/telegram.exe"},
        ]
        
        for exe in self.exe_files:
            self.create_button(exe["name"], exe["path"])
    
    def create_button(self, name, path):
        button_frame = ttk.Frame(self.button_frame)
        button_frame.pack(fill='x', pady=5)
        
        label = ttk.Label(button_frame, text=name, width=30)
        label.pack(side='left', padx=10)
        
        start_button = ttk.Button(button_frame, text="Start")
        start_button.pack(side='left', padx=5)
        start_button.config(command=lambda path=path, button=start_button: self.start_process(path, button))
        
        stop_button = ttk.Button(button_frame, text="Stop", command=lambda path=path, button=start_button: self.stop_process(path, button))
        stop_button.pack(side='left', padx=5)
        
        # Добавление чекбокса
        checkbox = ttk.Checkbutton(button_frame, text="")
        checkbox.pack(side='left', padx=5)
    
    def start_process(self, path, button):
        if path in self.processes:
            messagebox.showinfo("Info", f"{path} is already running.")
            return
        
        process = subprocess.Popen(path)
        self.processes[path] = process
        button.config(style="StartButton.TButton")
    
    def stop_process(self, path, button):
        process = self.processes.get(path)
        if process:
            process.terminate()
            process.wait()
            del self.processes[path]
            button.config(style="TButton")
        else:
            messagebox.showinfo("Info", f"{path} is not running.")

if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = App(root)
    root.mainloop()
