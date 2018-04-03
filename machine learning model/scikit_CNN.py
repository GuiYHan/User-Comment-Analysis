"""
Reference: # http://scikit-learn.org/stable/modules/neural_networks_supervised.html

Sample usage:

A = CNNModel()
train_X = [[0., 0.], [1., 1.]]
train_y = [0, 1]

#To test the performace:
test_X = [[[2., 2.], [-1., -2.]]
test_y = [1,0]
A.performace(test_X, test_y)


#If you want to have a predict on some sample.
print A.predict([[2., 2.], [-1., -2.]])

#if you want to show some wrongly classified data:
N/A
"""



from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score, accuracy_score
import time
class CNNModel(object):
    def __init__(self):

        # hiddenlayer size
        # (10,10,10) if you want 3 hidden layers with 10 hidden units each
        # 2 sample constuct: (25,11,7,5,3,), (45,2,11,)
        self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                     hidden_layer_sizes=(25, 11, 7, 5, 3, ), random_state=1)
        self.start_t = 0
        self.end_t = 0

    def train(self, train_X, train_y):
        self.start_t = time.time()
        # format X: [[0., 0.], [1., 1.]], y:  [0, 1]
        self.clf.fit(train_X, train_y)
        self.end_t = time.time()

    def predict(self, input_X):
        # [[2., 2.], [-1., -2.]]
        result = self.clf.predict(input_X)
        return result

    def performace(self, test_X, test_y):
        # input as same as train model.
        y_predict = self.clf.predict(test_X)
        y_real = test_y

        print "#######    Pulling Out Satistics   ##################"
        print "Training time: {} seconds".format(self.end_t - self.start_t)
        print "F1 Score: ", f1_score(y_real, y_predict, average="weighted")
        print "Accuracy : {}%".format(int(accuracy_score(y_real, y_predict) * 100))












