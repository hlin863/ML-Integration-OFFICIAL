# Import the necessary modules
# module to create a random forest classifier
from sklearn.ensemble import RandomForestClassifier
# module to split the data into training and testing sets
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris  # module to load the iris dataset

# Load the iris dataset
iris_data = load_iris()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    iris_data.data, iris_data.target, test_size=0.2, random_state=0)  # X_train and y_train are the training data and labels, while X_test and y_test are the testing data and labels.

# Create a random forest classifier with 100 trees
clf = RandomForestClassifier(n_estimators=100)

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Test the classifier on the testing data
score = clf.score(X_test, y_test)

# Print the accuracy score of the classifier
print("The model accuracy is: ", score)
