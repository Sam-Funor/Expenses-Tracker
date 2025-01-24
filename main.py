from ttkthemes import ThemedTk
import tkinter as tk
from gui import Setup_GUI

if __name__ == "__main__":
    Root = ThemedTk(theme="clam")
    Root.title("Expenses Tracker")
    Root.geometry("330x400")

    Setup_GUI(Root)

    Root.mainloop()