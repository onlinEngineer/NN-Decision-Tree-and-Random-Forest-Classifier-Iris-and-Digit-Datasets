from mlxtend import classifier
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import numpy as np
from sklearn.model_selection import learning_curve



def mlp_Classifier(data,hidden_layer_size,hiddenUnit1,hiddenUnit2=100):


        X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.20,random_state=1)
        if hidden_layer_size ==1:
            mlp=MLPClassifier(hidden_layer_sizes=(hiddenUnit1,),random_state=1)

        else:
            mlp = MLPClassifier(hidden_layer_sizes=(hiddenUnit1,hiddenUnit2), random_state=1)

        mlp.fit(X_train, y_train)
        print("Training set score: %f" % mlp.score(X_train, y_train))
        print("Test set score: %f" % mlp.score(X_test, y_test))

        train_sizes, train_scores, test_scores = learning_curve(mlp, data.data, data.target, n_jobs=-1, verbose=0)
        train_scores_mean = np.mean(train_scores, axis=1)

        test_scores_mean = np.mean(test_scores, axis=1)


        plt.figure()
        if hidden_layer_size==1:
            plt.title(f"MLP Classifier, HL Size:{hidden_layer_size}, HL Unit:{hiddenUnit1}")
        else:
            plt.title(f"MLP Classifier, HL Size:{hidden_layer_size}, HL Unit:{hiddenUnit1},{hiddenUnit2}")

        plt.xlabel("Training examples")
        plt.ylabel("Score")
        plt.gca().invert_yaxis()

        # plot the average training and test score lines at each training set size
        plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")

        plt.legend(["Training score", "Cross-validation score"])
        plt.ylim(-.1, 1.1)
        plt.show()


if __name__ == '__main__':
    digits = datasets.load_digits()
    mlp_Classifier(digits,1,150)
    mlp_Classifier(digits,1,300)
    mlp_Classifier(digits,2,150,100)
    mlp_Classifier(digits, 2, 300, 150)
