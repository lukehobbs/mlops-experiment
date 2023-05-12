import os
import warnings
import argparse

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import mlflow
import mlflow.sklearn

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha")
    parser.add_argument("--l1-ratio")
    args = parser.parse_args()

    input_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "input/Iris.csv"
    )
    data = pd.read_csv(input_path)

    X = data.drop(["Id", "Species"], axis=1)
    y = data["Species"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=5
    )

    with mlflow.start_run():
        knn = KNeighborsClassifier(n_neighbors=12)
        knn.fit(X_train, y_train)

        y_pred = knn.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        
        print(accuracy)

        mlflow.log_metric("acc", accuracy)

        mlflow.sklearn.log_model(
            sk_model=knn,
            artifact_path="model",
            registered_model_name="sk-learn-iris-knn-model"
        )
