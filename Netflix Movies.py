import zipfile
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Define the path to the zip file and the extraction directory
zip_file_path = r"C:\Users\Beacon Consulting\Downloads\netflix_data.zip"
extraction_path = 'Netflix_shows_movies'

# Create a directory if it doesn't exist
os.makedirs(extraction_path, exist_ok=True)

# Unzip the dataset
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_path)

df = pd.read_csv('Netflix_shows_movies/netflix_data.csv')
# Check for missing values
missing_values = df.isnull().sum()
# Fill missing values or drop them as appropriate
df['rating'] = df['rating'].fillna('TV-MA')  # Direct assignment
df.dropna(subset=['duration'], inplace=True)  # Drop rows where 'duration' is NaN

# Describe the dataset
description = df.describe()

# Explore value counts for categorical variables
genre_counts = df['listed_in'].value_counts()
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='listed_in', order=df['listed_in'].value_counts().index)
plt.title('Most Watched Genres')
plt.xlabel('Number of Shows/Movies')
plt.ylabel('Genres')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='rating', order=df['rating'].value_counts().index)
plt.title('Ratings Distribution')
plt.xlabel('Ratings')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()