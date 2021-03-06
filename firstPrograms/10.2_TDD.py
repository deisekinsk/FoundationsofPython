from unittest2 import TestCase, main

def eh_impar(num):
    try:
        #Implementa lógica
        if int(num) % 2 != 0:
            return True
        else:
            return False
    except Exception:
            return None

class Impar(TestCase):
    def test_impar(self):
        self.assertEqual(eh_impar(3), True)
        self.assertEqual(eh_impar(65673), True)
        self.assertEqual(eh_impar(3874), False)
        self.assertEqual(eh_impar('212121'), True)
        self.assertEqual(eh_impar('21212'), False)
        self.assertEqual(eh_impar('sfssfsd'), None)

if __name__ == '__main__':
    main()