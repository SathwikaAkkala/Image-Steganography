**Image Steganography**

**Project Description:**

This project implements Image Steganography, allowing users to securely hide text messages inside images using the Least Significant Bit (LSB) technique. The application is built using Python with a graphical user interface (GUI) powered by Tkinter.

**Features:**

Hide Text in an Image: Securely embed secret messages into an image.

Extract Hidden Text: Decode and retrieve the hidden message from a stego-image.

Password Protection: Option to mask the entered text for privacy.

User-Friendly GUI: Built with Tkinter for an intuitive interface.

Full-Screen Pop-up: The extracted text appears in a full-screen pop-up window.

**Technologies Used:**

Python (3.x)

OpenCV (cv2) for image processing

NumPy (numpy) for numerical operations

Tkinter for GUI

Pillow (PIL.ImageTk) for image handling in the GUI

**Installation & Setup:**

Prerequisites

Ensure you have Python installed. You can download it from Python's official website.

Install Dependencies

Run the following command to install the required Python libraries:

pip install opencv-python numpy pillow

Run the Application

To start the steganography tool, execute:

python steganography.py

**Usage Guide**

Encoding (Hiding Text in Image)

Enter your secret message in the text box.

Click "Encode Image" and select an image.

The encoded image will be saved after choosing a destination.

Decoding (Extracting Hidden Text)

Click "Decode Image" and select a stego-image.

The hidden text will be displayed in a full-screen pop-up.

**GUI Overview:**

Dark-Themed Interface with an attractive UI.

Buttons for encoding and decoding messages.

Password Protection (masked input for hidden messages).



Developed by: Sathwika Akkala
