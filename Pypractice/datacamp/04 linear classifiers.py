"""
Support vector definition
Which of the following is a true statement about support vectors?
 To help you out, here's the picture of support vectors from the video (top),
 as well as the hinge loss from Chapter 2 (bottom).
ANSWER THE QUESTION
35 XP
Possible Answers
All support vectors are classified correctly.
press 1
All support vectors are classified incorrectly.
press 2
All correctly classified points are support vectors.
press 3
All incorrectly classified points are support vectors.
press 4

Submit Answer
Support vectors are the points that "matter". They aren't necessarily classified correctly.
Are you sure about that? Take another look at the figure above.
Almost! But one can also become a support vector by being classified correctly and close to the boundary.

HINT
There are two ways to become a support vector: either the point is classified incorrectly, or it is classified correctly but very close to the boundary.
"""

ans = 4


"""
Effect of removing examples
Support vectors are defined as training examples that influence the decision boundary. In this exercise, you'll observe this behavior by removing non support vectors from the training set. The wine quality dataset is already loaded into X and y (first two features only). (Note: we specify lims in plot_classifier so that the two plots are forced to use the same axis limits and can be compared directly.)

INSTRUCTIONS
0 XP
Train a linear SVM on the whole data set.
Create a new data set containing only the support vectors.
Train a new linear SVM on the smaller data set.
HINT
svm.support_ returns the indices of the support vectors of the model svm. You can use this to directly index into X and y and return subsets containly only those examples. For example, X[svm.support_].
"""

# Train a linear SVM
svm = SVC(kernel="linear")
svm.fit(X,y)
plot_classifier(X, y, svm, lims=(11,15,0,6))

# Make a new data set keeping only the support vectors
print("Number of original examples", len(X))
print("Number of support vectors", len(svm.support_))
X_small = X[svm.support_]
y_small = y[svm.support_]

# Train a new SVM using only the support vectors
svm_small = SVC(kernel="linear")
svm_small.fit(X_small, y_small)
plot_classifier(X_small, y_small, svm_small, lims=(11,15,0,6))

"""
GridSearchCV warm-up
In the video we saw that increasing the RBF kernel hyperparameter gamma increases training accuracy. In this exercise we'll search for the gamma that maximizes cross-validation accuracy using scikit-learn's GridSearchCV. A binary version of the handwritten digits dataset, in which you're just trying to predict whether or not an image is a "2", is already loaded into the variables X and y.

INSTRUCTIONS
0 XP
Create a GridSearchCV object.
Call the fit method to select the best value of gamma based on cross-validation accuracy.
HINT
When instantiating the GridSearchCV object, pass in the model and the parameters. Then, call fit using the searcher object itself, not the original model.
"""

# Instantiate an RBF SVM
svm = SVC()

# Instantiate the GridSearchCV object and run the search
parameters = {'gamma':[0.00001, 0.0001, 0.001, 0.01, 0.1]}
searcher = GridSearchCV(svm, parameters)
searcher.fit(X, y)

# Report the best parameters
print("Best CV params", searcher.best_params_)

"""
Jointly tuning gamma and C with GridSearchCV
In the previous exercise the best value of gamma was 0.001 using the default value of C, which is 1. In this exercise you'll search for the best combination of C and gamma using GridSearchCV. As in the previous exercise, the 2-vs-not-2 digits dataset is already loaded, but this time it's split into the variables X_train, y_train, X_test, and y_test. Even though cross-validation already splits the training set into parts, it's often a good idea to hold out a separate test set to make sure the cross-validation results are sensible.

INSTRUCTIONS
0 XP
Run GridSearchCV to find the best hyperparameters using the training set.
Print the best values of the parameters.
Print out the accuracy on the test set, which was not used during the cross-validation procedure.
HINT
The GridSearchCV object is fit using the same syntax as other scikit-learn objects.
"""

# Instantiate an RBF SVM
svm = SVC()

# Instantiate the GridSearchCV object and run the search
parameters = {'C':[0.1, 1, 10], 'gamma':[0.00001, 0.0001, 0.001, 0.01, 0.1]}
searcher = GridSearchCV(svm, parameters)
searcher.fit(X_train, y_train)

# Report the best parameters and the corresponding score
print("Best CV params", searcher.best_params_)
print("Best CV accuracy", searcher.best_score_)

# Report the test accuracy using these best parameters
print("Test accuracy of best grid search hypers:", searcher.score(X_test, y_test))

"""
An advantage of SVMs
Which of the following is an advantage of SVMs over logistic regression?

ANSWER THE QUESTION
35 XP
Possible Answers
They naturally outputs meaningful probabilities.
press 1
They can be used with kernels.
press 2
They are computationally efficient with kernels.
press 3
They learn sigmoidal decision boundaries.
press 4

Submit Answer
Actually, it's logistic regression that outputs probabilities!
Logistic regression actually can be used with kernels, even if it's not common.
Kernel SVMs can learn all sorts of decision boundaries, but there's nothing particularly sigmoidal going on here.
Hint
Both models can use kernels, but there's an advantage with SVMs.
"""
ans = 3

"""

An advantage of logistic regression
Which of the following is an advantage of logistic regression over SVMs?

ANSWER THE QUESTION
35 XP
Possible Answers
It naturally outputs meaningful probabilities.
press 1
It can be used with kernels.
press 2
It is computationally efficient with kernels.
press 3
It learns sigmoidal decision boundaries.
press 4

HINT
Remember that we used a function called predict_proba for logistic regression.
INCORRECT SUBMISSION
Logistic regression and SVMs can both be used with kernels.
Actually, it's SVMs that are more efficient with kernels.
The sigmoid function is used to convert the raw model output to a probability, but the decision boundary is still linear.
"""

ans = 1

"""
Using SGDClassifier
In this final coding exercise, you'll do a hyperparameter search over the regularization type, regularization strength, and the loss (logistic regression vs. linear SVM) using SGDClassifier.

INSTRUCTIONS
0 XP
Instantiate an SGDClassifier instance with random_state=0.
Search over the regularization strength, the hinge vs. log losses, and L1 vs. L2 regularization.
HINT
To search over the two losses put "hinge" and "log" in the list.
To search over the two regularization types put "l1" and "l2" in the list.
"""

# We set random_state=0 for reproducibility
linear_classifier = SGDClassifier(random_state=0)

# Instantiate the GridSearchCV object and run the search
parameters = {'alpha':[0.00001, 0.0001, 0.001, 0.01, 0.1, 1],
             'loss':['hinge', 'log'], 'penalty':['l1','l2']}
searcher = GridSearchCV(linear_classifier, parameters, cv=10)
searcher.fit(X_train, y_train)

# Report the best parameters and the corresponding score
print("Best CV params", searcher.best_params_)
print("Best CV accuracy", searcher.best_score_)
print("Test accuracy of best grid search hypers:", searcher.score(X_test, y_test))
