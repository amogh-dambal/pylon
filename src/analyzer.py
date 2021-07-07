# python 3.6
# basic data analysis functions
import pandas as pd


def filter(pbp: pd.DataFrame, **kwargs: dict) -> pd.DataFrame:
	"""
	function to filter a dataframe around certain commonly used parameters
	for analysis.
	:param pbp: play-by-play dataset
	:param kwargs: keyword args representing the parameters currently supported by filtering
	- down: either 1, 2, 3, or 4
	- play_type: pass, rush, or no_play
	:return: filtered pandas DataFrame object
	"""
	pass


def find_game(pbp: pd.DataFrame, **kwargs: dict) -> pd.DataFrame:
	"""
	function wrapper around finding a specific game in a season-wide play-by-play
	dataset
	:param pbp: season worth of play-by-play data
	:param kwargs: the keys used to query for a particular game. can either be
	- home_team: HOME team abbreviation
	- away_team: AWAY team abbreviation
	OR
	- game_id: NFL gamecenter ID
	but NOT both
	:return: filtered dataframe with play-by-play data for the queried game
	"""
	df = pbp.copy(deep=True)

	if {"game_id", "home_team", "away_team"} is set(kwargs.keys()):
		raise ValueError("Cannot specify both game_id AND home, away team")

	if "home_team" in kwargs and "away_team" in kwargs:
		home = kwargs["home_team"]
		away = kwargs["away_team"]
		df = df.loc[(df.home_team == home) & (df.away_team == away)]
	else:
		game_id = kwargs["game_id"]
		df = df.loc[df.game_id == game_id]
	return df


