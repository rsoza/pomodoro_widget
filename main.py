from widget import Widget
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = Widget(root)

    # Bind mouse click event to flip between front and back
    root.bind("<Button-1>", lambda event: app.show_back()
              if app.front_frame.winfo_ismapped() else app.show_front())

    root.mainloop()
