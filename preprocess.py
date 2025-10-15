import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

# URL for the Penguins dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv'
df = pd.read_csv(url).dropna()  # drop any missing values (very few)

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

# Save the clean data
df.to_csv('data/penguins_clean.csv', index=False)

# Load data
df = pd.read_csv('data/penguins_clean.csv')
print("Data loaded successfully, shape:", df.shape)

# Label Encoding 
le_species = LabelEncoder()
le_island = LabelEncoder()
le_sex = LabelEncoder()

df['species'] = le_species.fit_transform(df['species'])
df['island'] = le_island.fit_transform(df['island'])
df['sex'] = le_sex.fit_transform(df['sex'])
print("Label encoding done")