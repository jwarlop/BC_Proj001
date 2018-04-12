# John M Warlop
# 4/07/18
# Python script to clean/reduce irs data
import csv
import pandas as pd 
import pickle

with open('irs_clean.csv','w') as o:
    with open('15zpallagi.csv','r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                o.write("ST,Zip,AGI,TtlR,TtlSR,TtlJR,Eld\n")
            else:
                o.write("{},{},{},{},{},{},{}\n".\
                    format(row[1],row[2],row[3],row[4],row[5],row[6],row[17]))
    f.close()
o.close()
df_irs = pd.read_csv('irs_clean.csv')
print(df_irs.shape)
df_irs.to_pickle('df_irs.pkl')
del(df_irs)
#check if pickled file reconstitutes itself as dataframe
df_irs=pd.read_pickle('irs_clean.pkl')
df_irs.head()