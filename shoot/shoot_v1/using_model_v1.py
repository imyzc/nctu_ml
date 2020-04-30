from joblib import load
from data_generator import *
import matplotlib.pyplot as plt
import numpy as np

from plotting import data_visualization

model_MLPr_i3_h = load("_train_model/MLPr_i3_h.joblib")
model_MLPr_i3_r = load("_train_model/MLPr_i3_r.joblib")

model_RFr_h = load("_train_model/RFr_h.joblib")
model_RFr_r = load("_train_model/RFr_r.joblib")

def generate_data():
    velocity_init = 0
    velocity_end = 200
    theta_init = 0
    theta_end = 180
    sample_amount = 1000
    return (velocity_init, velocity_end, sample_amount), (theta_init, theta_end, sample_amount)


def main():
    data_visualization(generate_data(), (model_RFr_h, model_RFr_r))


if __name__ == "__main__":
    main()
