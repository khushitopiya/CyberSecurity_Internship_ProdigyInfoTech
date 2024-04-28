from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Example encryption: adding the key value to each color channel
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            encrypted_pixel = (r, g, b)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Example decryption: subtracting the key value from each color channel
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            decrypted_pixel = (r, g, b)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

def main():
    input_image = input("Enter the path of the input image: ")
    output_image = input("Enter the path to save the output image: ")

    # Prompt the user until a valid integer is entered for the key
    while True:
        try:
            key = int(input("Enter the encryption/decryption key (an integer): "))
            break  # Exit the loop if a valid integer is entered
        except ValueError:
            print("Invalid input. Please enter an integer for the key.")

    choice = input("Encrypt or Decrypt? (E/D): ").upper()

    if choice == "E":
        encrypt_image(input_image, output_image, key)
    elif choice == "D":
        decrypt_image(input_image, output_image, key)
    else:
        print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")

if __name__ == "__main__":
    main()