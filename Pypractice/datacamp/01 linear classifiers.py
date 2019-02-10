"""
KNN classification
In this exercise you'll explore a subset of the Large Movie Review Dataset. The variables X_train, X_test, y_train, and y_test are already loaded into the environment. The X variables contain features based on the words in the movie reviews, and the y variables contain labels for whether the review sentiment is positive (+1) or negative (-1).

INSTRUCTIONS
0 XP
Create a KNN model with default hyperparameters.
Fit the model.
Print out the prediction for the test example 0.
HINT
The model you want to create is already imported. After that, the functions you need are fit, predict, and score.
"""

from sklearn.neighbors import KNeighborsClassifier

# Create and fit the model
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Predict on the test features, print the results
pred = knn.predict(X_test)[0]
print("Prediction for test example 0:", pred)


"""
Comparing models
Compare k nearest neighbors classifiers with k=1 and k=5 on the handwritten digits data set, which is already loaded into the variables X_train, y_train, X_test, and y_test. You can set k with the n_neighbors parameter when creating the KNeighborsClassifier object, which is also already imported into the environment.

Which model has a higher test accuracy?

INSTRUCTIONS
35 XP
Possible Answers
k=1
press 1
k=5
press 2

Submit Answer
HINT
Create the two classifiers with KNeighborsClassifier(n_neighbors=1) and KNeighborsClassifier(n_neighbors=5). Then, fit and score each one.
"""

ans = k = 5

"""
Overfitting
Which of the following situations looks like an example of overfitting?

ANSWER THE QUESTION
35 XP
Possible Answers
Training accuracy 50%, testing accuracy 50%.
press 1
Training accuracy 95%, testing accuracy 95%.
press 2
Training accuracy 95%, testing accuracy 50%.
press 3
Training accuracy 50%, testing accuracy 95%.
press 4

Submit Answer
HINT
Overfitting means your model is very good at predicting on the training data, without necessarily generalizing well to unseen (test) data.
"""

ans = 3

"""
Running LogisticRegression and SVC
In this exercise, you'll apply logistic regression and a support vector machine to classify images of handwritten digits.

INSTRUCTIONS
0 XP
Apply logistic regression and SVM to the handwritten digits data set using the provided train/validation split.
For each classifier, print out the training and validation accuracy.
HINT
First, instantiate a LogisticRegression object and fit it on the training data by calling fit. You can then use the score function to evaluate the classification accuracy on the train and test sets. Then repeat for SVC.
"""

from sklearn import datasets
digits = datasets.load_digits()
Xtrain, Xtest, ytrain, ytest = train_test_split(digits.data, digits.target)

# Apply logistic regression and print scores
lr = LogisticRegression()
lr.fit(Xtrain, ytrain)
print(lr.score(Xtrain, ytrain))
print(lr.score(Xtest, ytest))

# Apply SVM and print scores
svm = SVC()
svm.fit(Xtrain, ytrain)
print(svm.score(Xtrain, ytrain))
print(svm.score(Xtest, ytest))

"""
Sentiment analysis for movie reviews
In this exercise you'll explore the probabilities outputted by logistic regression on a subset of the Large Movie Review Dataset. The variables X and y are already loaded into the environment. X contains features based on the number of times words appear in the movie reviews, and y contains labels for whether the review sentiment is positive (+1) or negative (-1).

INSTRUCTIONS
0 XP
Train a logistic regression model on the movie review data.
Predict the probabilities of negative vs. positive for the two given reviews.
Feel free to write your own reviews and get probabilities for those too!
HINT
Use the predic_proba function to get the predicted probabilities of each class.
"""

# Instantiate logistic regression and train
lr = LogisticRegression()
lr.fit(X, y)

# Predict sentiment for a glowing review
review1 = "LOVED IT! This movie was amazing. Top 10 this year."
review1_features = get_features(review1)
print("Review:", review1)
print("Probability of positive review:", lr.predict_proba(review1_features)[0,1])

# Predict sentiment for a poor review
review2 = "Total junk! I'll never watch a film by that director again, no matter how good the reviews."
review2_features = get_features(review2)
print("Review:", review2)
print("Probability of positive review:", lr.predict_proba(review2_features)[0,1])

"""
Which decision boundary is linear?
Which of the following is a linear decision boundary?



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
In 2 dimensions, a linear decision boundary is just a straight line.
"""
ans = 1

"""
Visualizing decision boundaries
In this exercise, you'll visualize the decision boundaries of various classifier types. A subset of scikit-learn's built-in wine dataset is already loaded into X along with binary labels in y.

INSTRUCTIONS
0 XP
Create the following classifier objects with default hyperparameters: LogisticRegression, LinearSVC, SVC, KNeighborsClassifier.
Fit each of the classifiers on the provided data using a for loop.
Call the plot_4_classifers function (similar to the code here), passing in X, y, and a list containing the four classifiers.
HINT
Everything you need for the classifiers list is imported for you already. Don't forget to actually instantiate these with () after each classifier name.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier

# Define the classifiers
classifiers = [LogisticRegression(), LinearSVC(),
               SVC(), KNeighborsClassifier()]

# Fit the classifiers
for c in classifiers:
    c.fit(X, y)

# Plot the classifiers
plot_4_classifiers(X, y, classifiers)
plt.show()
