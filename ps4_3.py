from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn import metrics

iris=datasets.load_iris()

X=iris.data
y=iris.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

clf=RandomForestClassifier(n_estimators=100)

clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

print(f"Accuracy Score :", accuracy_score(y_test, y_pred))



"""*********************************************************************************"""


feature_imp = pd.Series(clf.feature_importances_,index=iris.feature_names).sort_values(ascending=False)

sns.barplot(y=feature_imp, x=feature_imp.index)
print(feature_imp)
plt.xlabel('Features')
plt.ylabel('Feature Importance Score')
plt.title("Random Forest Feature Importances")
plt.show()


"""*********************************************************************************"""

# f test
from sklearn.feature_selection import f_classif

# Create f_classif object to calculate F-value
f_value = f_classif(X, y)
for feature in zip(iris.feature_names, f_value[0]):
    print(feature)


sns.barplot(y=f_value[0] ,x=iris.feature_names)


plt.ylabel('F-value')
plt.title('F-value Comparison')
plt.show()


"""*********************************************************************************"""

from sklearn.feature_selection import mutual_info_classif

# Create mutual_info_classif object to calculate mutual information
MI_score = mutual_info_classif(X, y)

# Print the name and mutual information score of each feature
for feature in zip(iris.feature_names, MI_score):
    print(feature)


# Create a bar chart for visualizing the mutual information scores
sns.barplot(y=MI_score ,x=iris.feature_names)
# plt.bar(height=MI_score,x=iris.feature_names)

plt.ylabel('Mutual Information Score')
plt.title('Mutual Information Score Comparison')

plt.show()



"""*********************************************************************************"""

X=iris.data[:,2:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Create a Gaussian Classifier
feature_clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

# prediction on test set
y_pred=clf.predict(X_test)


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

"""*********************************************************************************"""

