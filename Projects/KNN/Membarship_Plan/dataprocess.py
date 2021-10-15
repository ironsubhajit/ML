# Process Data set

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import preprocessing, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class DataProcess:
    '''
    This Class Process and make KNN model for the given dataset
    K = 38 tends to max accuracy for prediction
    '''
    def __init__(self, data_loc, neighbors=38):
        self.dataset = data_loc
        self.df = pd.read_csv(self.dataset)
        self.k = neighbors
        self.x = None
        self.y = None

        # Below are only for dev purposes

        # self.x_train = None
        # self.x_test = None
        # self.y_train = None
        # self.y_test = None
        # self.neighbors = neighbors
        # self.mean_acc = np.zeros((self.neighbors - 1))
        # self.std_acc = np.zeros((self.neighbors - 1))

    def normalize(self):
        '''Normalize Dataset for KNN'''
        print("Normalizing Data...\n")
        self.x = self.df[[col for col in self.df.columns[:-1]]].values # as float type
        print(type(self.x))
        self.x = preprocessing.StandardScaler().fit(self.x).transform(self.x.astype(float))

        # custcat is the category of service plans for each customer, and its the target value to predict
        self.y = self.df['custcat'].values
        print("Normalizing Done.\n")

    def train_and_predict(self):
        self.normalize()    # Normalizing dataset

        # When in Production take all dataset for training
        # therefore remove below line
        # self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=4)

        neigh = KNeighborsClassifier(n_neighbors=self.k).fit(self.x, self.y)

        a = np.zeros((1, 11), dtype=float)
        for i in range(1):
            ip = list(map(float, input("Enter 11 data:\n").strip().split(" ")))
            a[i] = ip
        print(a)

        yhat = neigh.predict(a)
        return yhat

        # self.mean_acc[n-1] = metrics.accuracy_score(self.y_test, yhat)

        # self.std_acc[n-1] = np.std(yhat == self.y_test)/np.sqrt(yhat.shape[0])

        # best value of k
        # self.k = self.mean_acc.argmax() + 1
        # return f"Accuracy: {self.mean_acc.max()} with K: {self.k}\n"

    # Only for accuracy measure in dev purposes
    # def accuracyGraph(self):
    #     plt.plot(range(1, self.neighbors), self.mean_acc, 'g')
    #     plt.legend(f'Accuracy')
    #     plt.ylabel('Accuracy')
    #     plt.xlabel('Number of Neighbors (K)')
    #     plt.tight_layout()
    #     plt.show()

    def pnt_data(self):
        return f"DataSet:\n{self.df.head()}"


if __name__ == '__main__':
    loc = 'teleCustDetails.csv'
    data = DataProcess(loc, 100)
    print(data.train_and_predict())
    # data.accuracyGraph()
    print("Run Successful.")
