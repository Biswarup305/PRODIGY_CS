from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, output_path, key):
    """
    Encrypt an image by swapping pixels based on a key.

    Parameters:
    - image_path (str): Path to the input image.
    - output_path (str): Path to save the encrypted image.
    - key (int): Key used for encryption (acts as a seed for the random number generator).
    """
    # Open the image
    image = Image.open(image_path)
    pixels = np.array(image)

    # Get image dimensions
    height, width, channels = pixels.shape

    # Create a random permutation based on the key
    np.random.seed(key)
    permutation = np.random.permutation(height * width)

    # Flatten the pixel array for manipulation
    flat_pixels = pixels.reshape(-1, channels)

    # Apply the permutation to the pixels
    encrypted_pixels = flat_pixels[permutation]

    # Reshape back to the original image dimensions
    encrypted_pixels = encrypted_pixels.reshape(height, width, channels)

    # Create an encrypted image from the modified pixels
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path, format='PNG')  # Save as PNG format
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    """
    Decrypt an image by reversing the pixel swaps based on a key.

    Parameters:
    - image_path (str): Path to the encrypted image.
    - output_path (str): Path to save the decrypted image.
    - key (int): Key used for decryption (must be the same as the encryption key).
    """
    # Open the encrypted image
    image = Image.open(image_path)
    pixels = np.array(image)

    # Get image dimensions
    height, width, channels = pixels.shape

    # Create a random permutation based on the key
    np.random.seed(key)
    permutation = np.random.permutation(height * width)

    # Flatten the pixel array for manipulation
    flat_pixels = pixels.reshape(-1, channels)

    # Create an array to hold the decrypted pixels
    decrypted_pixels = np.zeros_like(flat_pixels)

    # Reverse the permutation
    decrypted_pixels[permutation] = flat_pixels

    # Reshape back to the original image dimensions
    decrypted_pixels = decrypted_pixels.reshape(height, width, channels)

    # Create a decrypted image from the modified pixels
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_path, format='PNG')  # Save as PNG format
    print(f"Decrypted image saved to {output_path}")

def main():
    """
    Main function to handle user input and perform encryption or decryption.
    """
    while True:
        action = input("Do you want to encrypt or decrypt an image? Input 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()
        if action == 'q':
            print("Exiting the program. Goodbye!")
            return
        elif action in ['e', 'd']:
            break
        else:
            print("Invalid action. Please choose 'e', 'd', or 'q' to quit.")

    # Get image paths and the encryption/decryption key
    image_path = input("Enter the path to the image: ").strip().replace('"', '')
    output_path = input("Enter the path to save the output image: ").strip().replace('"', '')
    key = int(input("Enter the encryption/decryption key: ").strip())

    if not os.path.isfile(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return

    if action == 'e':
        encrypt_image(image_path, output_path, key)
    elif action == 'd':
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
