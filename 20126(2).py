import pandas as pd
d=pd.read_csv("patient_details.csv")
df=pd.DataFrame(d)
print(df)
print()

#Checking Null values
print(df.isnull().sum())

#Fill Null values
#Handle Name
df['name'] = df['name'].fillna('Unknown')

# Handle Age:
#df['age'] = df['age'].abs()
age_median = df['age'].median()
df['age'] = df['age'].fillna(age_median)
print("\n",df)
print(df.isnull().sum()) 

#Find Outliers
print("\n",df['gender'].value_counts())
print("\n",df['height_cm'].value_counts())

#Replace Values
#(i)
print("\n",df['gender'].replace('Male','M',inplace=True))
print("\n",df['gender'].replace('Female','F',inplace=True))
print("\n",df['gender'].value_counts())

#(ii)
df['height_cm'] = pd.to_numeric(df['height_cm'], errors='coerce')
height_median = df['height_cm'].median()
df['height_cm'] = df['height_cm'].fillna(height_median)
print("\n",df)
print(df['height_cm'].value_counts())

#Convert City name to upperclass
df['city'] = df['city'].str.title()
print("\n",df)

#DateTime Format
df['admission_date'] = pd.to_datetime(df['admission_date'], format='mixed')
print("\n",df)

#Duplicates
print("Dup_Val.",df.duplicated().sum())
print(df.drop_duplicates(inplace=True))
print("\n",df)

#Cleaned file save
output_file = 'new_patient_details.csv'
df.to_csv(output_file, index=False)