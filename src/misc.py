# python 3.6
# file for the nflfastR functions I couldn't find a place for
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

from src.util.urls import ROSTER_URL, SCHEDULE_URL, STATS_URL


# TODO: might need to look into the Sleeper API to get roster data. For now,
# 		we just use the repo that has the data already stored
def get_roster(seasons: list) -> pd.DataFrame:
	"""
	Obtain rosters for all NFL teams across the given seasons
	:param seasons: list of integers representing seasons where each season[i] in the range [1999, 2020]
	:return: pandas DataFrame object
	"""
	roster_dfs = [
		pd.read_csv(ROSTER_URL.format(season=season), error_bad_lines=False)
		for season in seasons
		if 1999 <= int(season) <= 2020
	]
	df = pd.concat(roster_dfs)
	return df


def get_schedules(seasons: list) -> pd.DataFrame:
	# https://stackoverflow.com/questions/64178038/how-to-read-a-rds-file-from-a-url-in-python

	# TODO: come back to this later when I can figure out RDS files RIP LMAO
	return None


def get_stats(serialize: bool = False) -> pd.DataFrame:
	"""
	function that obtains player statistics
	:param serialize: if this is True, use serialization for greater efficiency(not supported yet)
	:return: pandas DataFrame object with all NFL player stats as maintained by nflfastR.
	"""
	df = pd.read_csv(STATS_URL, compression='gzip', low_memory=False)
	return df
