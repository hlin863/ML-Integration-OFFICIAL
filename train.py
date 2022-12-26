import pandas as pd 
# from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Set random seed
seed = 42

################################
########## DATA PREP ###########
################################

# Load in the data
df = pd.read_csv("wine_quality.csv")

# Randomize the data
df = df.sample(frac=1, random_state=seed).reset_index(drop=True)

# Split into train and test sections
y = df.pop("quality")

X = df

print("Y: ", y.head())

print("X: ", X.head())

# display the columns for X
print("X columns: ", X.columns)

# using indexing to select X_train as the first 80% of X
X_train = X[:int(0.8*len(X))]

y_train = y[:int(0.8*len(y))]

# using indexing to select X_test as the last 20% of X
X_test = X[int(0.8*len(X)):]

y_test = y[int(0.8*len(y)):]

# implement linear regression without sklearn library
class LinearRegression:

    def __init__(self, X, y):
        """
        
        Initialises the linear regression model by assigning the training data to the external parameters X and y.

        @param X: The training data
        @param y: The training labels

        """
        self.X = X
        self.y = y
        self.X_bar = self.meanX()
        self.Y_bar = self.meanY()

    def meanX(self):
        """
        
        Calculates the mean for the training data.

        @return: The mean of the training labels. 
        
        """
        return np.mean(self.X)
    
    def meanY(self):
        """
        
        Calculates the mean for the training labels.

        @return: The mean of the training labels.
        
        """

        return np.mean(self.y)

    def calculate_gradient(self):

        """
        
        This function calculates the gradient for the linear regression function.

        @return: The gradient of the linear regression function.

        """

        gradient = 0 # initialise gradient

        for i in range(len(self.X)): # for each data point

            gradient += (self.X[i] - self.X_bar) * (self.y[i] - self.Y_bar) / (self.X[i] - self.X_bar) ** 2 # gradient = (x - x^-) * (y - y^-) / (x - x^-) ** 2

        return gradient # return the gradient from the function. 
    
    def calculate_intercept(self):

        """
        
        Implement a function to calculate the y-intercept. 
        
        @return: The y-intercept of the linear regression function.

        """
        c = self.Y_bar = self.calculate_gradient() * self.X_bar # y-intercept = y^- - gradient * x^-

        return c # return the y-intercept from the function.
        
    def linear_regression(self, x_test):

        """
        
        Implements the linear regression function on the test data.

        @param x_test: The test data.
        
        """

        y_pred = []

        for i in range(len(x_test)): # for each data point

            y_pred.append(self.calculate_gradient() * x_test[i] + self.calculate_intercept()) # y = gradient * x + y-intercept

        return y_pred # return the predicted values from the function.

# #################################
# ########## MODELLING ############
# #################################

# # Fit a model on the train section
# regr = RandomForestRegressor(max_depth=2, random_state=seed)
# regr.fit(X_train, y_train)

# # Report training set score
# train_score = regr.score(X_train, y_train) * 100
# # Report test set score
# test_score = regr.score(X_test, y_test) * 100

# # Write scores to a file
# with open("metrics.txt", 'w') as outfile:
#         outfile.write("Training variance explained: %2.1f%%\n" % train_score)
#         outfile.write("Test variance explained: %2.1f%%\n" % test_score)


# ##########################################
# ##### PLOT FEATURE IMPORTANCE ############
# ##########################################
# # Calculate feature importance in random forest
# importances = regr.feature_importances_
# labels = df.columns
# feature_df = pd.DataFrame(list(zip(labels, importances)), columns = ["feature","importance"])
# feature_df = feature_df.sort_values(by='importance', ascending=False,)

# # image formatting
# axis_fs = 18 #fontsize
# title_fs = 22 #fontsize
# sns.set(style="whitegrid")

# ax = sns.barplot(x="importance", y="feature", data=feature_df)
# ax.set_xlabel('Importance',fontsize = axis_fs) 
# ax.set_ylabel('Feature', fontsize = axis_fs)#ylabel
# ax.set_title('Random forest\nfeature importance', fontsize = title_fs)

# plt.tight_layout()
# plt.savefig("feature_importance.png",dpi=120) 
# plt.close()


# ##########################################
# ############ PLOT RESIDUALS  #############
# ##########################################

# y_pred = regr.predict(X_test) + np.random.normal(0,0.25,len(y_test))
# y_jitter = y_test + np.random.normal(0,0.25,len(y_test))
# res_df = pd.DataFrame(list(zip(y_jitter,y_pred)), columns = ["true","pred"])

# ax = sns.scatterplot(x="true", y="pred",data=res_df)
# ax.set_aspect('equal')
# ax.set_xlabel('True wine quality',fontsize = axis_fs) 
# ax.set_ylabel('Predicted wine quality', fontsize = axis_fs)#ylabel
# ax.set_title('Residuals', fontsize = title_fs)

# # Make it pretty- square aspect ratio
# ax.plot([1, 10], [1, 10], 'black', linewidth=1)
# plt.ylim((2.5,8.5))
# plt.xlim((2.5,8.5))

# plt.tight_layout()
# plt.savefig("residuals.png",dpi=120) 