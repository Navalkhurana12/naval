import pandas as pd
date=pd.Series(['23-4-25','24-4-25','25-3-25'])
timeseries=pd.to_datetime(date)
print(timeseries)
print("question no 2")
data1={
    'id':[1,2,3,4],
    "name":["a","b","c","d"],
     'sub':["e","h","p","u"],

}
df1=pd.DataFrame(data1)
data2={
    'id':[1,2,3,4],
    "name":['r','g','h','d'],
    'sub':['d','j','f','c']
}
df2=pd.DataFrame(data2)
result=pd.merge(df1,df2,on='id',how='inner')
print(result)
result1=pd.merge(df1,df2,on='id',how='left')
print(result1)
result2=pd.merge(df1,df2,on='id',how='right')
print(result2)
df2_indexed = df2.set_index('id')
df1_indexed = df1.set_index('id')



print("question no 3")
dfA = pd.DataFrame({'ID': [1, 2], 'Value': ['A', 'B']})
dfB = pd.DataFrame({'ID': [3, 4], 'Value': ['C', 'D']})
dfC = pd.DataFrame({'ID': [2, 3, 4], 'Score': [91, 85, 77]})

df_AB = pd.concat([dfA, dfB])
print("Concatenated:\n", df_AB)
final = pd.merge(df_AB, dfC, on='ID', how='left')
print("Final Merged:\n", final)

