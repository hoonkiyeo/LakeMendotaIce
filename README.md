# Lake Mendota Ice covered days Prediction


## Summary
- The objective of this project is to predict the number of days Lake Mendota is covered by ice and eventually predict the specific year when the Lake Mendota would be no longer covered by ice
- 
## Dataset

- The dataset (Lake_Mendota.csv) for this program is manually created by myself. I retrieve years and the number of ice covered days of Lake Mendota in Wisconsin Madison from [Wisconsin State Climatology Office](https://www.aos.wisc.edu/~sco/lakes/Mendota-ice.html). Linear Regression Analysis is applied on this data to calculate and predict the number of ice covered days of Lake Mendota at specific years.

## Steps and Equations

- Using the whole data set as the training set, train a linear regression model:
- <img width="123" alt="Screen Shot 2022-06-14 at 10 41 18 PM" src="https://user-images.githubusercontent.com/69660509/173816577-966a7b14-2e14-4f67-ba91-70bc60aa63e9.png">
- Finding the closed-form MLE solution:
- <img width="237" alt="Screen Shot 2022-06-14 at 10 43 15 PM" src="https://user-images.githubusercontent.com/69660509/173817348-da7f6843-60da-4c80-92ae-83062d0fb931.png">
- The MLE solution in matrix form:
- <img width="185" alt="Screen Shot 2022-06-14 at 10 45 05 PM" src="https://user-images.githubusercontent.com/69660509/173817926-ef3bd01f-5be4-4b29-aa7a-c21a055e0c17.png">
- The final MLE solution this program uses by setting the gradient to zero 
- <img width="171" alt="Screen Shot 2022-06-14 at 10 45 33 PM" src="https://user-images.githubusercontent.com/69660509/173818555-d1bef7a1-9a0a-4a27-b1b4-24fa44fbc61b.png">

## Conclusion

- 