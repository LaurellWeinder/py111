import unittest
from Tasks.f0_binary_search_tree import *


class MyTestCase(unittest.TestCase):
	@classmethod
	def setUp(cls):
		cls.bst = BinarySearchTree()

	def test_inserts(self):
		try:
			self.bst.insert(42, 'The meaning of life, the universe and everything.')
			self.bst.insert(0, 'ZERO!')
			self.bst.insert(13, "Devil's sign here")
			self.bst.insert(13, "Oh no, devil's sign again Oo")
		except Exception as e:
			print(e)
			self.fail("Something wrong with inserts. Do you handle insert of value with similar keys?..")

	def test_removes(self):
		try:
			self.bst.insert(42, "The meaning again")
			self.bst.remove(42, self.bst.root)
			self.bst.remove(42, self.bst.root)
			self.bst.remove(43, self.bst.root)
		except Exception as e:
			print(e)
			self.fail(
				"Do not forget about deleting non-existing keys. "
				"I think that deleting of non-existing keys should be silent, unlike search.")

	def test_find(self):
		self.bst.insert(42, "Predictable")
		self.bst.insert(13, "And again")
		self.bst.insert(-999, "Nobody expects spanish inquisition!")
		self.assertEqual(
			"And again",
			self.bst.find(13),
			msg="Something gonna wrong..."
		)

	def test_not_find(self):
		self.bst.insert(0, "Never")
		self.bst.insert(1, "gonna")
		self.bst.insert(2, "give")
		self.bst.insert(11, "you")
		self.bst.insert(-3, "up")
		with self.assertRaises(KeyError, msg="Search of non-existing key should be erroneous."):
			self.bst.find(100)


if __name__ == '__main__':
	unittest.main()
