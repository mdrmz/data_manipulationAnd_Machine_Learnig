import seaborn as sns
from pandas.api.types import CategoricalDtype

diamonds = sns.load_dataset("diamonds")

df= diamonds.copy()

print(df.head())

print (df.info())
print()
print(df.describe().T)
print(df["cut"].value_counts())
cut_scatter = ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair']
print(df["cut"].astype(CategoricalDtype(categories= cut_scatter,ordered=True)))


print(df.cut.head(2))
