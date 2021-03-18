import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()
for column in columns:
  sns.countplot(df[column],order=df[column].value_counts().index)
  plt.xticks(rotation=30, fontsize=10)
  plt.xlabel(column, fontsize=12)
  plt.title(column + " Value Counts ")
  plt.show()
  plt.clf()
  #print(column)









