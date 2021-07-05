# python 3.6
# wrappers around nflfastR functions
# that return pandas DataFrames
import pandas as pd
from ..util.urls import PBP_URL


def build_nflfastr_pbp(game_ids: list, decode: bool = True, rules: bool = True) -> pd.DataFrame:
	pass


def load_pbp(seasons: list, serialize: bool = True, only_regular_season: bool = False) -> pd.DataFrame:
	pbp_dfs = [
		pd.read_csv(PBP_URL.format(season=season), error_bad_lines=False)
		for season in seasons
		if 1999 <= int(season) <= 2020
	]

	df = pd.concat(pbp_dfs).reset_index(drop=True, inplace=True)

	if only_regular_season:
		df = df.loc[df.season_type == 'REG']
	return df


