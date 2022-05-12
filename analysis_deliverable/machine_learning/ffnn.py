import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from matplotlib import pyplot


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


def get_data():
    '''
    Description: get dataset from the local directory and split it into training and testing data
    Inputs: none
    Returns: training inputs, testing inputs, training labels, testing labels
    '''
    # preprocess
    to_drop = ["song", "artist", "1st_appear", "type", "id", "uri", "track_href", "analysis_url"]
    all_songs_dfs = pd.read_csv('../dataset/song-features/all_features')
    with_spotify_dfs, without_spotify_dfs = with_and_without_spotify(all_songs_dfs)

    # drop unwanted columns
    for column in to_drop:
        with_spotify_dfs.drop(column, inplace=True, axis=1)
    y = with_spotify_dfs.pop("weeks_on_chart").values
    X = with_spotify_dfs.values

    # Split dataset into training and testing :
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

    return X_train, X_test, y_train, y_test


def main():
    '''
    Description: train a ffnn model with 2 dense layers
    '''
    # preprocess
    X_train, X_test, y_train, y_test = get_data()

    # define model
    model = Sequential([
        Dense(64, kernel_initializer='normal', activation="relu"),
        Dense(32, kernel_initializer='normal', activation="relu"),
        Dense(1, kernel_initializer='normal'),
    ])

    # compile the model before calling fit()
    model.compile(
        optimizer=keras.optimizers.RMSprop(learning_rate=1e-3),
        loss='mse',
        metrics=[tf.keras.metrics.MeanSquaredError()]
    )

    # fit model
    history = model.fit(
        X_train,
        y_train,
        batch_size=64,
        epochs=10,
        validation_data=(X_test, y_test),
    )

    # evaluate the model
    train_mse = model.evaluate(X_train, y_train, verbose=0)
    test_mse = model.evaluate(X_test, y_test, verbose=0)
    print(train_mse)
    print(test_mse)
    # print('Train: %.3f, Test: %.3f' % (train_mse, test_mse))

    # plot loss during training
    pyplot.title('Loss / Mean Squared Error')
    pyplot.plot(history.history['loss'], label='train')
    pyplot.plot(history.history['val_loss'], label='test')
    pyplot.legend()
    pyplot.show()

    # Evaluate the model on the test data using `evaluate`
    print("Evaluate on test data")
    results = model.evaluate(X_test, y_test, batch_size=128)
    print("test loss, test acc:", results)

    # Generate predictions on new data using `predict`
    print("Generate predictions for 10 samples")
    predictions = model.predict(X_test[:10])
    print(y_test[:10])
    print(predictions)

    # save the model
    model.save('./models/cat-model-test')

if __name__ == '__main__':
    main()
