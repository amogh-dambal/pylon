import unittest
import numpy as np

from src.pylon.main import test_stub
from src.pylon.misc import get_roster

EXPECTED_COLUMNS = [
	'season',
	'team',
	'position',
	'depth_chart_position',
	'jersey_number',
	'status',
	'full_name',
	'first_name',
	'last_name',
	'birth_date',
	'height',
	'weight',
	'college',
	'high_school',
	'gsis_id',
	'espn_id',
	'yahoo_id',
	'rotowire_id',
	'pff_id',
	'headshot_url',
	'fantasy_data_id',
	'sleeper_id',
	'years_exp',
	'sportradar_id'
]


class RosterTester(unittest.TestCase):
	def test_one_year(self):
		df = get_roster([1999])
		self.assertTrue(np.all(df.columns == EXPECTED_COLUMNS))
		self.assertEqual(df.shape[0], 1980)
		self.assertEqual(df.shape[1], 24)

	def test_multiple_years(self):
		df = get_roster([1999, 2001])
		self.assertTrue(np.all(df.columns == EXPECTED_COLUMNS))
		self.assertEqual(df.shape[1], 24)


if __name__ == '__main__':
	unittest.main()
