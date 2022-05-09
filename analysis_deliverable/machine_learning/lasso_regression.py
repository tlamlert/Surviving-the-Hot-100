import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.linear_model import Lasso
import numpy as np


def with_and_without_spotify(complete_df):
    '''
    Description: makes two dataset - one containing the songs with Spotify attributes, one without
    Inputs: a Dataframe of songs with and without Spotify attributes
    Returns: a tuple of (Dataframe of songs with Spotify attributes, Dataframe without)
    '''
    # checks if danceability attribute is null or not
    missing_spotify_df = complete_df[complete_df.speechiness.isnull()]
    with_spotify_df = complete_df[complete_df.speechiness.notnull()]
    return with_spotify_df, missing_spotify_df


def normalize(np_arr):
    avg = np.average(np_arr, axis=0)
    max = np.max(np_arr, axis=0)
    min = np.min(np_arr, axis=0)
    return (np_arr) / (max - min)


def lasso(decade):
    # preprocess
    to_drop = ["song", "artist", "1st_appear", "type", "id", "uri", "track_href", "analysis_url"]
    all_songs_dfs = pd.read_csv(f'../dataset/song-features/{decade}s_features')
    with_spotify_dfs, without_spotify_dfs = with_and_without_spotify(all_songs_dfs)

    # drop songs with 20 weeks ??
    with_spotify_dfs = with_spotify_dfs[with_spotify_dfs["weeks_on_chart"]!=20]

    # drop unwanted columns
    for column in to_drop:
        with_spotify_dfs.drop(column, inplace=True, axis=1)
    y = with_spotify_dfs.pop("weeks_on_chart").values

    # # add squared columns
    # for column in with_spotify_dfs.columns:
    #     with_spotify_dfs[column+"_squared"] = with_spotify_dfs[column]**2

    # normalize
    X = with_spotify_dfs.values
    # X = normalize(X)

    # split dataset into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # define model
    model = Lasso(alpha=0.01)

    # define model evaluation method
    cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
    # evaluate model
    scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
    # force scores to be positive
    scores = np.absolute(scores)
    # print("coeficients: " , model.coef_)
    print('Mean MAE: %.3f (%.3f)' % (np.mean(scores), np.std(scores)))

    # fit model
    model.fit(X_train, y_train)

    # Predict test set
    yhat = model.predict(X_test)
    print("prediction")
    print(yhat[:10])
    print("actual number of weeks on chart")
    print(y_test[:10])

    # print the weights
    print(f'{decade}s model\'s coefficients: ')
    print(model.coef_)

if __name__ == '__main__':
    for decade in range(1970, 2030, 10):
        lasso(decade)