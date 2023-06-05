import tkinter as tk
from tkinter import messagebox, filedialog


def save_data():
    name = name_entry.get()
    ID = ID_entry.get()
    DOB = DOB_entry.get()
    background = background_entry.get()

    with open("user_data.txt", "w") as f:
        f.write("Name: " + name + "\n")
        f.write("ID: " + ID + "\n")
        f.write("DOB: " + DOB + "\n")
        f.write("Background: " + background + "\n")
    messagebox.showinfo("Info", "Data has been saved to user_data.txt")


def open_file():
    os.startfile("user_data.txt")


def search_data():
    search_term = search_entry.get()
    search_results = ""
    with open("user_data.txt", "r") as f:
        for line in f:
            if search_term in line:
                search_results += line
    if search_results:
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert("1.0", search_results)
        result_text.config(state="disabled")
    else:
        messagebox.showinfo("Info", "No results found for: " + search_term)


root = tk.Tk()
root.title("User Data")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

ID_label = tk.Label(root, text="ID:")
ID_label.grid(row=1, column=0)
ID_entry = tk.Entry(root)
ID_entry.grid(row=1, column=1)

DOB_label = tk.Label(root, text="DOB:")
DOB_label.grid(row=2, column=0)
DOB_entry = tk.Entry(root)
DOB_entry.grid(row=2, column=1)

background_label = tk.Label(root, text="Background:")
background_label.grid(row=3, column=0)
background_entry = tk.Entry(root)
background_entry.grid(row=3, column=1)

save_button = tk.Button(root, text="Save", command=save_data)
save_button.grid(row=4, column=0)

open_file_button = tk.Button(root, text="Open File", command=open_file)
open_file_button.grid(row=4, column=1)

root.mainloop()
