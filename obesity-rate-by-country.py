import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

plt.style.use('lineplot-style.mplstyle')

# obesity rate working directory
python_work_dir = Path.home() / 'Programming/Python/'
work_dir = python_work_dir / 'data-visualization/obesity-rate-by-country/'

# obesity rate data
data_dir = Path.home() / 'Programming/data/obesity-rate-by-country/'
data_file = data_dir / 'BEFA58B_ALL_LATEST.csv'

# life expectancy dataframe
df = pd.read_csv(data_file)

print(df.head())

# # life expectancy pivot table dataframe
# le_yr_df = le_df.pivot(index='year', columns='location_name', values='val')
# le_yr_df.rename(columns={'United States of America': 'United States',
#                          'Republic of Korea': 'South Korea'}, inplace=True)
#
# # there are too many countries to plot, I've select just a few to show
# unselected_countries = ['Australia', 'Belgium', 'Canada',
#                         'Luxembourg', 'Netherlands', 'New Zealand',
#                         'Switzerland', 'Austria', 'Denmark',
#                         'Portugal', 'Finland', 'Sweden', 'Spain',]
# selected_countries = ['United Kingdom', 'Germany', 'Greece',
#                       'Ireland', 'Italy', 'Japan', 'South Korea',
#                       'Norway', 'Singapore', 'United States', 'France',]
#
# select_countries_df = le_yr_df[selected_countries]
#
# # life expectancy plot from 1990 to 2019
# fig, ax = plt.subplots()
# ax.plot(select_countries_df.index, select_countries_df,
#         label=select_countries_df.columns)
#
# ax.set_xlabel('Years')
# ax.set_ylabel('Life expectancy (years)')
# ax.set_title('Life expectancy from 1990 to 2019')
#
# for label in selected_countries:
#     ax.annotate(label, (2019.1, select_countries_df.loc[2019, label]))
#
# # Set source text
# ax.text(x=0.08, y=-0.02,
#         s='''Source: "2019 IHME Global Burden of Disease Study Results"''',
#         transform=fig.transFigure,
#         ha='left', fontsize=11, alpha=0.7)
#
# ax.legend(loc='center right', fontsize=11,
#           bbox_to_anchor=(0.195, 0.85), fancybox=True)
# plt.savefig(work_dir / 'plots/life_expectancy-1990-2019.png')
