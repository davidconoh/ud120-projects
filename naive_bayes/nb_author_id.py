#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ train, predict labels and compute 
    the accuracy of your Naive Bayes classifier """

    print()
    print("Classifier: GaussianNB")
    # import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    # create classifier
    clf = GaussianNB() #TODO

    # fit the classifier on the training features and labels
    t0 = time()
    clf.fit(features_train, labels_train) #TODO
    print "training time:", round(time()-t0, 3), "s"

    # predict labels for the test features
    t1 = time()
    pred = clf.predict(features_test) #TODO
    print "prediction time:", round(time()-t1, 3), "s"

    import collections
    counter = collections.Counter(pred)
    print "no. of emails predicted Chris': "+str(counter[1])
    print "no. of emails predicted to be Sara's:"+str(counter[0])

    # calculate and return the accuracy on the test data
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(pred, labels_test)
    print accuracy
    print()
#########################################################

NBAccuracy(features_train, labels_train, features_test, labels_test)

