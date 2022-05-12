import numpy as np
import pandas as pd
import tensorflow as tf
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
    # checks if track_href attribute is null or not
    missing_spotify_df = complete_df[complete_df.track_href.isnull()]
    with_spotify_df = complete_df[complete_df.track_href.notnull()]
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

    # drop songs with 20 weeks
    with_spotify_dfs = with_spotify_dfs[with_spotify_dfs["weeks_on_chart"] != 20]

    # map to category (20 weeks excluded)
    with_spotify_dfs["popularity"] = \
        (with_spotify_dfs["weeks_on_chart"] > 3) * 1 \
        + (with_spotify_dfs["weeks_on_chart"] > 8) * 1 \
        + (with_spotify_dfs["weeks_on_chart"] > 13) * 1 \
        + (with_spotify_dfs["weeks_on_chart"] > 18) * 1

    # # map to category (20 weeks included)
    # with_spotify_dfs["popularity"] = \
    #     (with_spotify_dfs["weeks_on_chart"] > 4) * 1 \
    #     + (with_spotify_dfs["weeks_on_chart"] > 8) * 1 \
    #     + (with_spotify_dfs["weeks_on_chart"] > 14) * 1 \
    #     + (with_spotify_dfs["weeks_on_chart"] > 19) * 1

    distribution = [np.count_nonzero(with_spotify_dfs["popularity"] == e) for e in list(range(0, 5))]
    print(distribution / np.sum(distribution))

    # drop unwanted columns
    for column in to_drop:
        with_spotify_dfs.drop(column, inplace=True, axis=1)
    wks = with_spotify_dfs.pop("weeks_on_chart").to_numpy()
    y = with_spotify_dfs.pop("popularity").to_numpy()

    # normalization
    with_spotify_dfs = with_spotify_dfs / (with_spotify_dfs.max() - with_spotify_dfs.min())
    X = with_spotify_dfs.to_numpy()

    # Split dataset into training and testing :
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    return X_train, X_test, y_train, y_test


def model():
    '''
    Description: train a ffnn model with 2 dense layers
    '''
    # preprocess
    X_train, X_test, y_train, y_test = get_data()
    one_hot_train = tf.keras.utils.to_categorical(y_train, num_classes=5)
    one_hot_test = tf.keras.utils.to_categorical(y_test, num_classes=5)

    # define model
    model = Sequential([
        Dense(64, kernel_initializer='normal', activation="relu"),
        Dense(32, kernel_initializer='normal', activation="relu"),
        Dense(5, kernel_initializer='normal', activation="softmax"),
    ])

    # compile the model before calling fit()
    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

    # fit model
    history = model.fit(
        X_train,
        one_hot_train,
        batch_size=100,
        epochs=20,
        validation_data=(X_test, one_hot_test),
    )

    # plot loss during training
    pyplot.title('Loss / Cross Entropy')
    pyplot.plot(history.history['loss'], label='train')
    pyplot.plot(history.history['val_loss'], label='test')
    pyplot.legend()
    pyplot.show()

    # evaluate the model
    pred_train = model.predict(X_train)
    scores = model.evaluate(X_train, one_hot_train, verbose=0)
    print('Accuracy on training data: {}%'.format(scores[1]))

    pred_test = model.predict(X_test)
    scores2 = model.evaluate(X_test, one_hot_test, verbose=0)
    print('Accuracy on test data: {}%'.format(scores2[1]))

    # Generate predictions on new data using `predict`
    print("Generate predictions for 25 samples")
    print(y_test[:25])
    np.set_printoptions(precision=3, suppress=True)
    print(np.argmax(pred_test[:25], axis=1))

    np.save('y_test', y_test)
    np.save('pred_test', np.argmax(pred_test, axis=1))

    # save the model
    model.save('./final-model')

    # print model summary
    print(model.summary())


if __name__ == '__main__':
    model()