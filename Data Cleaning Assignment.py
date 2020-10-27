import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',

'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

# Problem 1
df['FlightNumber']=df['FlightNumber'].interpolate().astype(int)

# Problem 2
From_to = df['From_To']
temp_df = pd.DataFrame([From_to[i].split('_') for i in range(len(From_to))], columns = ["From","To"])

# Problem 3
[r,c] = temp_df.shape
for i in range(r):
    for j in range(c):
        temp_df.iloc[i,j]=temp_df.iloc[i,j].capitalize()

# Problem 4        
df = df.drop(['From_To'], axis = 1)
df = pd.concat([temp_df,df], axis = 1)

# Problem 5
def array_sizer(array,max_size):
    new_array = np.empty(max_size)
    for i in range(len(array)):
        new_array[i] = array[i]
    for j in range(len(array),len(new_array)):
        new_array[j] = np.nan
    return new_array
    
no_of_rows = df.shape[0]
for i in range(no_of_rows):
    size_array[i]=len(df['RecentDelays'][i])

max_l = int(max(size_array))
new_array = np.empty([no_of_rows,max_l])
for i in range(no_of_rows):
    new_array[i,:] = array_sizer(df['RecentDelays'][i], max_l)

columns = ['delay_'+str(i) for i in range(1,max_l+1)]
delays = pd.DataFrame(new_array, columns = columns) 

df = df.drop(['RecentDelays'], axis = 1)

for i in range(delays.shape[1]):
    df.insert(3+i, columns[i], delays.iloc[:,i])
    
print(df)
    