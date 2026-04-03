import pandas as pb

df = pb.read_csv('../titanic.csv')

print(df.head())
print("Total no of pasangers:",len(df))
servilcount = (df['Survived']==1)
print("Total no of servivers: ",servilcount.count())
print("Servival reate: ", df['Survived'].mean())
print("Avarage Age", df['Age'].mean())