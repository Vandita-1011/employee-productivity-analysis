import pandas as pd
from scipy.stats import pearsonr, ttest_ind, f_oneway

df = pd.read_csv('../data/cleaned_employee_data.csv')

print("1. CORRELATION ANALYSIS")
corr_coef, p_value_corr = pearsonr(df['Work_Hours'], df['Productivity_Index'])
print(f"Pearson Correlation (r): {corr_coef:.3f}")
print(f"P-value: {p_value_corr:.5f}\n") 

print("2. HYPOTHESIS TESTING (T-TEST)")
normal_group = df[df['Overtime'] == 'No']['Productivity_Index']
overtime_group = df[df['Overtime'] == 'Yes']['Productivity_Index']

t_stat, p_value_t = ttest_ind(normal_group, overtime_group)
print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_value_t:.5f}\n")

print("3. VARIANCE ANALYSIS (ANOVA)")
def categorize_hours(hours):
    if hours < 35:
        return 'Part-Time'
    elif 35 <= hours <= 45:
        return 'Normal'
    else:
        return 'Heavy Overtime'

df['Hours_Category'] = df['Work_Hours'].apply(categorize_hours)

part_time = df[df['Hours_Category'] == 'Part-Time']['Productivity_Index']
normal = df[df['Hours_Category'] == 'Normal']['Productivity_Index']
heavy_overtime = df[df['Hours_Category'] == 'Heavy Overtime']['Productivity_Index']

print(f"   - Part-Time (<35 hrs): {len(part_time)} employees | Avg Productivity: {part_time.mean():.2f}")
print(f"   - Normal (35-45 hrs): {len(normal)} employees | Avg Productivity: {normal.mean():.2f}")
print(f"   - Heavy Overtime (>45 hrs): {len(heavy_overtime)} employees | Avg Productivity: {heavy_overtime.mean():.2f}\n")

f_stat_hours, p_value_anova_hours = f_oneway(part_time, normal, heavy_overtime)
print(f"F-statistic: {f_stat_hours:.3f}")
print(f"P-value: {p_value_anova_hours:.5f}\n")