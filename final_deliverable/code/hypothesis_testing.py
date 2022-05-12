import pandas as pd
from stats_tests import chisquared_independence_test, two_sample_ttest
from stats_functions import weeks_on_chart_count, with_and_without_spotify, split_by_percentile
from visualization import correlation_heatmap
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem


SPOTIFY_ATTRIBUTES = ["danceability", "energy", "key", "loudness", "mode", "speechiness",\
    "acousticness", "instrumentalness", "liveness", "valence", "tempo", "type", "id", "uri",\
        "track_href", "analysis_url", "duration_ms", "time_signature"]

all_songs_dfs = {}
for decade in range(1970, 2030, 10):
    filename = "/Users/rickychau/Documents/CS1951A/Homework/FinalProject/Team-Name/analysis_deliverable/dataset/song-features/%ss_features"%str(decade)
    all_songs_dfs[decade] = pd.read_csv(filename)
    all_songs_dfs[decade] = all_songs_dfs[decade][all_songs_dfs[decade]['weeks_on_chart']!=20] 
    

with_spotify_dfs = {}
without_spotify_dfs = {}
for decade in range(1970, 2030, 10):
    with_spotify_dfs[decade], without_spotify_dfs[decade] = with_and_without_spotify(all_songs_dfs[decade])


# concatenating all songs into one df
all_songs_df = with_spotify_dfs[1970]
for decade in range(1980, 2030, 10):
    with_decade_df = with_spotify_dfs[decade]
    # with_decade_df["decade"] = f"{decade}s"
    all_songs_df = pd.concat([all_songs_df, with_decade_df])


### Hypothesis 1: chi-square testing fo all numerical attributes on list songs with spotify data (but targetting dancebility)
def h1():
    for attribute in SPOTIFY_ATTRIBUTES:
        print("This is for " + attribute + ":")
        chisquared_independence_test(all_songs_df, "weeks_on_chart", attribute)
    

### Hypothesis 2: two sample t test to see if average valence is different for songs that are on charts longest
def h2():
    for decade in range(1970, 2030, 10):
        top_percentile, bottom_percentile = split_by_percentile(with_spotify_dfs[decade], 10)
        two_sample_ttest(top_percentile["valence"], bottom_percentile["valence"])
    top_percentile, bottom_percentile = split_by_percentile(all_songs_df, 10)
    two_sample_ttest(top_percentile["valence"], bottom_percentile["valence"])

### Hypothesis 3: two sample t test to see if average energy score is different from 1970s to 2010s
def h3():
    two_sample_ttest(with_spotify_dfs[1970]["energy"], with_spotify_dfs[2010]["energy"])

# h1()
# h2()
# h3()


# creating visualizations
def heatmap():
    correlation_heatmap(all_songs_df)
    plt.tight_layout()
    plt.show()

# heatmap()

def barcharts():
    bar_info = pd.concat([
                    with_spotify_dfs[1970].mean(axis=0).to_frame('1970s'),
                    with_spotify_dfs[1980].mean(axis=0).to_frame('1980s'),
                    with_spotify_dfs[1990].mean(axis=0).to_frame('1990s'),
                    with_spotify_dfs[2000].mean(axis=0).to_frame('2000s'),
                    with_spotify_dfs[2010].mean(axis=0).to_frame('2010s'),
                    with_spotify_dfs[2020].mean(axis=0).to_frame('2020s')], axis=1)

    se_by_characteristic = {}
    for characteristic in bar_info.index:
        list_of_se = []
        for decade in range(1970, 2030, 10):
            series = with_spotify_dfs[decade][characteristic].to_numpy()
            se = sem(series)
            list_of_se = list_of_se + [se]
        se_by_characteristic[characteristic] = list_of_se   
      
    for characteristic in bar_info.index:
        fig, ax=plt.subplots()
        current_row = bar_info.loc[characteristic]
        current_row.plot.bar(ax=ax, yerr=se_by_characteristic[characteristic], capsize=6)
        ax.set_title(characteristic)
        ax.set_xlabel("decade")
        ax.set_ylabel("value")

    plt.show()

# barcharts()


# # checking distributions for weeks_on_chart
# for decade in range(1970, 2030, 10):
#     song_df = with_spotify_dfs[decade]
#     count_df = weeks_on_chart_count(song_df=song_df)
#     print(count_df)
#     print(count_df['count'].sum())

# NUM_PERCENTILE = 5
# songs_df = all_songs_df
# # songs_df = songs_df[songs_df['weeks_on_chart']!=20]
# songs_df.sort_values(by=['weeks_on_chart'])
# print(songs_df.quantile([e/NUM_PERCENTILE for e in range(1, NUM_PERCENTILE)]))
# count_df = weeks_on_chart_count(song_df=songs_df)
# count_df.plot(x='weeks_on_chart', y='count', kind='bar')
# plt.title("Duration of songs on the Billboard charts")
# plt.ylabel("Number of songs")
# plt.xlabel("Number of weeks on the chart")
# # plt.grid()
# plt.show()

# for decade in range(1970, 2030, 10):
#     count_df = weeks_on_chart_count(song_df=with_spotify_dfs[decade])
#     # print(count_df)
#     count_df.plot(x='weeks_on_chart', y='count', kind='bar')
#     plt.show()
    
