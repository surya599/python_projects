import qrcode

url = input("Enter the URL: ")

# Provide the full file path along with file name before running the program
# Example (Windows):
# C:\\Users\\YourName\\Desktop\\qrcode_image.png
file_path = ""

qr = qrcode.QRCode()
qr.add_data(url)

image = qr.make_image()

image.save(file_path)

print("QR CODE CREATED SUCCESSFULLY")
