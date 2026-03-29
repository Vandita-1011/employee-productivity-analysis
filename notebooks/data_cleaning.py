import pandas as pd

df = pd.read_csv("data/employee_productivity.csv")

print(df.head())

df.rename(columns={
    'Hours_Worked_Per_Week': 'Work_Hours',
    'Projects_Completed': 'Tasks_Completed',
    'Performance_Rating': 'Quality_Score'
}, inplace=True)

print(df.columns)

df['Overtime'] = df['Work_Hours'].apply(lambda x: 'Yes' if x > 40 else 'No')

print(df[['Work_Hours', 'Overtime']].head())

df['Productivity_Index'] = (
    df['Tasks_Completed'] * 0.5 +
    df['Quality_Score'] * 0.5
)

df.to_csv("data/cleaned_employee_data.csv", index=False)

print("Cleaned dataset saved successfully!")