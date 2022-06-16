import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_dataset(filename):
    df = pd.read_csv(filename)
    return df

def get_plot(filename):
    df = pd.read_csv(filename)
    plt.plot(df[df.columns[0]], df[df.columns[1]])
    plt.xlabel("Year")
    plt.ylabel("Number of frozen days")
    plt.savefig("frozen.png")
    
def get_matrix_X(dataframe):
    df = dataframe
    years = np.matrix(df['year'])
    ones = np.matrix(np.ones(len(df['year']))).astype(int)
    X = np.hstack((ones.T, years.T))
    return X

def get_vector_Y(dataframe):
    df = dataframe
    Y = np.array(df['days'])
    return Y

def get_matrix_Z(X):
    Z = X.T@X
    return Z

#I = inverse of X.T@X
def get_matrix_I(Z):
    I = np.linalg.inv(Z)
    return I

#PI = pseudo-inverse of X
def get_matrix_PI(I):
    PI = I@X.T
    return PI

def get_hat_beta(PI):
    beta = PI@Y
    return beta

def prediction(year):
    pred_days = hat_beta[0,0] + hat_beta[0,1]*year
    return pred_days

def get_x_star():
    x_star = -hat_beta[0,0] / hat_beta[0,1]
    return x_star

if __name__ == "__main__":
    input_year = int(input())
    df = get_dataset("Lake_Mendota.csv")
    get_plot("Lake_Mendota.csv")
    X = get_matrix_X(df)
    Y = get_vector_Y(df)
    Z = get_matrix_Z(X)
    I = get_matrix_I(Z)
    PI = get_matrix_PI(I)
    hat_beta = get_hat_beta(PI)
    print(prediction(input_year))
    print(get_x_star())
    
    
    