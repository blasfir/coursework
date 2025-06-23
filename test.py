import unittest
from SEED import EncryptBlock, GenerateRoundKeys


class TestSEEDEncrypt(unittest.TestCase):
    def test_encrypt_vectors(self):
        test_cases = [
            (
                0x00102030405060708090a0b0c0d0e0f,
                0x00000000000000000000000000000000,
                0x5ebac6e0054e166819aff1cc6d346cdb
            ),
            (
                0x00000000000000000000000000000000,
                0x00102030405060708090a0b0c0d0e0f,
                0xc11f22f20140505084483597e4370f43
            ),
            (
                0x123456789abcdef0123456789abcdef,
                0x123456789abcdef0123456789abcdef,
                0x504ec8814d4f85eb81ec4bd210111425
            ),
            (
                0x00102030405060708090a0b0c0d0e0f,
                0x00102030405060708090a0b0c0d0e0f,
                0xa6e8d7325bbe0998cf235c1b57e64360
            ),
            (
                0x123456789abcdeffedcba9876543210,
                0x123456789abcdeffedcba9876543210,
                0xcaf1d16d6ec079a21ea4066794222c2a
            ),
        ]

        for plaintext, key, expected in test_cases:
            round_keys = GenerateRoundKeys(key)
            ciphertext = EncryptBlock(plaintext, round_keys)
            self.assertEqual(
                ciphertext, expected, f"Failed for plaintext={hex(plaintext)}, key={hex(key)}")


if __name__ == '__main__':
    unittest.main()
