import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")  # ✅ Use PNG format

# Check if image loaded successfully
if img is None:
    print("❌ Error: Image not loaded. Check the file path or format.")
    exit()

# Get the original passcode
original_passcode = input("Enter the original passcode used for encryption: ")

# Mapping ASCII to characters (including 255)
c = {i: chr(i) for i in range(256)}  # Include 255

# User input for decryption
pas = input("Enter passcode for Decryption: ")

# Decrypt only if passcode matches
if original_passcode == pas:
    message = ""
    n = m = z = 0

    while True:
        # Check boundaries
        if m >= img.shape[1]:
          
            break

        pixel_value = img[n, m, z]

   # Handle unexpected values
        if pixel_value not in c:
            
            break

        char = c[pixel_value]
        message += char

        # Break if end marker is found
        if "$END$" in message:
           
            message = message.replace("$END$", "")
            break

        # Move to the next pixel
        n += 1
        if n >= img.shape[0]:  # If end of row, move to next column
            n = 0
            m += 1
        z = (z + 1) % 3  # Cycle through RGB

    print("\nDecrypted message:", message)
else:
    print("❌ YOU ARE NOT AUTHORIZED")
