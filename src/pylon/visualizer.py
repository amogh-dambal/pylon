# python 3.6
# basic data viz
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# credits to Deryck97's python guide
TEAM_COLORS = {
	'ARI': '#97233F', 'ATL': '#A71930', 'BAL': '#241773', 'BUF': '#00338D', 'CAR': '#0085CA',
	'CHI': '#00143F', 'CIN': '#FB4F14', 'CLE': '#FB4F14', 'DAL': '#B0B7BC', 'DEN': '#002244',
	'DET': '#046EB4', 'GB': '#24423C', 'HOU': '#C9243F', 'IND': '#003D79', 'JAX': '#136677',
	'KC': '#CA2430', 'LA': '#002147', 'LAC': '#2072BA', 'LV': '#C4C9CC', 'MIA': '#0091A0',
	'MIN': '#4F2E84', 'NE': '#0A2342', 'NO': '#A08A58', 'NYG': '#192E6C', 'NYJ': '#203731',
	'PHI': '#014A53', 'PIT': '#FFC20E', 'SEA': '#7AC142', 'SF': '#C9243F', 'TB': '#D40909',
	'TEN': '#4095D1', 'WAS': '#FFC20F'
}


def build_histogram(vars: list, **kwargs) -> (plt.Figure, plt.Axes):
	"""
	function to build a histogram for the distribution of a set of variable
	:param vars: variable whose distribution we're plotting
	:param kwargs: parameters to pass to build the graph.
	:return:
	"""


# basic way to build scatterplot
def build_scatterplot(x: pd.Series, y: pd.Series, **kwargs) -> (plt.Figure, plt.Axes):
	"""
	function to build a scatterplot for x and y.
	code entirely adapted from Deryck97's amazing tutorial on nflfastR
	for python
	:param x:
	:param y:
	:param kwargs:
	:return:
	"""
	# validate input series
	if x.size <= 0 or y.size <= 0:
		raise ValueError("Invalid arguments passed to function (build-scatterplot): size of input series is 0.")

	opts = {
		'figsize': (15, 15) if 'figsize' not in kwargs else kwargs['figsize'],
		'best_fit': True if 'best_fit' not in kwargs else kwargs['best_fit'],
		'gridlines': True if 'gridlines' not in kwargs else kwargs['gridlines'],
		'x_label': 'X' if 'x_label' not in kwargs else str(kwargs['x_label']),
		'y_label': 'y' if 'y_label' not in kwargs else str(kwargs['y_label']),
		'title': 'Title' if 'title' not in kwargs else str(kwargs['title']),
		'save_as': None if 'save_as' not in kwargs else str(kwargs['save_as'])
	}

	fig, ax = plt.subplots(figsize=opts['figsize'])

	ax.scatter(x, y, s=0.001, color='navy')
	if opts['best_fit']:
		ax.plot(
			np.unique(x),
			np.poly1d(np.polyfit(x, y, 1)) * np.unique(x)
		)

	if opts['gridlines']:
		ax.grid(zorder=0, alpha=0.4)
		ax.set_axisbelow(True)

	ax.set_xlabel(str(opts['x_label']), fontsize=12)
	ax.set_ylabel(str(opts['y_label']), fontsize=12)
	ax.set_title(str(opts['title']), fontsize=15)

	plt.figtext(x=0.79, y=0.05, s='Data: nflfastR.', fontsize=10)

	if opts['save_as'] is not None:
		plt.savefig(opts['save_as'], dpi=400)

	return fig, ax


def build_logoplot(x: pd.Series, y: pd.Series, **kwargs) -> (plt.Figure, plt.Axes):
	"""
	Function that builds a scatterplot using team logos instead of the
	:param x: x-axis data
	:param y: y-axis data
	:param kwargs:
	:return: pyplot.Figure and pylo
	"""
	# validate input series
	if x.size <= 0 or y.size <= 0:
		raise ValueError("Invalid arguments passed to function (build-scatterplot): size of input series is 0.")

	opts = {
		'figsize': (15, 15) if 'figsize' not in kwargs else kwargs['figsize'],
		'best_fit': True if 'best_fit' not in kwargs else kwargs['best_fit'],
		'gridlines': True if 'gridlines' not in kwargs else kwargs['gridlines'],
		'x_label': 'X' if 'x_label' not in kwargs else str(kwargs['x_label']),
		'y_label': 'y' if 'y_label' not in kwargs else str(kwargs['y_label']),
		'title': 'Title' if 'title' not in kwargs else str(kwargs['title']),
		'save_as': None if 'save_as' not in kwargs else str(kwargs['save_as'])
	}
	return fig, ax


def build_hbar(x: pd.Series, y: pd.Series, **kwargs) -> None:
	"""

	:param x:
	:param y:
	:return:
	"""
	# validate input series
	if x.size <= 0 or y.size <= 0:
		raise ValueError("Invalid arguments passed to function (build-scatterplot): size of input series is 0.")

	opts = {
		'figsize': (15, 15) if 'figsize' not in kwargs else kwargs['figsize'],
		'x_label': 'X' if 'x_label' not in kwargs else str(kwargs['x_label']),
		'y_label': 'y' if 'y_label' not in kwargs else str(kwargs['y_label']),
		'title': 'Title' if 'title' not in kwargs else str(kwargs['title']),
		'save_as': None if 'save_as' not in kwargs else str(kwargs['save_as'])
	}

	raise NotImplementedError("This function is not supported by this version of pylon. ")


def build_vbar(x: pd.Series, y: pd.Series) -> None:
	raise NotImplementedError("This function is not supported by this version of pylon. ")
