import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Encryption
def encrypt_text(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

# Caesar Cipher Decryption
def decrypt_text(text, key):
    return encrypt_text(text, -key)
    
# Encrypt Button Function
def encrypt_button():
    try:
        key = int(key_entry.get())
        text = input_entry.get("1.0", tk.END).strip()

        encrypted = encrypt_text(text, key)

        encrypt_entry.delete("1.0", tk.END)
        encrypt_entry.insert(tk.END, encrypted)

    except ValueError:
        messagebox.showerror("Invalid Input", "Key must be an integer.")

# Decrypt Button Function
def decrypt_button():
    try:
        key = int(key_entry.get())
        text = encrypt_entry.get("1.0", tk.END).strip()

        decrypted = decrypt_text(text, key)

        decrypt_entry.delete("1.0", tk.END)
        decrypt_entry.insert(tk.END, decrypted)

    except ValueError:
        messagebox.showerror("Invalid Input", "Key must be an integer.")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher GUI")
root.geometry("600x500")

# Input Text Box
tk.Label(root, text="Enter Text:").pack(pady=5)

input_entry = tk.Text(root, height=3, width=40)
input_entry.pack(pady=5)

# Key Input
tk.Label(root, text="Enter Key (integer):").pack(pady=5)

key_entry = tk.Entry(root, width=10)
key_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt",
    command=encrypt_button,
    width=10
)
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt",
    command=decrypt_button,
    width=10
)
decrypt_btn.grid(row=0, column=1, padx=5)

exit_btn = tk.Button(
    button_frame,
    text="Exit",
    command=root.quit,
    width=10,
    fg="red"
)
exit_btn.grid(row=0, column=2, padx=5)

# Encryption Output
tk.Label(root, text="Encrypt Result:").pack(pady=5)

encrypt_entry = tk.Text(root, height=3, width=40)
encrypt_entry.pack(pady=5)

# Decryption Output
tk.Label(root, text="Decrypt Result:").pack(pady=5)

decrypt_entry = tk.Text(root, height=3, width=40)
decrypt_entry.pack(pady=5)

root.mainloop()
