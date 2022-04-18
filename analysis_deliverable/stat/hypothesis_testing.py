import pandas as pd
from analysis_deliverable.stat.stats_tests import chisquared_independence_test, two_sample_ttest
from analysis_deliverable.stat.stats_functions import weeks_on_chart_count, with_and_without_spotify, split_by_percentile
from analysis_deliverable.visualization.visualization import correlation_heatmap
import matplotlib.pyplot as plt
import numpy as np


SPOTIFY_ATTRIBUTES = ["danceability", "energy", "key", "loudness", "mode", "speechiness",\
    "acousticness", "instrumentalness", "liveness", "valence", "tempo", "type", "id", "uri",\
        "track_href", "analysis_url", "duration_ms", "time_signature"]

all_songs_dfs = {}
for decade in range(1970, 2030, 10):
    filename = "dataset/%ss_dataset"%str(decade)
    all_songs_dfs[decade] = pd.read_csv(filename)
    
print(all_songs_dfs[1970].dtypes)

with_spotify_dfs = {}
without_spotify_dfs = {}
for decade in range(1970, 2030, 10):
    with_spotify_dfs[decade], without_spotify_dfs[decade] = with_and_without_spotify(all_songs_dfs[decade])


### Hypothesis 1: chi-square testing fo all numerical attributes on list songs with spotify data (but targetting dancebility)
def h1():
    for decade in range(1970, 2030, 10):
        print("********************\nThis is %s decade:\n********************"%str(decade))
        for attribute in SPOTIFY_ATTRIBUTES:
            print("This is for " + attribute + ":")
            chisquared_independence_test(with_spotify_dfs[decade], "weeks_on_chart", attribute)
    

### Hypothesis 2: two sample t test to see if average valence is different for songs that are on charts longest
def h2():
    for decade in range(1970, 2030, 10):
        top_percentile, bottom_percentile = split_by_percentile(with_spotify_dfs[decade], 10)
        two_sample_ttest(top_percentile["valence"], bottom_percentile["valence"])


### Hypothesis 3: two sample t test to see if average energy score is different from 1970s to 2010s
def h3():
    two_sample_ttest(with_spotify_dfs[1970]["energy"], with_spotify_dfs[2010]["energy"])

# h1()
# h2()
# h3()
all_songs_df = with_spotify_dfs[1970]
all_songs_df["decade"] = "1970s"
print(all_songs_df)

for decade in range(1980, 2030, 10):
    with_decade_df = with_spotify_dfs[decade]
    with_decade_df["decade"] = "%ss"%decade
    all_songs_df = pd.concat([all_songs_df, with_decade_df])



correlation_heatmap(all_songs_df)

# print(weeks_on_chart_count(with_spotify_dfs[1970]))

# print(all_songs_df.mean(axis=0))

bar_info = pd.concat([
                with_spotify_dfs[1970].mean(axis=0).to_frame('1970s'),
                with_spotify_dfs[1980].mean(axis=0).to_frame('1980s'),
                with_spotify_dfs[1990].mean(axis=0).to_frame('1990s'),
                with_spotify_dfs[2000].mean(axis=0).to_frame('2000s'),
                with_spotify_dfs[2010].mean(axis=0).to_frame('2010s'),
                with_spotify_dfs[2020].mean(axis=0).to_frame('2020s')], axis=1)


print(bar_info)

for characteristic in bar_info.index:
    fig, ax=plt.subplots()
    current_row = bar_info.loc[characteristic]
    current_row.plot.bar(ax=ax, yerr=current_row.std(), capsize=6)
    ax.set_title(characteristic)
    ax.set_xlabel("decade")
    ax.set_ylabel("value")

plt.show()

