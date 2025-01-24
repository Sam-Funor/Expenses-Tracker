import tkinter as tk
import os

Categories = {}

def Show_Frame(Frame):
    Frame.tkraise()

def Update_Tree(Tree, Label_3_0):
    Tree.delete(*Tree.get_children())
    if not Categories:
        Label_3_0.pack()
    else:
        Label_3_0.pack_forget()
        for category, items in Categories.items():
            category_id = Tree.insert("", "end", text=category, open=True)
            for item, value in items:
                Tree.insert(category_id, "end", text=item, values=(f"${value}"))

def Create_Category(Entry_Category, Category_Dropdown, Label_Category_Status, Tree, Label_3_0):
    Category = Entry_Category.get().strip()
    if Category:
        if Category not in Categories:
            Categories[Category] = []
            Update_Tree(Tree, Label_3_0)
            Category_Dropdown["values"] = list(Categories.keys())
            Label_Category_Status.config(text=f"Category '{Category}' Created!", fg="green")
        else:
            Label_Category_Status.config(text=f"Category '{Category}' Already Exists!", fg="red")
    else:
        Label_Category_Status.config(text="Please create or select a category.", fg="red")
    Entry_Category.delete(0, tk.END)

def Add(Entry_Name, Entry_Value, Label_2_3, Category_Dropdown, Tree, Label_3_0):
    Item = Entry_Name.get().strip()
    try:
        Value = int(Entry_Value.get())
    except ValueError:
        Label_2_3.config(text="Invalid Amount! Please Enter a Number.", fg="red")
        return
    Category = Category_Dropdown.get().strip()
    if Item and Category:
        if Category in Categories:
            Categories[Category].append((Item, Value))
            Update_Tree(Tree, Label_3_0)
            Entry_Name.delete(0, tk.END)
            Entry_Value.delete(0, tk.END)
            Label_2_3.config(text="")
        else:
            Label_2_3.config(text=f"Category '{Category}' Does Not Exist!", fg="red")
    else:
        Label_2_3.config(text="Please Fill in All Fields!", fg="red")

def Calculate(Total_Label):
    Total = sum(value for items in Categories.values() for _, value in items)
    Total_Label.config(text=f"Total: ${Total}")

def Save_Expenses():
    File_Path = os.path.join(os.getcwd(), "Expenses.txt")
    try:
        with open(File_Path, "w") as File:
            for category, items in Categories.items():
                File.write(f"Category:{category}\n")
                for item, value in items:
                    File.write(f"{item},{value}\n")
        print(f"Expenses Saved Successfully to {File_Path}.")
    except Exception as e:
        print(f"Error Saving Expenses: {e}")

def Load_Expenses(Category_Dropdown, Tree, Label_3_0):
    File_Path = os.path.join(os.getcwd(), "Expenses.txt")
    if os.path.exists(File_Path):
        try:
            with open(File_Path, "r") as File:
                current_category = None
                for line in File:
                    line = line.strip()
                    if line.startswith("Category:"):
                        current_category = line[len("Category:"):].strip()
                        if current_category not in Categories:
                            Categories[current_category] = []
                    elif "," in line:
                        parts = line.split(",", 1)
                        if len(parts) == 2:
                            item, value = parts
                            try:
                                value = int(value)
                                if current_category:
                                    Categories[current_category].append((item.strip(), value))
                            except ValueError:
                                print(f"Invalid Value in Line: '{line}' - Skipping.")
                        else:
                            print(f"Skipping malformed line: '{line}'")
            Update_Tree(Tree, Label_3_0)
            Category_Dropdown["values"] = list(Categories.keys())
        except Exception as e:
            print(f"Error Loading Expenses: {e}")

def Countdown(Countdown_Label, Root):
    global seconds
    if seconds > 0:
        Countdown_Label.config(text=f"Thank you for using the Expense Tracker!\nClosing in {seconds} Seconds...")
        seconds -= 1
        Root.after(1000, lambda: Countdown(Countdown_Label, Root))
    else:
        Save_Expenses()
        Root.destroy()
seconds = 5