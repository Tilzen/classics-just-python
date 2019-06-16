from unittest import TestCase, main
from morse import encrypt, decrypt


class TestMorse(TestCase):
    def test_encrypt(self):
        test_word = 'test word'
        expected = '- . ... - / .-- --- .-. -.. '
        self.assertEqual(encrypt(test_word), expected)

    def test_decrypt(self):
        test_word = '- . ... - / .-- --- .-. -.. '
        expected = 'test word'
        self.assertEqual(decrypt(test_word), expected)


if __name__ == '__main__':
    main()
