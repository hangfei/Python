
#Hangfei Lin, and Fei Shao's Assignment3

import playfair
import unittest

class TestPlayfair(unittest.TestCase):

    def testEncode(self):
        message1 = 'Programming in Python is fun!!'
        message2 = 'Amazingly few discotheques provide jukeboxes.'

        secretPhrase = 'Barack H. Obama'
        self.assertEquals('Gbt`cr\x00\t\x00ht_aookJ~hipoaooO[}p\x0b"\t',
            playfair.encode(message1,secretPhrase))
        self.assertEquals(':" vjo^tzkgfzr\\plOphq[h|fqHo javefroyBg.lzfqa"',
            playfair.encode(message2,secretPhrase))

        secretPhrase = "George Herbert Walker Bush"
        self.assertEquals("MHr GB|&njftszitN{H\ttcsz$sy#c'&k",
            playfair.encode(message1, secretPhrase))
        self.assertEquals('Efsqjpeuzg`gzofjkirWlHya lWigrz``rHisBotrw l0s',
            playfair.encode(message2, secretPhrase))

    def testDecode(self):
        message1 = 'Programming in Python is fun!!'
        message2 = 'Amazingly few discotheques provide jukeboxes.'

        secretPhrase = 'Barack H. Obama'
        self.assertEquals(message1,
          playfair.decode('Gbt`cr\x00\t\x00ht_aookJ~hipoaooO[}p\x0b"\t',
                                secretPhrase))
        self.assertEquals(message2,
          playfair.decode(':" vjo^tzkgfzr\\plOphq[h|fqHo javefroyBg.lzfqa"',
                                secretPhrase))

        secretPhrase = "George Herbert Walker Bush"
        self.assertEquals(message1,
          playfair.decode("MHr GB|&njftszitN{H\ttcsz$sy#c'&k",
                                secretPhrase))
        self.assertEquals(message2,
          playfair.decode('Efsqjpeuzg`gzofjkirWlHya lWigrz``rHisBotrw l0s',
                                secretPhrase))

    def testFillout(self):
        message1 = [[ 'B', 'a', 'r', 'c', 'k', ' ', 'H', '.', 'O', 'b'],
            ['m', '\x00', '\t',chr(10),chr(11),chr(13), '!', '"', '#', '$'],
            [ '%', '&', "'", '(', ')', '*', '+', ',', '-', '/'],
            [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            [ ':', ';', '<', '=', '>', '?', '@', 'A', 'C', 'D'],
            [ 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'P'],
            [ 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
            [ '[', '\\', ']', '^', '_', '`', 'd', 'e', 'f', 'g'],
            [ 'h', 'i', 'j', 'l', 'n', 'o', 'p', 'q', 's', 't'],
            [ 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']]
        secretPhrase1 = playfair.Keyword("Barack H. Obama")

        self.assertEquals(message1, playfair.Fillout(secretPhrase1))

    def testKeyword(self):
        message1 = "Barck H.Obm"
        message2 = "Georg HbtWalkBush"

        secretPhrase1 = "Barack H. Obama"
        self.assertEquals(message1,
                         playfair.Keyword(secretPhrase1))
        secretPhrase2 = "George Herbert Walker Bush"
        self.assertEquals(message2,
                         playfair.Keyword(secretPhrase2))

    def testTextforward(self):
        message1 = ['P', 'r', 'o', 'g', 'r', 'a', 'm', '\x00',
                   'm', 'i', 'n', 'g', ' ', 'i', 'n', ' ', 'P',
                   'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ',
                   'f', 'u', 'n', '!', '!', '\x00']
        message2 = ['J', 'a', 'm', 'e', 's', ' ', 'b', 'o', 'n',
                   'd', ' ', 'i', 's', ' ', 'h', 'o', 't', '!']

        PlainTextmessage1 = "Programming in Python is fun!!"
        self.assertEquals(message1,
                         playfair.Textforward(PlainTextmessage1))
        PlainTextmessage2 = "James bond is hot!"
        self.assertEquals(message2,
                         playfair.Textforward(PlainTextmessage2))

       
        
                          

unittest.main()
