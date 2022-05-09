import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn import metrics

def confusion_matrix():
    # get targets and predictions
    targs = np.load('y_test.npy')
    preds = np.load('pred_test.npy')

    # initialize figure and axis
    fig, ax = plt.subplots()

    # define labels and create confusion matrix
    labels = list(range(0, 5))
    label_titles = ['1-3 wks', '4-8 wks', '9-13 wks', '14-18 wks', '19+ wks']
    cf_matrix = metrics.confusion_matrix(targs, preds, labels=labels)
    cf_matrix_df = pd.DataFrame(cf_matrix, index=label_titles, columns=label_titles)

    # plot
    sns.heatmap(ax=ax, data=cf_matrix_df, annot=True, fmt="")

    # add title and axes
    ax.set_title(f"Confusion Matrix for Classification Model")
    ax.set_xlabel("Predictions")
    ax.set_ylabel("Targets")

    plt.show()


def f1_score():
    # get targets and predictions
    targs = np.load('y_test.npy')
    preds = np.load('pred_test.npy')

    # f1-score
    f1_score = metrics.f1_score(targs, preds, average='macro')
    print(f1_score)


if __name__ == '__main__':
    confusion_matrix()
    # f1_score()