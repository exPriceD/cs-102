import string


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alphabet = string.ascii_lowercase
    for letter in plaintext:
        if letter.lower() not in alphabet or letter == ' ':
            ciphertext += letter
            continue
        if letter.islower():
            ciphertext += chr((ord(letter) + shift - 97) % 26 + 97)
        else:
            ciphertext += chr((ord(letter) + shift - 65) % 26 + 65)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alphabet = string.ascii_lowercase
    for letter in ciphertext:
        if letter.lower() not in alphabet or letter == ' ':
            plaintext += letter
            continue
        if letter.islower():
            plaintext += chr((ord(letter) - shift - 97) % 26 + 97)
        else:
            plaintext += chr((ord(letter) - shift - 65) % 26 + 65)
    return plaintext

# python -m doctest -v src/lab2/caesar.py
