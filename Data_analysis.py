import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import scipy.stats as stats
import statsmodels.stats.multicomp as ssm
import researchpy as rp

alpha = 0.05

dataA = [70, 50, 90, 55, 77, 90, 85, 76, 85, 86]
dataB = [98, 91, 84, 87, 78, 75, 81, 56, 66, 89]
dataC = [80, 90, 88, 78, 71, 75, 74, 69, 82, 78]
dataD = [80, 90, 88, 75, 74, 88, 85, 81, 73, 90]
dataE = [78, 81, 71, 91, 87, 82, 88, 95, 94, 73]

data_dict = {'dataA':dataA, 
             'dataB':dataB, 
             'dataC':dataC, 
             'dataD':dataD, 
             'dataE':dataE,}
# 創建一個空的 DataFrame
data_df = pd.DataFrame(data_dict)
data_summary = rp.summary_cont(data_df)
data_melt = data_df.melt(value_name='Score', var_name='Class')
print(data_df)
print()
print(data_summary)
print()
print(data_melt)
print()
print(data_df.describe())
print()
# Normal Distribution test:
for i in data_df.columns:
    statistic, p_value = stats.shapiro(data_df[i])
    print(f"shapiro of {i} :\nstatistic:{statistic:.2f}, p_value:{p_value:.2f}")
    if p_value > 0.05:
        print(f"The {i} is Normal distritubtion")
    else:
        print(f"The {i} is Not Normal distribution")
    print()
print()

# Homogenity of Variance test:
for j in data_df:
    statistic_1, p_value_1 = stats.levene(*[data_df[col] for col in data_df.columns])
print(f"Homogenity of Data :\nstatistic:{statistic_1:.2f}, p_value:{p_value_1:.2f}")    
if p_value_1 > 0.05:
    print(f"These data are Homogenity of Variance")
else:
    print(f"These data are Not Homogenity of Variance")
print()

# Anove of test:
for k in data_df:
    F_statistic, p_value_2 = stats.f_oneway(*[data_df[col] for col in data_df])
print(f"Anova of data :\nF-statistic{F_statistic:.2f}, p_value:{p_value_2:.2f}")
if p_value_2 > 0.05:
    print(f"These data are different")
else:
    print(f"These data are Not different")
print()

# TukeyHSD:
data_melt = data_df.melt(value_name='Score', 
                         var_name='Class')
mc = ssm.MultiComparison(data_melt['Score'], 
                         data_melt['Class'])
Result = mc.tukeyhsd()
print(data_melt)
print()
print(Result)

print()

# Get the data information:
data_Mean = list(data_summary['Mean'])
data_SE = list(data_summary['SE'])
data_Group = list(data_summary['Variable'])
data_error = [0 if e > 0 else -e for e in data_SE]

# figure:

plt.bar(data_Group, 
        data_Mean, 
        yerr = [data_error, data_SE], 
        alpha = 0.5,
        align = 'center', 
        capsize = 10, 
        hatch = '///', 
        edgecolor = 'black', 
        linewidth = 1, 
        )
plt.xticks(rotation = 40)
plt.title('Score')
plt.xlabel('Class')
plt.ylabel('Score')
plt.show

print(data_SE)