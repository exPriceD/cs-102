import string


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    alphabet = string.ascii_lowercase
    for i in range(len(plaintext)):
        if plaintext[i].lower() not in alphabet or plaintext[i] == ' ':
            ciphertext += plaintext[i]
            continue
        if plaintext[i].islower():
            ciphertext += chr(((ord(plaintext[i]) + (ord(keyword[i % len(keyword)]) - 97) % 26) - 97) % 26 + 97)
        else:
            ciphertext += chr(((ord(plaintext[i]) + (ord(keyword[i % len(keyword)]) - 65) % 26) - 65) % 26 + 65)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    alphabet = string.ascii_lowercase
    for i in range(len(ciphertext)):
        if ciphertext[i].lower() not in alphabet or ciphertext[i] == ' ':
            plaintext += ciphertext[i]
            continue
        if keyword[i % len(keyword)].islower():
            exp = (ord(keyword[i % len(keyword)]) - 97)
        else:
            exp = (ord(keyword[i % len(keyword)]) - 65)
        if ciphertext[i % len(keyword)].islower():
            plaintext += chr(((ord(ciphertext[i]) - exp % 26) - 97) % 26 + 97)
        else:
            plaintext += chr(((ord(ciphertext[i]) - exp % 26) - 65) % 26 + 65)
    return plaintext
