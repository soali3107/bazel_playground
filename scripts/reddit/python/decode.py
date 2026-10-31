import base64

# Read the image file as binary data
with open('Screenshot 2024-03-16 at 12.26.44.png', 'rb') as image_file:
    image_data = image_file.read()

# Encode the image data as Base64
encoded_image = base64.b64encode(image_data)

# Decode the Base64-encoded image data back to binary
decoded_image = base64.b64decode(encoded_image)

print("encoded: " + str(encoded_image))
print("decoded: " + str(decoded_image))
# Write the decoded image data to a new file
with open('decoded_image.png', 'wb') as decoded_image_file:
    decoded_image_file.write(decoded_image)
