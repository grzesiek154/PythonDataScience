# Biuiding the model

## LinearSVC

```python
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

cancer_data = load_breast_cancer(as_frame = True)
cancer_df = cancer_data.data
cancer_df['target'] = cancer_data.target

X = cancer_df.drop(["target"], axis=1)
y = cancer_df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 417)

model = LinearSVC(penalty="l2", loss="squared_hinge", C=20, max_iter=3500, random_state=417)
model.fit(X_train, y_train)
```

Expalation

The code correctly loads the breast cancer dataset using `load_breast_cancer` function from `sklearn.datasets`. It then creates a pandas dataframe `cancer_df` from the dataset and adds a column `target` to it. The `target` column contains the target variable for the dataset.

The code then splits the dataset into training and testing sets using `train_test_split` function from `sklearn.model_selection`. It uses 85% of the data for training and 15% for testing.

Next, the code creates a LinearSVC model from `sklearn.svm` and fits it to the training data using the `fit` method. The model uses L2 regularization with a squared hinge loss function and a regularization parameter `C` of 20. It also sets the maximum number of iterations to 3500 and a random state of 417.

## Test accuracy of the model

```
model = LinearSVC(penalty="l2", loss="squared_hinge", C=20, max_iter=3500, random_state=417)
model.fit(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
print(test_accuracy)
```
