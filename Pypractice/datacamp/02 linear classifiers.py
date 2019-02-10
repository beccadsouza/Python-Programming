'''
How models make predictions
Which classifiers make predictions based on the sign (positive or negative) of the raw model output?

ANSWER THE QUESTION
50 XP
Possible Answers
Logistic regression only
press 1
Linear SVMs only
press 2
Neither
press 3
Both logistic regression and Linear SVMs
press 4

Submit Answer
Take Hint (-15 XP)
INCORRECT SUBMISSION
Remember, logistic regression and linear SVMs make predictions in the same way.
'''

ans = 4

"""
Changing the model coefficients
In this exercise, you will observe the effects of changing the coefficients of a linear classifer. A 2D dataset is already loaded into the environment as X and y, along with a linear classifier object model.

INSTRUCTIONS
0 XP
Explore the effects of changing the two coefficients and the intercept.
Set the coefficients and intercept so that the model makes no errors.
HINT
The first element of model.coef_ should be a negative number, and the second element should be a positive number. Remember that coef_ controls the angle of the boundary and intercept_ shifts the boundary without changing the angle.
"""

# Set the coefficients
model.coef_ = np.array([[-1,1]])
model.intercept_ = np.array([-3])

# Plot the data and decision boundary
plot_classifier(X,y,model)

# Print the number of errors
num_err = np.sum(y != model.predict(X))
print("Number of errors:", num_err)

"""

The 0-1 loss
In the figure below, what is the 0-1 loss (number of classification errors) of the classifier?



ANSWER THE QUESTION
35 XP
Possible Answers
0
press 1
1
press 2
2
press 3
3
press 4

Submit Answer
HINT
There is one red point predicted to be blue, and one blue point predicted to be red.
"""
ans = 3

"""
Minimizing a loss function
In this exercise you'll implement linear regression "from scratch" using scipy.optimize.minimize. We'll train a model on the Boston housing price data set, which is already loaded into the variables X and y. For simplicity, we won't include an intercept in our regression model.

INSTRUCTIONS
0 XP
Fill in the loss function for least squares linear regression.
Fill in the call to minimize.
Compare the coefficients to sklearn's LinearRegression.
HINT
The loss is the square of the difference between y[i] and predicted_y.
"""

# The squared error, summed over training examples
def my_loss(w):
    s = 0
    for i in range(y.size):
        predicted_y_i = w@X[i]
        s = s + (predicted_y_i - y[i])**2
    return s

# Returns the w that makes my_loss(w) smallest
w_fit = minimize(my_loss, X[0]).x
print(w_fit)

# Compare with scikit-learn's LinearRegression
lr = LinearRegression(fit_intercept=False).fit(X,y)
print(lr.coef_)

"""
Classification loss functions
Which of the four loss functions makes sense for classification?



ANSWER THE QUESTION
35 XP
Possible Answers
(1)
press 1
(2)
press 2
(3)
press 3
(4)
press 4

Submit Answer
HINT
You're looking for a loss that prefers (has lower values for) correct predictions and higher values for incorrect predictions.
"""

ans = 2

"""
Comparing the logistic and hinge losses
In this exercise you'll create a plot of the logistic and hinge losses using their mathematical expressions, which are provided to you. The loss function diagram from the video is shown on the right.

INSTRUCTIONS
0 XP
Plot the logistic and hinge losses evaluated on the grid points.
HINT
Use the provided log_loss and hinge_loss functions.
"""

# Mathematical functions for logistic and hinge losses
# Feel free to ignore if you're not interested
def log_loss(raw_model_output):
   return np.log(1+np.exp(-raw_model_output))
def hinge_loss(raw_model_output):
   return np.maximum(0,1-raw_model_output)

# Create a grid of values and plot
grid = np.linspace(-2,2,1000)
plt.plot(grid, log_loss(grid), label='logistic')
plt.plot(grid, hinge_loss(grid), label='hinge')
plt.legend()
plt.show()

"""
Implementing logistic regression
This is very similar to the earlier exercise where you implemented linear regression "from scratch" using scipy.optimize.minimize. However, this time we'll minimize the logistic loss and compare with scikit-learn's LogisticRegression (we've set C to a large value to disable regularization; more on this in Chapter 3!). The log_loss function from the previous exercise is already defined in your environment, and the sklearn breast cancer prediction dataset (first 10 features, standardized) is loaded into the variables X and y.

INSTRUCTIONS
0 XP
Fill in the loss function for logistic regression.
Compare the coefficients to sklearn's LogisticRegression.
HINT
There are several ways to get the number of training examples, such as y.size, len(y), or len(X).
Call log_loss, which is already defined for you.
"""

# The logistic loss, summed over training examples
def my_loss(w):
    s = 0
    for i in range(y.size):
        raw_model_output = w@X[i]
        s = s + log_loss(raw_model_output * y[i])
    return s

# Returns the w that makes my_loss(w) smallest
w_fit = minimize(my_loss, X[0]).x
print(w_fit)

# Compare with scikit-learn's LogisticRegression
lr = LogisticRegression(fit_intercept=False, C=1000000).fit(X,y)
print(lr.coef_)
