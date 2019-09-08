import pandas as pd
data=pd.read_csv('Berkeley.csv')
admitted=data[data["Admit"]=="Admitted"]
print(admitted)
perc_admit=(len(admitted)/len(data["Admit"]))*100
perc_reject=100-perc_admit
print(perc_admit)
print(perc_reject)
male_admitted=data[(data["Gender"]=="Male")&(data["Admit"]=="Admitted"])]
