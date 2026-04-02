import pandas as pb

#load dataset
df = pb.read_csv("titanic.csv")

print(df.head())

# 1. How many passengers survived? (groupby Survived, count)
cnt = df.groupby('Survived').count()
print('Count of survived members: ',cnt)
print(df['Survived'].value_counts())
survied_count = (df['Survived']==1).sum()
print(survied_count)

# 2. What is the average age per passenger class (Pclass)?
avg_age = df.groupby('Pclass')['Age'].mean().reset_index(name='Avg_Age')
print(avg_age.to_string(index=False))

# 3. Filter: only female passengers who survived
survived_femals = df[(df['Sex']=='female') & (df['Survived']==1)]

print(survived_femals.head().to_string(index=False))

print(f"\nTotal No of survived:  {len(survived_femals)}")

# 4. Sort by Fare descending, show top 5
print(df.sort_values('Fare', ascending=False).head())

# 5. How many null values in the Age column?
cntnull=df['Age'].isnull().sum()
print(f"Ther are {cntnull} null in Age Column")