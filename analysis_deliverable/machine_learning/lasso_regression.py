import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso


def with_and_without_spotify(complete_df):
    '''
    Description: makes two dataset - one containing the songs with Spotify attributes, one without
    Inputs: a Dataframe of songs with and without Spotify attributes
    Returns: a tuple of (Dataframe of songs with Spotify attributes, Dataframe without)
    '''
    # checks if danceability attribute is null or not
    missing_spotify_df = complete_df[complete_df.danceability.isnull()]
    with_spotify_df = complete_df[complete_df.danceability.notnull()]
    return with_spotify_df, missing_spotify_df


# preprocess
all_songs_dfs = pd.read_csv('./dataset/features-sample.csv')
with_spotify_dfs, without_spotify_dfs = with_and_without_spotify(all_songs_dfs)
data = all_songs_dfs.values
X = data[data != "weeks_on_chart"]
y = data[data == "weeks_on_chart"]
print(X[:10])
# X_train, X_val_test, y_train, y_val_test = train_test_split(X, y, test_size = 0.4, random_state = 1)