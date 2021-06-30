# python 3.6
# file for the nflfastR functions I couldn't find a place for
import pandas as pd
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

from src.util.urls import ROSTER_URL, SCHEDULE_URL


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

	for season in seasons:
		url_string = SCHEDULE_URL.format(season=season)

		base = importr("base")
		r_df <- base.readRDS(base.url(url_string))
		pandas2ri.activate()
		df = pandas2ri.ri2py(r_df)
	pass


def get_stats(serialize: bool = False) -> pd.DataFrame:
	pass
