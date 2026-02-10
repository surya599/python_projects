QR Code Generator using Python

This Python script generates a QR code for a user-entered URL and saves it as a PNG image.

Requirements

Python 3

qrcode library

Install the library using:

pip install qrcode[pil]

How It Works

The user enters a URL

The QR code is generated using the qrcode module

The image is saved to a user-defined file path

Important Note (File Path)

The file path is hard-coded

The path must exist on the system

The path should be changed when running on another device

Example:

C:\\Users\\YourName\\Desktop\\qrcode_using_pythoncode.png

(use this double back slashes)

If the path is incorrect or does not exist, the program will fail to save the file.

Output

A PNG image containing the QR code

Message printed after successful creation

Author

Velagala Surya Bhuvaneswara Reddy
