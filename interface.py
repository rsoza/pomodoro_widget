class Interface:
    def __init__(self, root) -> None:
        self.root = root
    

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