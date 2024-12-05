from PIL import Image
import os

# Define a function for encryption
def encrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        pixels = img.load()

        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]

                # Swapping red and blue channels
                encrypted_pixel = (b, g, r)

                pixels[i, j] = encrypted_pixel

        img.save(output_path)
        print(f"Image encrypted successfully! Saved as {output_path}")
    except Exception as e:
        print(f"Error encrypting image: {e}")

# Define a function for decryption
def decrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        pixels = img.load()

        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]

                # Swapping red and blue channels back
                decrypted_pixel = (b, g, r)

                pixels[i, j] = decrypted_pixel

        img.save(output_path)
        print(f"Image decrypted successfully! Saved as {output_path}")
    except Exception as e:
        print(f"Error decrypting image: {e}")

# Function to get image paths securely using environment variables
def get_image_paths():
    input_image = os.getenv('INPUT_IMAGE_PATH', 'default_input_image.png')
    encrypted_image = os.getenv('ENCRYPTED_IMAGE_PATH', 'default_encrypted_image.png')
    decrypted_image = os.getenv('DECRYPTED_IMAGE_PATH', 'default_decrypted_image.png')

    return input_image, encrypted_image, decrypted_image

if __name__ == "__main__":
    # Fetch image paths from environment variables or use defaults
    input_image, encrypted_image, decrypted_image = get_image_paths()

    # Encrypt the image
    encrypt_image(input_image, encrypted_image, key=None)

    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image, key=None)

