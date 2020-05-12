from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from joblib import dump, load
from sklearn.svm import SVR
import numpy as np


def RFr(X, y):
    RFr_ = RandomForestRegressor(n_estimators=100, random_state=0)

    # fitting
    RFr_.fit(X, y)

    return RFr_


def main():
    #####
    # a test
    x_list = []
    ans_list = []
    for i in range(1000):
        create_ = np.random.uniform(0, 100, 10)
        x_list.append(create_)
        ans_list.append(sum(create_))
    x_array = np.array(x_list)
    y_array = np.array(ans_list)
    print(f"X shape: {x_array.shape}")
    print(f"Y shape: {y_array.shape}")

    model_ = RFr(x_array, y_array)

    # predict
    y = model_.predict(np.array([[20, 20, 20, 20, 20, 30, 30, 30, 30, 30]]))
    print(f"predict: {y}")
    print(f"actual: 250")


if __name__ == "__main__":
    main()
