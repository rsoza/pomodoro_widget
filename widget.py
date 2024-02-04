import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime
import pandas as pd
import os


class Widget:
    def __init__(self, root):
        self.root = root
        # TODO: make this relatable to timer
        self.df = pd.read_csv("schedule.csv", index_col=False) if os.path.exists('schedule.csv') else False
        self.front_frame = ttk.Frame(self.root)
        self.back_frame = ttk.Frame(self.root)
        self.remaining_time = 1800 
        self.original_time = 1800
        self.gui()
        self.front_text()
        self.back_text()
        self.show_front()
        self.start_timer()
        self.schedule()

       

    def gui(self):
        root.title("Widget")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 200
        window_height = 100
        root.geometry(f"{window_width}x{window_height}+{screen_width - window_width - 10}+{screen_height - window_height - 30}")
        root.overrideredirect(True)
        root.resizable(False, False)
        root.attributes('-topmost', True)
        root.configure(bg="black")

    def schedule(self):
        if type(self.df) == bool:
            print("Add tasks to your schedule")
            self.edit_schedule(False)
        else:
            print("Do you want to add something to your schedule? [y/n]")
            input1 = input().lower()
            valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}

            if valid[input1]:
                self.edit_schedule(True)

        print("conti")
        
    
    
    def edit_schedule(self, header):
        time_format = '%H:%M:%S'
        print("Start time of task: ")
        start=input()
        start = datetime.strptime(start, time_format)
        print("End time of task: ")
        end=input()
        end = datetime.strptime(end, time_format)
        print("Task: ")
        task=input()
        data = [[start, end, task]]
        df = pd.DataFrame(data, columns=['start', 'end', 'task'])   
        print(df)   
        if header:
            df.to_csv("schedule.csv", mode='a', header=False, index=False)
        else:
            df.to_csv("schedule.csv", index=False)
            
        self.df = pd.read_csv("schedule.csv", index_col=False) 
        print(self.df) 
        self.schedule()

    def front_text(self):
        text = "Read oop in c++ \nor 6502 processor\n instructions" if self.original_time == 1800 else "Take a break "
        self.timer_label = ttk.Label(self.front_frame, text="00:00", font=("Helvetica", 24), foreground="white", background="black")
        self.example = ttk.Label(self.front_frame, text=text, font=("Helvetica", 11), foreground="white", background="black")
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

    def update_timer(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        hours, minutes = divmod(minutes, 60)
        time_format = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

        # Update the timer label
        self.timer_label.config(text=time_format)
        self.remaining_time -= 1
        
        if self.remaining_time < 0:
            # Stop the timer
            if self.original_time == 1800:
                self.remaining_time = 900
                self.original_time = 900
            else:
                self.remaining_time = 1800
                self.original_time = 1800

if __name__ == "__main__":
    root = tk.Tk()
    app = Widget(root)

    # Bind mouse click event to flip between front and back
    root.bind("<Button-1>", lambda event: app.show_back() if app.front_frame.winfo_ismapped() else app.show_front())

    root.mainloop()
