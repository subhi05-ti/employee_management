
import tkinter as tk
from tkinter import ttk, messagebox

from employee import *

def add():
    try:
        add_employee(
            int(e1.get()), e2.get(),
            int(e3.get()), int(e4.get())
        )
        messagebox.showinfo("Success", "Employee Added")
        display()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def remove():
    try:
        result = remove_employee(int(e1.get()))

        if result:
            messagebox.showinfo("Success", "Employee Removed")
        else:
            messagebox.showwarning("Error", "Employee Not Found")

        display()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def update():
    try:
        result = update_employee(
            int(e1.get()), e2.get(),
            int(e3.get()), int(e4.get())
        )

        if result:
            messagebox.showinfo("Success", "Employee Updated")
        else:
            messagebox.showwarning("Error", "Employee Not Found")

        display()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def display():
    for row in table.get_children():
        table.delete(row)

    for emp in get_all_employees():
        table.insert("", tk.END, values=emp)


def run_gui():
    global e1, e2, e3, e4, table

    root = tk.Tk()
    root.title("Employee Management System")
    root.geometry("650x450")

    tk.Label(
        root, text="Employee Management System",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack()

    labels = ["ID", "Name", "Salary", "Age"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(frame, text=label).grid(row=i, column=0, pady=5)
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1)
        entries.append(entry)

    e1, e2, e3, e4 = entries

    btn = tk.Frame(root)
    btn.pack(pady=15)

    tk.Button(btn, text="Add Employee", command=add).grid(row=0, column=0, padx=5)
    tk.Button(btn, text="Remove Employee", command=remove).grid(row=0, column=1, padx=5)
    tk.Button(btn, text="Update Employee", command=update).grid(row=0, column=2, padx=5)
    tk.Button(btn, text="Display Employees", command=display).grid(row=0, column=3, padx=5)

    table = ttk.Treeview(
        root,
        columns=("ID", "Name", "Salary", "Age"),
        show="headings"
    )

    for col in ("ID", "Name", "Salary", "Age"):
        table.heading(col, text=col)
        table.column(col, width=130)

    table.pack(fill="x", padx=15, pady=10)

    display()

    root.mainloop()
