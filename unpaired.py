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

df_filtered = df[df["JobLevel"].isin(["Junior", "Senior"])]


workload_mean = (
    df_filtered
    .groupby("JobLevel")["Workload"]
    .mean()
)

ax = workload_mean.plot(
    kind="bar",
    figsize=(8, 6)
)

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.2f",
        fontsize=10,
        fontweight="bold"
    )

plt.title(
    "Average Workload by Job Level",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel(
    "Job Level",
    fontsize=12,
    fontweight="bold"
)

plt.ylabel(
    "Average Workload",
    fontsize=12,
    fontweight="bold"
)

plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show(block=True)


