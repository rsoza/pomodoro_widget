
from tkinter import ttk


class Interface:
    def __init__(self, root) -> None:
        self.root = root
        self.front_frame = ttk.Frame(self.root)
        self.back_frame = ttk.Frame(self.root)
        self.remaining_time = 1800
        self.original_time = 1800
        self.text = "Read oop in c++ \nor 6502 processor\n instructions"
   
        self.gui()
        self.front_text()
        self.back_text()
        self.show_front()

    def gui(self):
        self.root.title("Widget")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 200
        window_height = 100
        self.root.geometry(f"{window_width}x{window_height}+{screen_width - window_width - 10}+{screen_height - window_height - 30}")
        self.root.overrideredirect(True)
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)
        self.root.configure(bg="black")

    def front_text(self):
        self.timer_label = ttk.Label(self.front_frame, text="00:00", font=("Helvetica", 24), foreground="white", background="black")
        self.example = ttk.Label(self.front_frame, text=self.text, font=("Helvetica", 11), foreground="white", background="black")
        self.timer_label.pack()
        self.example.pack()
        self.example.configure(background="black")
        # pady=10

    def show_front(self):
        self.front_frame.pack()
        self.back_frame.pack_forget()

    def show_back(self):
        self.front_frame.pack_forget()
        self.back_frame.pack()

    def start_timer(self):
        self.update_timer()
        self.root.after(1000, self.start_timer)

    def back_text(self):
        self.schedule_label = ttk.Label(self.back_frame, text="Next task: Do something", font=("Helvetica", 12), foreground="white", background="black")
        self.schedule_label.pack()
