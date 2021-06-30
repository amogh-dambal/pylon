import unittest

from src.main import test_stub
from src.misc import get_roster

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
	'sportradar_id',
	'yahoo_id',
	'rotowire_id',
	'update_dt',
	'headshot_url'
]


class RosterTester(unittest.TestCase):
	def test_one_year(self):
		df = get_roster([1999])
		self.assertEqual(df.columns, EXPECTED_COLUMNS)
		self.assertEqual(df.shape[0])


if __name__ == '__main__':
	unittest.main()
