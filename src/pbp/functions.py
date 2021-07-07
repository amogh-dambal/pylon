# python 3.6
# wrappers around nflfastR functions
# that return pandas DataFrames
import pandas as pd
from ..util.urls import PBP_URL


def build_nflfastr_pbp(game_ids: list, decode: bool = True, rules: bool = True) -> pd.DataFrame:
	pass


def load_pbp(
		seasons: list, only_regular_season: bool = False, remove_plays=True
) -> pd.DataFrame:
	pbp_dfs = [
		pd.read_csv(PBP_URL.format(season=season), error_bad_lines=False)
		for season in seasons
		if 1999 <= int(season) <= 2020
	]

	df = pd.concat(pbp_dfs).reset_index(drop=True).copy(deep=True)

	# cleaning code adapted directly from Deryck97's nflfastR python guide.
	# https://gist.github.com/Deryck97/dff8d33e9f841568201a2a0d5519ac5e
	if only_regular_season:
		df = df.loc[df.season_type == 'REG']

	# we want to remove plays like kickoffs, field goals, kneel downs, etc.
	# since they usually don't have any effect on the analysis
	if remove_plays:
		df = df.loc[
			(df.play_type.isin(['no_play', 'pass', 'run']) & (not df.epa.isna()))
		]

	# change play type to match play call. for example,
	# sometimes QB scrambles get mistakenly labled as run
	# plays but we want to analyze them as pass plays
	df.play_type.loc[df['pass'] == 1] = 'pass'
	df.play_type.loc[df.rush == 1] = 'run'

	# just for good measure
	df.reset_index(drop=True)

	return df
