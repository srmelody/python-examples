import unittest

from Palindrome import Palindrome
from Palindrome import PalindromeWrapper


class PalindromeTest(unittest.TestCase):
    def test_is_plaindrome(self):
        p = Palindrome()

        # The classic!
        self.assertTrue(p.isA("A man a plan a canal, Panama!"))

        # Boundary cases
        self.assertTrue(p.isA("A"))
        self.assertTrue(p.isA("Abba"))
        self.assertTrue(p.isA("Asa"))

        # Negative cases
        self.assertFalse(p.isA("Bobby"))
        self.assertFalse(p.isA("Panama City"))
        self.assertFalse(p.isA("ABC"))

        self.assertFalse(p.isA("ABCDECBA"))

        self.assertTrue( p.isA("nuf era semordnila Palindromes are fun"))

    def test_low_memory(self):
        tester = Palindrome()
        p = PalindromeWrapper("ABCDE", True)

        self.assertTrue(tester.isA(str(p)))

        self.assertEquals(str(p), "ABCDEEDCBA")

        buf = ""
        for ch in p:
            buf += ch
        self.assertEquals(str(p), buf)

        p = PalindromeWrapper("ABC", False)

        self.assertEquals("ABCBA", str(p))

        buf = ""
        for ch in p:
            buf += ch
        self.assertEquals(str(p), buf)


        self.assertTrue(tester.isA(str(p)))


