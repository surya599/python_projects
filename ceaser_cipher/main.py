from cipherart import logo
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def encrypt(text,shift):
    cipher_text = ""
    for letter in text:
        shift_position = (alphabets.index(letter) + shift) % 26
        cipher_text += alphabets[shift_position]
    return cipher_text

def decrypt(ciphertext,shift):
    original_text = ""
    for letter in ciphertext:
        shiftposition = (alphabets.index(letter) - shift) %26
        original_text += alphabets[shiftposition]
    return original_text

print(logo)
direction =  input("Type 'encode' to encrypt:\n")
text = input(f"Enter the text you want to {direction} :\n").lower()
shift = int(input("enter the shift number: \n"))
if direction == 'encode':
    cipher_text = encrypt(text,shift)
    print(f"the encrypted text is {cipher_text}")
else :
    print("thank you")
direction = input("type 'decode' to decrypt the message 0 to stop ")
if direction == 'decode':
    original_text = decrypt(cipher_text,shift)
    print(f"the decoded message is {original_text}")
else:
    print("Thank you")
