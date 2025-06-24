def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


plaintext = "Hello, World!"
shift = 3
encrypted = caesar_encrypt(plaintext, shift)
decrypted = caesar_decrypt(encrypted, shift)

print(f"Original message ====>: {plaintext}")
print(f"Encrypted message=====>: {encrypted}")
print(f"Decrypted message=====>: {decrypted}")