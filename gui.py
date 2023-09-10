# gui.py

import tkinter as tk
from tkinter import simpledialog

def get_project_info():
    root = tk.Tk()
    root.title("Project Information")

    # Create labels and entry fields for project attributes
    tk.Label(root, text="Project Name:").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Project Address:").pack()
    address_entry = tk.Entry(root)
    address_entry.pack()

    tk.Label(root, text="Project ID:").pack()
    id_entry = tk.Entry(root)
    id_entry.pack()

    tk.Label(root, text="Project Manager:").pack()
    manager_entry = tk.Entry(root)
    manager_entry.pack()

    tk.Label(root, text="Project PO:").pack()
    po_entry = tk.Entry(root)
    po_entry.pack()

    tk.Label(root, text="Project Invoice:").pack()
    invoice_entry = tk.Entry(root)
    invoice_entry.pack()

    # Create an OK button to submit the form
    def submit():
        name = name_entry.get()
        address = address_entry.get()
        id = id_entry.get()
        manager = manager_entry.get()
        po = po_entry.get()
        invoice = invoice_entry.get()

        root.destroy()  # Close the window

        # Return the collected project information as a tuple
        return name, address, id, manager, po, invoice

    tk.Button(root, text="OK", command=submit).pack()

    root.mainloop()
