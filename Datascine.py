import  seaborn as sns
import pandas as pd


planets = sns.load_dataset("planets")
print(planets.head())

df=planets.copy()
print(df.info())
print(df.dtypes)

a = df.method = pd.Categorical(df.method)
print(a)
print(df.shape)
print(df.describe().T)

# hiç eksik gözlem varmı diye kontrol ediyoruz
print(df.isnull().values.any())

# eksik gözlem yapılan yerleri göster
print(df.isnull().sum())
print( "/////////////////////////////////////")
# bu durumu düzeletmek için yani sıfırımlak için
print(df["orbital_period"].fillna(0,inplace= True))
print(df.isnull().sum())
# bunun dışında  oralama degeri vermek için şuda kullanılır
print(df["mass"].fillna(df.mass.mean(),inplace= True),"\n")
print(df.isnull().sum(),"\n")
#veri seti içindeki tüm bilinmzeleri gidermek için hepsine ortalmayadı atabiliriz bunu içinde
#print(df.fillna(df.mean(),inplace= True))

