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