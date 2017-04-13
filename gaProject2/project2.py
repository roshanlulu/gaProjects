# Import standard modules
import numpy as np
import scipy.stats as stats
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1 Load the sat_scores.csv dataset and describe it
# 1.1 Load the file with the csv module and put it in a Python dictionary

# Load file with a csv module
sat_csv = []
with open('./sat_scores.csv', 'r') as sat_score:
    reader = csv.reader(sat_score)
    for row in reader:
        sat_csv.append(row)

sat_score.close()
header = sat_csv[0]
rows = sat_csv[1:]

# Put file contents into a dictionary
# Code to convert data read with help of csv reader to dictionary
sat_dict = {col:[row[index] for row in rows]    for index, col in enumerate(header)}
print(sat_dict)

# Code to convert dataframe read with help of pandas to a dictionary
# [sat_dict.update({column:sat_df[column].tolist()}) for column in sat_df.columns]

# 1.2 Make a pandas DataFrame object with the SAT dictionary, and another with the pandas .read_csv() function
sat_dict_df = pd.DataFrame(sat_dict)
sat_df = pd.read_csv('./sat_scores.csv')

print('\nDatatypes - Dictionary dataframe\n', sat_dict_df.dtypes)
print('\nDatatypes - Csv dataframe\n',   sat_df.dtypes)

# 1.3 Look at the first ten rows of the DataFrame: what does our data describe?
print(sat_df.head(10))
print(sat_df)
print('Describe data\n', sat_df.describe())

# 2. Create a "data dictionary" based on the data

# Convert the data types to a dictionary format and add the shape of the dataset
sat_data_dict = (sat_df.dtypes.apply(lambda x: {'Data type':x.name} ).to_dict())
sat_data_dict.update({'Shape':sat_df.shape})
# Add Description to the column name values
sat_txt_desc = ['State for which SAT scores are noted', 'Average Percentage', 'Verbal Section Scores', 'Math Section Scores', '(Rows, columns) of the dataset']
[sat_data_dict.update({key:[sat_data_dict[key], {'Description':text}]})
                for key, text in zip(sat_data_dict, sat_txt_desc)]

print('\nThe data dictionary of SAT scores dataset is: \n')
# Print data dictionary
for key, value in sat_data_dict.items():
    print(key, ' : ', value)

# 3. Plot the data using seaborn
# rate = pd.Series(sat_df['Verbal'].values, name = 'Rate', index = sat_df['Verbal'])
sns.distplot(sat_df['Rate'], bins = 7, kde = False, color = 'r', vertical = False)
sns.distplot(sat_df['Verbal'], bins = 7, kde = False, color = 'g', vertical = False)
sns.distplot(sat_df['Math'], bins = 7, kde = False, color = 'orange', vertical = False)

sns.pairplot(sat_df)
plt.show()
