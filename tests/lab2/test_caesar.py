import unittest

from src.lab2.caesar import encrypt_caesar, decrypt_caesar


class CaesarTestCase(unittest.TestCase):
    def test_encrypt_caesar(self):
        result = encrypt_caesar("pythoooon")
        self.assertEquals(result, "sbwkrrrrq")
        print("Test 'encrypt_caesar' completed")

    def test_encrypt_caesar_with_number(self):
        result = encrypt_caesar("python 3.11")
        self.assertEquals(result, "sbwkrq 3.11")
        print("Test 'encrypt_caesar_with_number' completed")

    def test_encrypt_caesar_zero_letters(self):
        result = encrypt_caesar("")
        self.assertEquals(result, "")
        print("Test 'encrypt_caesar_zero_letters' completed")

    def test_encrypt_caesar_different_registers(self):
        result = encrypt_caesar("pRoGRAmMing")
        self.assertEquals(result, "sUrJUDpPlqj")
        print("Test 'encrypt_caesar_different_registers' completed")

    def test_decrypt_caesar(self):
        result = decrypt_caesar("frpsxwhu vflhqfh")
        self.assertEquals(result, "computer science")
        print("Test 'decrypt_caesar' completed")

    def test_decrypt_caesar_with_number(self):
        result = decrypt_caesar("frpsxwhu vflhqfh 2023!")
        self.assertEquals(result, "computer science 2023!")
        print("Test 'decrypt_caesar' completed")

    def test_decrypt_caesar_zero_letters(self):
        result = decrypt_caesar("")
        self.assertEquals(result, "")
        print("Test 'decrypt_caesar_zero_letters' completed")

    def test_decrypt_caesar_different_registers(self):
        result = decrypt_caesar("sUrJUDpPlqj")
        self.assertEquals(result, "pRoGRAmMing")
        print("Test 'decrypt_caesar_different_registers' completed")


if __name__ == "__name__":
    unittest.main()
