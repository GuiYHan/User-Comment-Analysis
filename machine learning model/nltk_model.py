"""
dependecy: scipy, scikit-learn, nltk

80% training set
20% test set

"""
import nltk
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC


class MLModel(object):
    def __init__(self):
        self.training_set = [({"you":2, "hate":1}, "negative"), ({"like":2, "LIKE": 2, "rating":3}, "positive")]
        self.testing_set = [({"comment":4, "rating":10},"2")]

    def train_different_model(self):
        training_set = self.training_set
        testing_set = self.testing_set

        MNB_classifier = SklearnClassifier(MultinomialNB())
        MNB_classifier.train(training_set)
        print "MultinomialNB accuracy percent:", nltk.classify.accuracy(MNB_classifier, testing_set)

        BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
        BernoulliNB_classifier.train(training_set)
        print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

        LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
        LogisticRegression_classifier.train(training_set)
        print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

        SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
        SGDClassifier_classifier.train(training_set)
        print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

        LinearSVC_classifier = SklearnClassifier(LinearSVC())
        LinearSVC_classifier.train(training_set)
        print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

        NuSVC_classifier = SklearnClassifier(NuSVC())
        NuSVC_classifier.train(training_set)
        print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

    def predict(self, list_obj):
        # example: [{"comment":4, "rating":10},{"comment":4, "rating":10}]
        return NuSVC_classifier.classify_many(list_obj)

