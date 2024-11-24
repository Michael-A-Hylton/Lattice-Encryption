import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def run_encryption():
    file_path = file_input_encrypt.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a file to encrypt.")
        return
    try:
        # Run the encryption script
        subprocess.run(["python", "encryption_program.py"], input=f"{file_path}\n", text=True)
        messagebox.showinfo("Success", "File encrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def run_decryption():
    file_path = file_input_decrypt.get()
    decrypted_name = decrypted_file_name.get()
    if not file_path or not decrypted_name:
        messagebox.showerror("Error", "Please select a file and provide a name for the decrypted file.")
        return
    try:
        # Run the decryption script
        subprocess.run(["python", "decryption_program.py"], input=f"{file_path}\n{decrypted_name}\n", text=True)
        messagebox.showinfo("Success", "File decrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_file(entry_field):
    file_path = filedialog.askopenfilename()
    entry_field.delete(0, tk.END)
    entry_field.insert(0, file_path)

# Create the main application window
root = tk.Tk()
root.title("Encryption and Decryption Program")

# Encryption Section
tk.Label(root, text="Encrypt a File").grid(row=0, column=0, padx=10, pady=5, sticky="w")
file_input_encrypt = tk.Entry(root, width=50)
file_input_encrypt.grid(row=1, column=0, padx=10, pady=5)
tk.Button(root, text="Browse", command=lambda: select_file(file_input_encrypt)).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Encrypt", command=run_encryption).grid(row=1, column=2, padx=10, pady=5)

# Decryption Section
tk.Label(root, text="Decrypt a File").grid(row=2, column=0, padx=10, pady=5, sticky="w")
file_input_decrypt = tk.Entry(root, width=50)
file_input_decrypt.grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Browse", command=lambda: select_file(file_input_decrypt)).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Decrypted File Name").grid(row=4, column=0, padx=10, pady=5, sticky="w")
decrypted_file_name = tk.Entry(root, width=50)
decrypted_file_name.grid(row=5, column=0, padx=10, pady=5)
tk.Button(root, text="Decrypt", command=run_decryption).grid(row=5, column=2, padx=10, pady=5)

# Run the application
root.mainloop()
