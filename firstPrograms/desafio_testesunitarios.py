from unittest2 import TestCase, main

def palindrome(palavra):
    return True if palavra == palavra[::-1] else False
    # try:
    #     aux = ' '
    #     for x in palavra:
    #         aux = x + aux
    # except Exception:
    #      return None

class Teste(TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome('ovo'), True)
        self.assertEqual(palindrome('arara'), True)
        self.assertEqual(palindrome('python'), False)
        self.assertEqual(palindrome('osso'), True)
        
if __name__ == '__main__':
    main()
