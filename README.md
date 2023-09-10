# NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets

# Question 1.
In this part, we used sklearn.dataset digits dataset. We split data into two parts which are training and testing part as a 20%. We used sklearn.neural_network MLPClassifier and random state =1.
## 1 Hidden Layer Results
### Hidden Layer Unit: 150

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/319b5041-f3ed-462f-ad7c-6a8d02229fd0" width="40%" >

### Accuracy
For Training Part is 1.0, For Testing Part is 0.978

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/f29320da-de54-486c-94e3-3efdd3482629" width="25%" >

### Hidden Layer Unit: 300
<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/f8d33005-2c51-4f82-8cf7-5517a0f786a2" width="40%" >

### Accuracy
For Training Part is 1.0, For Testing Part is 0.98

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/9cdeec3c-7443-4277-b517-8755d0c91d23" width="25%" >

## 2 Hidden Layer Results

### Hidden Layer Unit: 150,300
<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/e6ea35c5-83b2-4120-a43f-19e0a1717ff9" width="40%" >

### Accuracy
For Training Part is 1.0, For Testing Part is 0.9861

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/1d484d87-d36c-462f-af63-aa6234b75e81" width="25%" >


### Hidden Layer Unit: 300, 150
<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/248aec2a-3113-45d9-8721-0c4cc7f2264d" width="40%" >

### Accuracy
For Training Part is 1.0, For Testing Part is 0.994

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/c888bdf9-0fb3-4757-ae81-47dd04d3b5f6" width="25%" >


## Question 2.
In this part, we used sklearn.dataset iris dataset. We splitted data into two parts which are traning and testing part as a 20%. We used sklearn.tree DecisionTreeClassifier with a criterion Entropy, random state 42.

### For Max Tree Depth = 2
<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/804452a5-c6f2-4062-a1a0-7ddd8a47c27b" width="40%" >

### Accuracy
For Training Part is 0.95834, For Testing Part is 0.967

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/60093025-b4df-4f47-b3e8-c10a83dbbca2" width="30%" >

### For Max Tree Depth = 3
<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/5d9022b6-71df-4012-ad1f-9d0c4c9720e7" width="40%" >


### Accuracy
For Training Part is 0.983, For Testing Part is 0.967

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/adf40d01-b028-4554-9677-f49283d87789" width="30%" >


### For Max Tree Depth = 4
<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/575649c1-31b2-4e54-9d76-b05cd852bf94" width="40%" >

### Accuracy
For Training Part is 0.99167, For Testing Part is 0.967

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/5ed5a21d-a851-44c3-90c1-98744af7fe60" width="30%" >

## Question 3.
In this part, we used sklearn.dataset iris dataset. We splitted data into two parts which are traning and testing part as a 20%. We used sklearn.ensemble RandomForestClassifier with an estimator =100

### Random Forest Classifier Feature Selection
According to Forest Classifier Pedal Length and pedal width are important for Classification.

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/4e296a99-c8ff-4010-90ff-6dfd2d9ab230" width="40%" >

### Importance of Features
Petal Length 0.4953, Petal Width 0.3685

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/15f3e015-221c-47f1-9c08-a8344011f252" width="25%" >

### F-Value Comparison
According to F-Value Comparison Pedal Length and pedal width are highly important for Classification.

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/a4b6046d-c8e6-48d9-a01a-3a87d550e4e6" width="40%" >

### Importance of Features
Petal Length 1180.16, Petal Width 960.01.

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/eef62c9a-6128-49f2-88a0-0d8f3c2a665d" width="30%" >


### Mutual Information Score Comparison
According to Mutual Information Score Pedal Length, pedal width, and sepal length (even if less) are important for Classification.

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/1709e129-3985-4d95-b9bf-0b1bded6cff6" width="40%" >


### Importance of Features
Petal Length 0.9912, Petal Width 0.9964, and Sepal Length 0.5203.

<img src="https://github.com/onlinEngineer/NN-Decision-Tree-and-Random-Forest-Classifier-Iris-and-Digit-Datasets/assets/70773825/cb6ad048-fd5b-4afd-ac16-8b59daf67060" width="30%" >

### Results of Random Forest Classifier
When we used all features of the data, the accuracy has become 0.9. After that, according to three classifications, we drop the sepal length and sepal width since they do not important for classification.
When we use Random Forest Classifier again by using Pedal Length and Pedal Width, the accuracy has increased and become 0.967.

# CONCLUSION

In this Assignment, we learned what is multi-Layer classification, Random classification, Decision Tree, how we can apply this classification on given data etc.
For Multi-Layer Classification we used 1 and 2 hidden layer size and two different hidden layer which is 150 and 300 for 1 hidden layer, and two different layer unit which are 150,100 and 300,150 for 2 hidden layers. When we increase the hidden layer unit, the accuracy increased. Also, for layer size, the same things happening. However, the speed of classification is reducing when we increased the hidden units and layer. So that, to be more accurate and speed, we should the find out correct hidden layer and units.
For decision tree, we tried three different depth which are 2,3,4 and criterion “Entropy”. Once we increased the depth, the train data accuracy has increased, but the test data accuracy has not changed.
Finally, in last question we used Random Forest Classification. To detect the best feature for classification, we tried three different comparison that are Random Forest feature selection, f-value comparison, and mutual information score comparison. All the comparison algorithm gives us the same result. These results say that the most important features are pedal length and pedal width for classification. So that, if we use these features for classification, we can get better results. Therefore, we applied the random forest classification for all features and pedal length and pedal width as a two different classification and we get the different results. The result of all features is 0.9, the results of the two features is 0.967. Briefly, when we use two important features, the accuracy increased.
