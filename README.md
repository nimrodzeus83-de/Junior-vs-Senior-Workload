# Junior vs Senior Workload 
This is my summarization of all the reports that I did in this analysis between Junior Level and Senior Level Workloads.

# Background:
In this report, I used the data on the workloads of Junior and Senior employees and applied an Independent t-test. This statistical test is used to determine whether there is a significant difference between the mean workloads of two independent groups.

The purpose of this analysis is to compare the workloads of Junior and Senior employees and to determine whether the difference between them is statistically significant. Understanding workload differences is important for effective workforce management, operational efficiency, and sustainable team growth. It can help organizations identify potential issues such as employee burnout, excessive workload distribution, and unfair compensation that may not match employees' responsibilities.

To support my analysis, I used the bar chart as my graph analysis model in this study to show how the Junior and Senior Level became differ in terms of their workload rates by diffferentiating them using their average or mean. And the graph shows that Junior level has much higher but almost near to the Senior level which is suggested that they don't have much differences with their workloads and it is proven by our p-values below.

# Objective:
* The objective of this report is to analyze the significant differences of Junior and Senior Level Workload using the Independent paired T-test.

# Hypothesis:
* Null Hypothesis (H0)- There is no significant difference between the workload of Junior and Senior Employees.
* Alternative Hypothesis (HA)- There is a significant difference between the workload of Junior and Senior Employees.
* 
# Analysis and Findings:
* Junior Level - Mean: 3.046511627906977, Standard Deviation: 1.4193209658228474, Variance: 2.0144720040243005
* Senior Level - Mean: 2.9476145930776427, Standard Deviation: 1.3858117380870323, Variance: 1.9204741734198014
* Degree of Freedom: 1669
* T- Critical Value:  1.9613863711666333
* T-Statistics: 1.3883022853292168
* P-Value: 0.1652302835172021

Based on the number of P-Value which is higher than alpha level of 0.05, It is concluded that 
"There is no significant difference between the workload of Junior and Senior Employees", and when you look at the graph named "unpaired_analysis.png" of this report it is shown that Workload of Junior and Senior Level graph was almost overlapped to each other which is caused by the number of their workloads was the almost the same between Junior and Senior Job Level.

# Mean 
* A statistical measurement of central tendency that represents the mathetical center of the dataset and it is calculated by adding all the data points together and dividing the sum by the total number of points.

# Standard Deviation
*  It is a statistical measure that quantifies how spread out the values in a dataset are from the average (mean).

# Variance 
*  It is the measure of how much values in a data set differ or spread out from their average (mean).

# Degree of Freedom(df)
* It is represented as the number of independent values or parameters in a system that have the freedom to vary without viollating eastbalished constraints.
  
# T-Critical Value 
*A threshold that tell's the test whether to accept the null hypothesis(not significant) or  reject the null hypothesis(significant). 

# T-Statistics
* It  measures how different two group averages (means) of the variables are and a relative to the random noise in the data. It acts as a ratio of "signal" to "noise," where a higher absolute value indicates a more significant difference.

# P-Value 
* It measures the probability of your test experiment's whether it results happened by a random chance.
* Low p-value means "highly significant and unlikely to be a coincidence
* High p-value means "small chance to be true due to a random noise"

* File source: Kaggle.com, new_data.csv
* Tools used: VS Code, Python 
