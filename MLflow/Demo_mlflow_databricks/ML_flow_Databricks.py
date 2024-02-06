# Databricks notebook source
# MAGIC %md
# MAGIC ####Select the Cluster Machine Learning cluster
# MAGIC ####anything above  11.3 LTS ML(Scala 2.12) above  

# COMMAND ----------

# MAGIC %md
# MAGIC ####MLfLow (mlflow is already PIP installed) as it is comminity edition we only have mlflow-skinny i.e. light version of MLflow

# COMMAND ----------

# MAGIC %pip list

# COMMAND ----------

# MAGIC %pip show mlflow-skinny

# COMMAND ----------

# DBTITLE 1,Modules Required
import mlflow
import mlflow.sklearn
import pandas as pd
import matplotlib.pyplot as plt
from numpy import savetxt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# COMMAND ----------

db = load_diabetes()
X = db.data
y = db.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# COMMAND ----------

# DBTITLE 1,Background of Train_Test_Split
train_test_split??

# COMMAND ----------

# MAGIC %md
# MAGIC #### Create a random forest model and log parameters, metrics, and the model using mlflow.sklearn.autolog().

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Ml_flow provide Python API

# COMMAND ----------

#Enable autolog
mlflow.sklearn.autolog()
# With autolog() enabled, all model parameters, a model score, and the fitted model are automatically logged.  

# COMMAND ----------

with mlflow.start_run():
  # Set the model parameters. 
  n_estimators = 100
  max_depth = 6
  max_features = 3
  
  # Create and train model.
  rf = RandomForestRegressor(n_estimators = n_estimators, max_depth = max_depth, max_features = max_features)
  rf.fit(X_train, y_train)
  
  # Use the model to make predictions on the test dataset.
  predictions = rf.predict(X_test)

# COMMAND ----------

# MAGIC %md
# MAGIC Records and maintain the version of Model for each run

# COMMAND ----------

# Classification Problem

# COMMAND ----------

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

# COMMAND ----------

db = load_iris()
X = db.data
y = db.target
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3 , random_state=50)

# COMMAND ----------

with mlflow.start_run(run_name="Classification Model"):
    #call the model
    Mdl=KNeighborsClassifier(n_neighbors=3)
    #fit the data
    Mdl.fit(X_train,y_train)
    #predict the test
    y_pred=Mdl.predict(X_test)

# COMMAND ----------
# Compare the Accuracy across the experiments
accuracy=accuracy_score(y_test,y_pred)
print(f'Accuracy: {accuracy}')

# COMMAND ----------


