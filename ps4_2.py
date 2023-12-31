
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
# Reading the Iris.csv file
data = load_iris()

# Extracting Attributes / Features
X = data.data

# Extracting Target / Class Labels
y = data.target

# Import Library for splitting data
from sklearn.model_selection import train_test_split

# Creating Train and Test datasets
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 50, test_size = 0.2)

# Creating Decision Tree Classifier

for i in range(2,5):
        clf = DecisionTreeClassifier(criterion="entropy",max_depth=i,random_state=42)
        clf.fit(X_train,y_train)
        plot_tree(clf)
        # Predict Accuracy Score
        y_pred = clf.predict(X_test)
        print("Train data accuracy:",accuracy_score(y_true = y_train, y_pred=clf.predict(X_train)))
        print("Test data accuracy:",accuracy_score(y_true = y_test, y_pred=y_pred))

        plt.show()