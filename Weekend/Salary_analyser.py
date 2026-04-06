import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mp

url = "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"

df = pd.read_csv(url)

#data cleaning
df = df.drop_duplicates()
df=df.dropna()

df.columns= df.columns.str.strip().str.lower()

#understaing data set
print(df.info())
print(df.describe())
print(df.columns)

#replace
df["commission_pct"] = df["commission_pct"].replace('-',np.nan)

#convert to numiric
df["commission_pct"] = pd.to_numeric(df["commission_pct"], errors="coerce")

#converting salary to numric
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

print(df.head())

#data handling
df["hire_date"] = pd.to_datetime(df["hire_date"], format="%d-%b-%y")
#adding exp column
df["exprience"]=(pd.Timestamp.now() - df["hire_date"]).dt.days //365

#salary category
df["salary_category"]=np.where(df["salary"]>10000,"High", "Low")
#commision flag
df["has_commission"] = np.where(df["commission_pct"].notna(),1,0)

#top 5 highly paid employees
top_paid = df.sort_values(by="salary", ascending=False).head(5)
print(top_paid[["first_name", "salary"]])

#avarage salary for dep
dept_Avg=df.groupby("department_id")["salary"].mean()
print(dept_Avg)

#manager wise team size
tem_size=df.groupby("manager_id")["department_id"].count()
print(tem_size)


#salary by department
dept_Avg.plot(kind="bar")
plt.title("Avarage salary by department")
plt.xlabel("dempatment_id")
plt.xlabel("salary")
plt.show()

#recent hires in last 2 years
recent = df[df["hire_date"] > pd.Timestamp.now() - pd.DateOffset(years=2)]
print("recent hires :", recent)


#Report Generation
with open("recent.txt", "w") as f:
    f.write("Employee Salary Analysis\n")
    f.write("========================\n\n")

    f.write(f"Total Employees: {len(df)}\n")
    f.write(f"Average Salary: {df['salary'].mean()}\n")
    f.write(f"Max salary: {df['salary'].max()}\n\n")

    f.write("Top 5 Highest Paid:\n")
    f.write(str(top_paid[["first_name", "salary"]]))

# #numpy creating new column
# df["salary_in_hike"] = np.round(df["salary"]/100000,2)
#
# #expreince bucket
# df["expreience_level"] = np.where([df[E]])
#
