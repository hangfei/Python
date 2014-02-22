import kwic
import unittest

class TestKwic(unittest.TestCase):
    def testChomp(self):
        message1 = "This is a test"
        message2 = "This is another test/n"

        expected1 = "This is a test"
        expected2 = "This is another test"

        self.assertEquals(kwic.chomp(message1), expected1)
        self.assertEquals(kwic.chomp(message2), expected2)

unittest.main()
