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

print(f"Degree of Freedom: {degree_freedom}")
print(f"T-Critical value: {t_critical}")
print(f"T-Stat: {t_statistics}")
print(f"P-Value: {p_value}")
print("")

if p_value < alpha:
    print("Reject H0")
    print("There is a significant difference between the workload of Junior and Senior Employees")
    
else:
  print("Failed to reject H0")
  print("There is no significant difference between the workload of Junior and Senior Employees")

sns.kdeplot(junior_level, label="Junior Level", fill=True)
sns.kdeplot(senior_level, label="Senior Level", fill=True)
plt.title(f"Distribution between Job level and Work Load of Employees")
plt.tight_layout()
plt.xlabel("Workload")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("unpaired_analysis.png")
plt.show(block=True)

