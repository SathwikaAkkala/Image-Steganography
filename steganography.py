import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Convert text to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text) + '1111111111111110'  # End delimiter

# Convert binary to text
def binary_to_text(binary_str):
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if int(char, 2) != 65534)

# Hide text in image
def encode_image():
    file_path = filedialog.askopenfilename(title="Select Image")
    if not file_path:
        return

    img = cv2.imread(file_path)
    secret_text = text_entry.get()

    if not secret_text:
        messagebox.showerror("Error", "Enter text to hide", parent=root)
        return

    binary_secret = text_to_binary(secret_text)
    data_index = 0
    binary_len = len(binary_secret)

    rows, cols, channels = img.shape
    for row in range(rows):
        for col in range(cols):
            for channel in range(3):  # Modify RGB channels
                if data_index < binary_len:
                    img[row, col, channel] = (img[row, col, channel] & ~1) | int(binary_secret[data_index])
                    data_index += 1
                else:
                    break

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        cv2.imwrite(save_path, img)
        messagebox.showinfo("Success", "Data hidden successfully!", parent=root)

# Extract hidden text from image
def decode_image():
    file_path = filedialog.askopenfilename(title="Select Image")
    if not file_path:
        return

    img = cv2.imread(file_path)
    binary_data = ""

    for row in img:
        for pixel in row:
            for channel in pixel:
                binary_data += str(channel & 1)

    delimiter = '1111111111111110'
    if delimiter in binary_data:
        binary_data = binary_data[:binary_data.index(delimiter)]

    hidden_text = binary_to_text(binary_data)

    # Full-screen popup for decoded message
    popup = tk.Toplevel(root)
    popup.title("Decoded Message")
    popup.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    popup.configure(bg="#34495E")

    label = tk.Label(popup, text="Decoded Message:", font=("Arial", 18, "bold"), fg="white", bg="#34495E")
    label.pack(pady=20)

    text_display = tk.Text(popup, wrap=tk.WORD, font=("Arial", 16), height=10, width=60)
    text_display.insert(tk.END, hidden_text)
    text_display.pack(pady=20)

    close_btn = tk.Button(popup, text="Close", font=("Arial", 14), bg="#E74C3C", fg="white", command=popup.destroy)
    close_btn.pack(pady=10)

    popup.mainloop()

# GUI Setup
root = tk.Tk()
root.title("Image Steganography")

# Make window adaptive to screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{int(screen_width * 0.5)}x{int(screen_height * 0.5)}")

root.configure(bg="#2C3E50")

# Title Label
title_label = tk.Label(root, text="🔒 Image Steganography 🔒", font=("Arial", 18, "bold"), fg="white", bg="#2C3E50")
title_label.pack(pady=10)

# Input Field
text_label = tk.Label(root, text="Enter Text to Hide:", font=("Arial", 12), fg="white", bg="#2C3E50")
text_label.pack(pady=5)

text_entry = tk.Entry(root, width=50, font=("Arial", 14), bd=3, relief="ridge", fg="black", bg="white", insertbackground="black", show="*")

text_entry.pack(pady=5)

# Buttons
btn_style = {"font": ("Arial", 12, "bold"), "width": 20, "height": 2}

encode_btn = tk.Button(root, text="🔐 Encode Image", bg="#16A085", fg="white", **btn_style, command=encode_image)
encode_btn.pack(pady=10)

decode_btn = tk.Button(root, text="🔓 Decode Image", bg="#2980B9", fg="white", **btn_style, command=decode_image)
decode_btn.pack(pady=10)

root.mainloop()
