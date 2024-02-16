
from interface import Interface
from datetime import datetime
import pandas as pd
import time
import os

class Widget(Interface):
    def __init__(self, root):
        super().__init__(root)
        # TODO: make this relatable to timer
        self.df = pd.read_csv("schedule.csv", index_col=False) if os.path.exists('schedule.csv') else False

        self.start_timer()
        self.schedule()    


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

    def start_timer(self):
        self.update_timer()
        self.root.after(1000, self.start_timer)

   
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
                self.text = "Take a break"
            else:
                self.remaining_time = 1800
                self.original_time = 1800
                self.text = "Read oop or 6502"

