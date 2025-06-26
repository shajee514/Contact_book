import tkinter as tk
from tkinter import messagebox

# Function to save contact
def save_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Input Error", "Please enter both name and phone.")
        return

    with open("contacts.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Phone: {phone}\n")
        file.write("-----\n")

    messagebox.showinfo("Success", "Contact saved successfully!")
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Function to view contacts
def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            data = file.read()
    except FileNotFoundError:
        data = "No contacts saved yet."

    contact_window = tk.Toplevel(root)
    contact_window.title("Saved Contacts")

    text_box = tk.Text(contact_window, width=40, height=15)
    text_box.pack(padx=10, pady=10)
    text_box.insert(tk.END, data)
    text_box.config(state="disabled")  # Make it read-only

# GUI Layout
root = tk.Tk()
root.title("Contact Book")

tk.Label(root, text="Enter Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Phone:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Save Contact", command=save_contact).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="View Contacts", command=view_contacts).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
