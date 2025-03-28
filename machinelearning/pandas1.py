# Create a DataFrame with 3 columns: "Name", "Age", and "Salary" with 5 random records.

# Load the "titanic.csv" dataset (you can download it online).

# Display the first 10 rows of the dataset.

import pandas as pd

data = {'Name':['Hanzala','Aziz','Bilal','Uzair','Hamza'],'Age':[25,30,21,24,28],'Salary':['10','11','10','45','67']}

df = pd.DataFrame(data)

print(df.head(3))


titanic = pd.read_csv('titanic.csv')

print(titanic.head(10))