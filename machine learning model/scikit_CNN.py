# http://scikit-learn.org/stable/modules/neural_networks_supervised.html

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score, accuracy_score
import time
class CNNModel(object):
    def __init__(self):
        self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                     hidden_layer_sizes=(5, 2), random_state=1)
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

#A = CNNModel()
#A.train([[0., 0.], [1., 1.]], [0, 1])
#print A.predict([[2., 2.], [-1., -2.]])
#A.performace([[2., 2.], [-1., -2.]],[1,0])











