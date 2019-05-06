from unittest import TestCase, main
from main import encrypt, decrypt


class TestCifraCesar(TestCase):
    def test_encrypt_abc_should_return_def(self):
        test_input = 'abc'
        expected = 'def'
        self.assertEqual(encrypt(test_input), expected)

    def test_decrypt_def_should_return_abc(self):
        test_input = 'def'
        expected = 'abc'
        self.assertEqual(decrypt(test_input), expected)

    def test_encrypt_xyz_should_return_abc(self):
        test_input = 'xyz'
        expected = 'abc'
        self.assertEqual(encrypt(test_input), expected)

    def test_decrypt_abc_should_return_xyz(self):
        test_input = 'abc'
        expected = 'xyz'
        self.assertEqual(decrypt(test_input), expected)


if __name__ == '__main__':
    main()
