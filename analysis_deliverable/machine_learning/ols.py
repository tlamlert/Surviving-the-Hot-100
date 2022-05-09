import pandas as pd
import statsmodels.api as sm
from statsmodels.tools import eval_measures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def with_and_without_spotify(complete_df):
    '''
    Description: makes two dataset - one containing the songs with Spotify attributes, one without
    Inputs: a Dataframe of songs with and without Spotify attributes
    Returns: a tuple of (Dataframe of songs with Spotify attributes, Dataframe without)
    '''
    # checks if danceability attribute is null or not
    missing_spotify_df = complete_df[complete_df.track_href.isnull()]
    with_spotify_df = complete_df[complete_df.track_href.notnull()]
    return with_spotify_df, missing_spotify_df


def ols(decade):
    # preprocess
    to_drop = ["song", "artist", "1st_appear", "danceability", "type", "id", "uri", "track_href", "analysis_url"]
    all_songs_dfs = pd.read_csv(f'../dataset/song-features/{decade}s_features')
    with_spotify_dfs, without_spotify_dfs = with_and_without_spotify(all_songs_dfs)

    # drop unwanted columns
    for column in to_drop:
        with_spotify_dfs.drop(column, inplace=True, axis=1)

    # print(with_spotify_dfs.dtypes)
    y = with_spotify_dfs.pop("weeks_on_chart").values
    X = with_spotify_dfs.values

    # # add squared columns
    # for column in with_spotify_dfs.columns:
    #     with_spotify_dfs[column+"_squared"] = with_spotify_dfs[column]**2

    # split dataset into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # add constants
    X_train = sm.add_constant(X_train)
    X_test = sm.add_constant(X_test)

    # define model and fit the mode.
    model = sm.OLS(y_train, X_train).fit()

    # calculate mse for the models
    y_pred_train = model.predict(X_train)
    mse_train = eval_measures.mse(y_train, y_pred_train)
    y_pred_test = model.predict(X_test)
    mse_test = eval_measures.mse(y_test, y_pred_test)

    # Calculate the *test* R-squared value (using sklearn's r2_score function)
    rsquared_val = r2_score(y_test, y_pred_test)

    # model evaluation
    print(f"mse on training set: {mse_train}")
    print(f"mse on testing set: {mse_test}")
    print(f"R-squared value: {rsquared_val}")

    # prediction
    print("Labels")
    print(y_test[:10])
    print("Predictions")
    print(y_pred_test[:10])

    # # model summary
    # print(model.summary())


if __name__ == '__main__':
    for decade in range(1970, 2030, 10):
        ols(decade)
