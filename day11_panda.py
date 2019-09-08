import pandas as pd
data=pd.read_csv('test.csv')#to read hre csv data
'''print(data)
print(type(data))#Data frame allow us to imprt tabular data
print(data.columns.values)
print(data['Student'])#THis will only print the values in the column
print(data,'\n','-'*100)'''
#print(data[['Student','Maths','Physics']])#multiple column with column name
#data=data.fillna(0)
#print(data)
data['total']=data['Physics']+data['Chemistry']+data['Maths']
#print(data)
data=data.dropna()#This will delete all the rows with missing values
#print(data)
#print(data[data['total']>200])
total_mt_200=data[data['total']>200]
mt_80_in_mat_and_phy=data[(data['Maths']>80)&(data['Physics']>80)]
print(mt_80_in_mat_and_phy)
print(data[(data['Maths']>80)&(data['Physics']>80)][["Student","total"]])#Conditional Data Extraction
print(data["Student"].tolist())#create a list of all the student ID in the data frame
data=data.drop(["Maths","Physics"],axis=1)
print(data)
print(data['total'].sum())
#ROW SUM???
print(len(data['Student']))
data['Chem_Result']=data['Chemistry'].apply(lambda x:"Fail" if x<35 else "Pass")#Boolean type funnctions in the data frame
print(data)
data.to_csv('abc.csv')
