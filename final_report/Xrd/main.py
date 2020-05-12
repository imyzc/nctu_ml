import pymatgen.ext.matproj
from pymatgen import MPRester
import json
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import numpy as np
import time

from ML_model import RFr
from side_fxn import _align
from pmg_load_data import load_data_from_api, get_XY


def main():
    #####
    # load data, get XY
    t1 = time.time()
    count_info, tt_i_list, a, b, c, alpha, beta, gamma = load_data_from_api("7sahRFJrSABCUN8T",
                                                                            "Ca-Co-Cr-Fe-K-Mn-Ni-Sc-Ti-V-")
    select_, notselect_, nomaterial_ = count_info
    X, Y = get_XY(tt_i_list, a, b, c, alpha, beta, gamma)
    t2 = time.time()
    print(f"Api load data, get XY time: {t2-t1} sec")
    print(f"Selected: {select_}")
    print(f"Not Selected: {notselect_}")
    print(f"No material: {nomaterial_}")

    #####
    # split XY
    x_train = X[0:30]
    y_train = Y[0:30]
    print(f"x_train shape: {x_train.shape}")  # (#, 180)
    print(f"y_train shape: {y_train.shape}")  # (#, 6)

    #####
    # model fit
    model_ = RFr(x_train, y_train)

    #####
    # model predict
    print("[Prediction of first 2 data]")
    print(f"Prediction: {model_.predict(X[0:1])}")
    print(f"Truth: {Y[0:1]}")
    print(f"Prediction: {model_.predict(X[1:2])}")
    print(f"Truth: {Y[1:2]}")


if __name__ == "__main__":
    main()
