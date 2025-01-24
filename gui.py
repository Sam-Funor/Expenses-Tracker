from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk
from flow import Categories, Show_Frame, Update_Tree, Create_Category, Add, Calculate, Save_Expenses, Load_Expenses, Countdown

def Setup_GUI(Root):

    Frame_1 = tk.Frame(Root)
    Frame_2 = tk.Frame(Root)
    Frame_3 = tk.Frame(Root)
    Frame_4 = tk.Frame(Root)

    for Frame in (Frame_1, Frame_2, Frame_3, Frame_4):
        Frame.grid(row=0, column=0, sticky="nsew")

    Label_1 = tk.Label(Frame_1, text="Welcome to Expenses Tracker", font=(25))
    Label_1.pack(pady=15)
    Button_1_0 = tk.Button(Frame_1, text="Add Expenses", command=lambda: Show_Frame(Frame_2))
    Button_1_0.pack(pady=10)
    Button_1_1 = tk.Button(Frame_1, text="View Expenses", command=lambda: Show_Frame(Frame_3))
    Button_1_1.pack(pady=10)
    Button_1_2 = tk.Button(Frame_1, text="Calculate Total", command=lambda: Show_Frame(Frame_4))
    Button_1_2.pack(pady=10)
    Button_Exit = tk.Button(Frame_1, text="Exit", command=lambda: Countdown(Countdown_Label, Root))
    Button_Exit.pack(pady=10)

    Label_2_0 = tk.Label(Frame_2, text="Name of Expense")
    Label_2_0.pack()
    Entry_Name = tk.Entry(Frame_2)
    Entry_Name.pack()
    Label_2_1 = tk.Label(Frame_2, text="Amount of Expense")
    Label_2_1.pack()
    Entry_Value = tk.Entry(Frame_2)
    Entry_Value.pack()
    Label_2_2 = tk.Label(Frame_2, text="Create a Category")
    Label_2_2.pack()
    Entry_Category = tk.Entry(Frame_2)
    Entry_Category.pack()
    Button_Category = tk.Button(Frame_2, text="Create Category", command=lambda: Create_Category(Entry_Category, Category_Dropdown, Label_Category_Status, Tree, Label_3_0))
    Button_Category.pack(pady=5)
    Label_Category_Status = tk.Label(Frame_2, text="", fg="green")
    Label_Category_Status.pack()
    Category_Dropdown = ttk.Combobox(Frame_2, state="readonly", values=list(Categories.keys()))
    Category_Dropdown.pack()
    Label_2_3 = tk.Label(Frame_2, text="", fg="red")
    Label_2_3.pack()
    Button_Add = tk.Button(Frame_2, text="Add Expense", command=lambda: Add(Entry_Name, Entry_Value, Label_2_3, Category_Dropdown, Tree, Label_3_0))
    Button_Add.pack(pady=5)
    Button_Back_2 = tk.Button(Frame_2, text="Go Back", command=lambda: Show_Frame(Frame_1))
    Button_Back_2.pack(pady=10)

    Tree = ttk.Treeview(Frame_3, columns=("Amount"), show="tree headings", height=10)
    Tree.heading("#0", text="Name", anchor="w")
    Tree.heading("Amount", text="Amount ($)", anchor="e")
    Tree.column("#0", width=200, anchor="w")
    Tree.column("Amount", width=100, anchor="e")
    Tree.pack(pady=10)
    Label_3_0 = tk.Label(Frame_3, text="No Expenses Recorded Yet.")
    Label_3_0.pack()
    Button_Back_3 = tk.Button(Frame_3, text="Go Back", command=lambda: Show_Frame(Frame_1))
    Button_Back_3.pack(pady=10)

    Calculate_Button = tk.Button(Frame_4, text="Calculate Total", command=lambda: Calculate(Total_Label))
    Calculate_Button.pack(pady=10)
    Total_Label = tk.Label(Frame_4, text="Total: $0")
    Total_Label.pack(pady=5)
    Button_Back_4 = tk.Button(Frame_4, text="Go Back", command=lambda: Show_Frame(Frame_1))
    Button_Back_4.pack(pady=10)

    Countdown_Label = tk.Label(Root, text="", font=("Arial", 10))
    Countdown_Label.grid()

    Load_Expenses(Category_Dropdown, Tree, Label_3_0)
    Show_Frame(Frame_1)

    Update_Tree(Tree, Label_3_0)
    Save_Expenses()