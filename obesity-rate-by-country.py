import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

plt.style.use('lineplot-style.mplstyle')

# path to save plot
work_dir = Path.home() / 'Programming/Python/data-visualization/obesity-rate-by-country'

# obesity rate data
data_dir = Path.home() / 'Programming/data/obesity-rate-by-country/'
data_file = data_dir / 'BEFA58B_ALL_LATEST.csv'

# life expectancy dataframe
columns=['GEO_NAME_SHORT', 'DIM_TIME', 'DIM_SEX', 'RATE_PER_100_N', 'RATE_PER_100_NL', 'RATE_PER_100_NU']
ob_rt_df = pd.read_csv(data_file, usecols=columns)

ob_rt_df['GEO_NAME_SHORT'] = ob_rt_df['GEO_NAME_SHORT'].replace(to_replace={
    'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
    'Republic of Korea': 'South Korea',
    'United States of America': 'United States',
    'Netherlands (Kingdom of the)': 'Netherlands'})

ob_rt_df.rename(columns={'GEO_NAME_SHORT': 'Country', 'DIM_TIME': 'Year',
                         'RATE_PER_100_N': 'Obesity rate'}, inplace=True)

selected_countries = ['United Kingdom', 'Germany', 'Greece', 'Mexico',
                      'Finland', 'Italy', 'Japan', 'South Korea',
                      'Netherlands', 'Singapore', 'United States', 'France',]

slct_ctr_ob_rt_df = ob_rt_df[ob_rt_df['Country'].isin(selected_countries)]
slct_ctr_ob_rt_df = slct_ctr_ob_rt_df.pivot_table(index='Year', columns='Country',
                                                  values='Obesity rate', aggfunc='mean')

# obesity rate from 1990 to 2022
fig, ax = plt.subplots()
ax.plot(slct_ctr_ob_rt_df.index, slct_ctr_ob_rt_df,
        label=slct_ctr_ob_rt_df.columns)

ax.set_xlabel('Years')
ax.set_ylabel(r'Obesity rate (BMI $\geq$ 30)')
ax.set_title('Obesity rate from 1990 to 2022')

for label in selected_countries:
    ax.annotate(label, (2022.1, slct_ctr_ob_rt_df.loc[2022, label]))

# Set source text
ax.text(x=0.08, y=-0.02,
        s='''Source: "World health statistics 2024: monitoring health for the SDGs, sustainable development goals"''',
        transform=fig.transFigure,
        ha='left', fontsize=11, alpha=0.7)

ax.legend(loc='center right', fontsize=11,
          bbox_to_anchor=(0.195, 0.85), fancybox=True)
plt.savefig(work_dir / 'plots/obesity_rate_1990_2022.png')
