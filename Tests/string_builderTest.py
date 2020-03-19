import unittest
from Tasks.string_builder import StringBuilder


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.sb = StringBuilder('')
        cls.sb.clear()

    def test_append(self):
        self.sb.append('a')
        self.sb.append('1')
        self.sb.append('BLABLA')
        self.assertEqual(str(self.sb), 'a1BLABLA')

    def test_insert(self):
        self.sb.clear()
        self.sb.insert('0', 0)
        self.sb.insert('1', 1)
        self.sb.insert('-1', -1)
        with self.assertRaises(IndexError):
            self.sb.insert('BLAA', 10)
        self.assertEqual(str(self.sb), '0-11')

    def test_setitem(self):
        self.sb.clear()
        self.sb[0] = 'H'
        self.sb[1] = 'i'
        self.assertEqual(str(self.sb), 'Hi')

    def test_getitem(self):
        self.sb.clear()
        self.sb.append('ABCDEFG')
        self.assertEqual(self.sb[0], 'A')
        self.assertEqual(self.sb[:2], 'AB')

    def test_iadd(self):
        self.sb.clear()
        self.sb.append('ABC')
        sb1 = StringBuilder('DEF')
        self.sb += sb1
        self.assertEqual(str(self.sb), 'ABCDEF')
        self.sb += 'GH'
        self.assertEqual(str(self.sb),  'ABCDEFGH')


if __name__ == '__main__':
    unittest.main()
