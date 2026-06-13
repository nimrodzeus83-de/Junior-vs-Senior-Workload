import pandas as pd 
from scipy import stats 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 


df = pd.read_csv("employee.csv")
junior_level = df[df["JobLevel"] == "Junior"]["Workload"]
senior_level = df[df["JobLevel"] =="Senior"]["Workload"]
alpha = 0.05

degree_freedom = len(junior_level) + len(senior_level) - 2
t_critical = stats.t.ppf(1-alpha / 2, degree_freedom)

#print(junior_level.head(602))
#print(senior_level.head(1069))
t_statistics, p_value = stats.ttest_ind(junior_level, senior_level)
mean1, mean2 = junior_level.mean(), senior_level.mean()
sd1, sd2 = junior_level.std(), senior_level.std()
var1, var2 = junior_level.var(), senior_level.var()

print(f"Junior Level - Mean: {mean1}, Standard Deviation: {sd1}, Variance: {var1}")
print(f"Senior Level - Mean: {mean2}, Standard Deviation: {sd2}, Variance: {var2}")
print(f"Degree of Freedom: {degree_freedom}")
print(f"T-Critical value: {t_critical}")
print(f"T-Stat: {t_statistics}")
print(f"P-Value: {p_value}")
print("")

if p_value < alpha:
    print("There is a significant difference between the workload of Junior and Senior Employees")
    
else:
  print("There is no significant difference between the workload of Junior and Senior Employees")


sns.kdeplot(junior_level, label="Junior Level", fill=True)
sns.kdeplot(senior_level, label="Senior Level", fill=True)
plt.title(f"Distribution between Job level and Work Load of Employees",
          fontsize=15,
          fontweight="bold")

plt.tight_layout()

plt.xlabel("Workload",fontsize=15,fontweight="bold")
plt.ylabel("Frequency",fontsize=15,fontweight="bold")

plt.legend()
plt.savefig("unpaired_analysis.png")
plt.show(block=True)


