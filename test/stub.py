import unittest

from src.main import test_stub

class MyTestCase(unittest.TestCase):
	def test_tstub(self):
		self.assertEqual("NFL", test_stub())


if __name__ == '__main__':
	unittest.main()
