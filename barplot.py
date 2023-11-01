import  seaborn as sns
import matplotlib.pyplot as plt

diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()
print(df.head())

#df["cut"].value_counts().plot.barh()
#plt.title("cut desgişkeni frenkasları")
#plt.show()
sns.barplot(x = "cut", y = df.cut.index,data =df)
plt.title("data f")
plt.show()