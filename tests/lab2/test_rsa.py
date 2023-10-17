import unittest
import random
from src.lab2.rsa import is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt


class RSATestCase(unittest.TestCase):
    def test_is_prime_true(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
        for prime in primes:
            self.assertTrue(is_prime(prime))
        print("Test 'is_prime_true' completed")

    def test_is_prime_false(self):
        not_primes = [4, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36, 40, 45, 54, 60, 64, 81, 90, 100, 120]
        for not_prime in not_primes:
            self.assertFalse(is_prime(not_prime))
        print("Test 'is_prime_false' completed")

    def test_gcd(self):
        self.assertEqual(gcd(21, 7), 7)
        self.assertEqual(gcd(15, 45), 15)
        self.assertEqual(gcd(-25, -50), -25)
        print("Test 'gcd' completed")

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(2, 5), 3)
        self.assertEqual(multiplicative_inverse(3, 7), 5)
        print("Test 'multiplicative_inverse' completed")

    def test_generate_keypair_errors(self):
        with self.assertRaises(ValueError) as exc:
            generate_keypair(20, 54)
            self.assertEqual(str(exc.exception), "Both numbers must be prime.")

        with self.assertRaises(ValueError) as exc:
            generate_keypair(11, 11)
            self.assertEqual(str(exc.exception), "p and q cannot be equal")

        self.assertEqual(type(()), type(generate_keypair(17, 19)))  # type
        self.assertEqual(2, len(generate_keypair(41, 59)))  # length
        generated_keypair = generate_keypair(127, 151)
        self.assertTrue(all(isinstance(key, int) for keys in generated_keypair for key in keys))  # type elem. in tuple
        print("Test 'generate_keypair_errors' completed")

    def test_encrypt_and_decrypt(self):
        message_list = ["Hello", "python 3.10", "programming", "RSA", "PRIME", "1234", "qwerty"]
        for message in message_list:
            p = random.choice([17, 19, 23, 37, 41, 59, 73, 157])
            q = random.choice([13, 29, 89, 97, 101, 127, 151, 181])
            public, private = generate_keypair(p, q)

            encrypted_msg = encrypt(private, message)
            self.assertTrue(isinstance(encrypted_msg, list))
            self.assertTrue(all(isinstance(element, int) for element in encrypted_msg))

            decrypted_msg = decrypt(public, encrypted_msg)
            self.assertTrue(isinstance(decrypted_msg, str))
            self.assertEqual(decrypted_msg, message)
        print("Test 'encrypt_and_decrypt' completed")


if __name__ == "__name__":
    unittest.main()
