import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_results(filename):
    df = pd.read_csv(filename)
    #plot
    plt.plot(df['year'], df['days'])
    plt.xlabel("Year")
    plt.ylabel("Number of frozen days")
    plt.savefig("plot.png")
    
    features = np.matrix(df['year'])
    ones = np.matrix(np.ones((len(df['year']))).astype(int))
    #3.a
    X = np.hstack((np.transpose(ones),np.transpose(features)))
    print("Q3a:")
    print(X)
    #3.b
    Y = np.array(df['days'])
    print("Q3b:")
    print(Y)
    #3.c
    Z = X.T@X
    print("Q3c:")
    print(Z)
    #3.d
    I = np.linalg.inv(Z)
    print("Q3d:")
    print(I)
    #3.e
    PI = I@X.T
    print("Q3e:")
    print(PI)
    #3.f
    hat_beta = PI@Y
    print("Q3f:")
    print(hat_beta)
    #4
    y_test = hat_beta[0,0] + hat_beta[0,1]*2021
    print("Q4: " + str(y_test))
    #5a
    if hat_beta[0,1] == 0:
        Symbol = "="
    elif hat_beta[0,1] > 0:
        Symbol = ">"
    else:
        Symbol = "<"
    print("Q5a: " + Symbol)
    print("Q5b: β1 is the beta coefficient. The sign of a beta coefficient tells us that whether there is a positive or negative correlation between the independent variable (years) and the dependent variable (ice coverd days). Since the sign of β1 is negative here, we explain that as year increases, the number of days Lake Mendota was covered by ice decreases")
    #6a
    x_star = -hat_beta[0,0] / hat_beta[0,1]
    print("Q6a: " + str(x_star))
    #6b
    print("Q6b: x* is a compelling prediction based on the trends in the data because as we can observe in the data, there is a trend (not obvious) that as time goes by, the number of days Lake Mendota was covered by ice is decreasing. Especially, since 2014, the number of days Lake Mendota was covered by ice has never been more than 91 days.")

    
if __name__ == "__main__":
    filename = sys.argv[1]
    get_results(filename)