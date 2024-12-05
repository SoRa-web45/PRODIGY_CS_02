import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog, simpledialog
import os

# Function to open the file dialog and select an image
def select_image():
    root = tk.Tk()
    root.withdraw()  # Hide the Tkinter root window
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    return file_path

# Function to save the encrypted image
def save_image(image, filename):
    image.save(filename)
    print(f"Image saved as {filename}")

# Function to shift RGB channels independently with overflow prevention
def shift_channels(pixels, shift_value):
    # Ensure that the pixel values stay within [0, 255] range after shifting
    pixels[..., 0] = (pixels[..., 0] + shift_value) % 256  # Red channel
    pixels[..., 1] = (pixels[..., 1] + shift_value) % 256  # Green channel
    pixels[..., 2] = (pixels[..., 2] + shift_value) % 256  # Blue channel
    return pixels

# Function to encrypt an image with pixel manipulation
def encrypt_image(image_path, shift_value):
    image = Image.open(image_path)
    pixels = np.array(image)  # Convert image to numpy array
    
    # Encrypt by shifting RGB values
    pixels = shift_channels(pixels, shift_value)
    
    encrypted_image = Image.fromarray(pixels.astype(np.uint8))
    return encrypted_image

# Function to decrypt an image (reversing the encryption process)
def decrypt_image(image_path, shift_value):
    image = Image.open(image_path)
    pixels = np.array(image)  # Convert image to numpy array
    
    # Reverse the shifting of channels
    pixels = shift_channels(pixels, -shift_value)
    
    decrypted_image = Image.fromarray(pixels.astype(np.uint8))
    return decrypted_image

# Main function to interact with the user
def main():
    print("Welcome to the Image Encryption Tool!")
    
    # Ask for image selection
    image_path = select_image()
    if not image_path:  # If no image is selected, exit
        print("No image selected. Exiting.")
        return

    # Ask for the shift value for encryption
    shift_value = int(simpledialog.askstring("Shift Value", "Enter the shift value for encryption (e.g., 50):", initialvalue="50"))
    
    # Encrypt the image
    encrypted_image = encrypt_image(image_path, shift_value)
    filename = os.path.basename(image_path).split('.')[0] + "_encrypted.png"
    save_image(encrypted_image, filename)

    # Ask the user if they want to decrypt the image
    decrypt_option = simpledialog.askstring("Decrypt Option", "Do you want to decrypt the image? (yes/no)").lower()
    
    if decrypt_option == "yes":
        decrypted_image = decrypt_image(filename, shift_value)
        decrypted_filename = os.path.basename(filename).split('.')[0] + "_decrypted.png"
        save_image(decrypted_image, decrypted_filename)
    
    print("Operation completed.")

if __name__ == "__main__":
    main()
