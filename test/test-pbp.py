import unittest

from src.pbp import functions


class TestPBP(unittest.TestCase):
	def test_load(self):
		pbp = functions.load_pbp([2019])
		self.assertEqual(True)

	def test_load(self):
		pbp = functions.load_pbp([2019, 2018, 2017])
		self.assertEqual(True, True)


if __name__ == '__main__':
	unittest.main()
