import pandas as pd
data=pd.read_csv("medical_records.csv")
df=pd.DataFrame(data)
print(df)
print()

#Checking Null values
print(df.isnull().sum())

#Fill Null values 
sugar_median=df['sugar_level'].median()
df['sugar_level']=df['sugar_level'].fillna(sugar_median)
print(df)
print(df.isnull().sum())
print()

#check outliers
print(df['bp'].value_counts())
print()

#Relace high as 140/90
df['bp'].replace('high','140/90',inplace=True)
print("\n",df)

print(df['bp'].value_counts())

#Average diagnosis cost
print(df.groupby('diagnosis')['visit_cost'].mean())

#Cleaned file save
output_file = 'new_medical_records.csv'
df.to_csv(output_file, index=False)
