#Merge dataframe medical_records & patient_details
import pandas as pd
d1=pd.read_csv("new_medical_records.csv")
df=pd.DataFrame(d1)
print("\n",df)

d2=pd.read_csv("new_patient_details.csv")
df=pd.DataFrame(d2)
print("\n",df)

#Merge both datasets
merged_inner=pd.merge(d1,d2,on='patient_id',how='inner')
print("\n",merged_inner)
#Save file
output_file = 'Merged_file.csv'
merged_inner.to_csv(output_file, index=False)