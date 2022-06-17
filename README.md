# Lake Mendota Ice covered days Prediction


## Objective
- The objective of this project is to predict the number of days Lake Mendota is covered by ice and eventually predict the specific year when the Lake Mendota would be no longer covered by ice
## Dataset

- The dataset (Lake_Mendota.csv) for this program is manually created by myself. I retrieve years and the number of ice covered days of Lake Mendota in Wisconsin Madison from [Wisconsin State Climatology Office](https://www.aos.wisc.edu/~sco/lakes/Mendota-ice.html). Linear Regression Analysis is applied on this data to calculate and predict the number of ice covered days of Lake Mendota at specific years.

## Main concepts & Equations

- Using the whole data set as the training set, train a linear regression model:
- <img width="123" alt="Screen Shot 2022-06-14 at 10 41 18 PM" src="https://user-images.githubusercontent.com/69660509/173816577-966a7b14-2e14-4f67-ba91-70bc60aa63e9.png">
- Finding the closed-form MLE solution:
- <img width="237" alt="Screen Shot 2022-06-14 at 10 43 15 PM" src="https://user-images.githubusercontent.com/69660509/173817348-da7f6843-60da-4c80-92ae-83062d0fb931.png">
- The MLE solution in matrix form:
- <img width="185" alt="Screen Shot 2022-06-14 at 10 45 05 PM" src="https://user-images.githubusercontent.com/69660509/173817926-ef3bd01f-5be4-4b29-aa7a-c21a055e0c17.png">
- The final MLE solution this program uses by setting the gradient to zero 
- <img width="171" alt="Screen Shot 2022-06-14 at 10 45 33 PM" src="https://user-images.githubusercontent.com/69660509/173818555-d1bef7a1-9a0a-4a27-b1b4-24fa44fbc61b.png">
- Predicting the specific year (x*) when the Lake Mendota will be no longer covered by ice
- <img width="114" alt="Screen Shot 2022-06-16 at 8 37 02 AM" src="https://user-images.githubusercontent.com/69660509/174082556-f1557870-6e5d-4b94-904a-c0ab6d7f0539.png">


## Conclusion

- β1 is the beta coefficient. The sign of a beta coefficient tells us that whether there is a positive or negative correlation between the independent variable (years) and the dependent variable (ice coverd days). Since the sign of β1 is negative here, we explain that as year increases, the number of days Lake Mendota was covered by ice decreases
- x* is a compelling prediction based on the trends in the data because as we can observe in the data, there is a trend (not obvious) that as time goes by, the number of days Lake Mendota was covered by ice is decreasing. Especially, since 2014, the number of days Lake Mendota was covered by ice has never been more than 91 days. Based on the prediction, the Lake Mendota will no longer be covered by ice from the year 2456.
- Prediction for 2021-2022 is 85.6 days and the actual record is 85 days and so the prediction is pretty accurate.
## Downside & Future Direction

- In this problem, X.T@X is invertible such that it could be easily solved by the closed-form MLE. However, if the X.T@X is not invertible, then it should be solved in different approaches.
- Need to consider different methods such as performing gradient descent on the MSE. 