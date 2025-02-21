import cv2
import os

# Load the image
img = cv2.imread("mydata.webp")  # Replace with your image path

# Check if image loaded successfully
if img is None:
    print("Error: Image not loaded. Check the file path or format.")
    exit()

# Get the message and passcode
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Append an end marker to the message
msg += "$END$"

# Create character to ASCII mapping
d = {chr(i): i for i in range(255)}

# Initialize pixel positions
n = m = z = 0

# Embed the message into the image
for char in msg:
    img[n, m, z] = d[char]
    n += 1
    if n >= img.shape[0]:  # Move to next row if end of column is reached
        n = 0
        m += 1
    z = (z + 1) % 3

# Save and open the encrypted image
cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Use 'start' for Windows
