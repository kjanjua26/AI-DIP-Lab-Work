import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestClassifier

DISGUISED = ['Q006', 'Q015', 'Q029', 'Q028', 'Q034', 'Q087', 'Q090']

DISTANCE_VECTOR = shuffle(pd.read_csv('distance.csv'))
DISTANCE_VECTOR = DISTANCE_VECTOR[~DISTANCE_VECTOR['Question'].isin(DISGUISED)]
FEATURE_LIST = list(DISTANCE_VECTOR.columns)[2:]
X = DISTANCE_VECTOR[['Ratio', 'Transitions',
                     'Black_Size', 'Normalization',
                     'Normalization_Sums', 'Angles',
                     'Centroid']].dropna()
y = DISTANCE_VECTOR['Ref'] + DISTANCE_VECTOR['Question']

def plot_important_features():
    model = RandomForestClassifier()
    model.fit(X, y)
    importances = model.feature_importances_
    std = np.std([tree.feature_importances_ for tree in model.estimators_], axis=0)
    indices = np.argsort(importances)
    plt.figure()
    plt.title("Feature importances")
    plt.barh(range(X.shape[1]), importances[indices],
             color="black", xerr=std[indices], align="center")
    plt.yticks(range(X.shape[1]), FEATURE_LIST)
    plt.ylim([-1, X.shape[1]])
    plt.show()

if __name__ == "__main__":
    plot_important_features()
