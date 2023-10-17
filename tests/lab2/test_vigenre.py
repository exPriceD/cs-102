import unittest

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


class VigenreTestCase(unittest.TestCase):
    def test_encrypt_vigenere(self):
        result = encrypt_vigenere("pythoooon", "a")
        self.assertEquals(result, "pythoooon")
        print("Test 'encrypt_vigenere' completed")

    def test_encrypt_vigenere_with_number(self):
        result = encrypt_vigenere("python 3.11", "python")
        self.assertEquals(result, "ewmoca 3.11")
        print("Test 'encrypt_vigenere_with_number' completed")

    def test_encrypt_vigenere_zero_letters(self):
        result = encrypt_vigenere("", "aeq")
        self.assertEquals(result, "")
        print("Test 'encrypt_vigenere_zero_letters' completed")

    def test_encrypt_vigenere_different_registers(self):
        result = encrypt_vigenere("pRoGRAmMing", "aDggpRT")
        self.assertEquals(result, "pUuMGRfMltm")
        print("Test 'encrypt_vigenere_different_registers' completed")

    def test_encrypt_vigenere_with_space(self):
        result = encrypt_vigenere("i am good boy", "good")
        self.assertEquals(result, "o oa jucr eum")
        print("Test 'encrypt_vigenere_with_space' completed")

    def test_decrypt_vigenere(self):
        result = decrypt_vigenere("vvtd", "shadowfiend")
        self.assertEquals(result, "dota")
        print("Test 'decrypt_vigenere' completed")

    def test_decrypt_vigenere_with_space(self):
        result = decrypt_vigenere("uoepkpah wuiwnsa", "sasaqwwqe")
        self.assertEquals(result, "computer science")
        print("Test 'decrypt_vigenere_with_space' completed")

    def test_decrypt_vigenere_different_registers(self):
        result = decrypt_vigenere("pUuMGRfMltm", "aDggpRT")
        self.assertEquals(result, "pRoGRAmMing")
        print("Test 'decrypt_vigenere_different_registers' completed")

    def test_decrypt_vigenere_zero_letters(self):
        result = decrypt_vigenere("", "")
        self.assertEquals(result, "")
        print("Test 'decrypt_vigenere_zero_letters' completed")

    def test_decrypt_caesar_with_numbers(self):
        result = decrypt_vigenere("yhsmxnoplfg3.12", "qwerty")
        self.assertEquals(result, "ilovepython3.12")
        print("Test 'decrypt_caesar_with_numbers' completed")


if __name__ == "__name__":
    unittest.main()
