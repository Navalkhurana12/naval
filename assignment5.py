import pandas as pd
data={
    "naval":[23,4,5],
    "nitesh":[9,3,4],
    "khurana":[3,54,5]
}
df=pd.Series(data)
print(df)
data1=[2,3,4,5]
dff=pd.Series(data1)
print(dff)
print(dff[0])

print("question no 2")
no={
"naval":[23,4,5],
    "nitesh":[9,3,4],
    "khurana":[3,54,5]
}
d=pd.DataFrame(no,index=["a","b","c"])
print(d)
no1=[2,3,4,5]
d1=pd.DataFrame(no1)
print(d1)
print()
n1=[[1,2,3],[34,43,5],["a","b"]]
d2=pd.DataFrame(n1)
print(d2)
print()
k1=[(1,2,4),(8,8,9),(89,8,67)]
d3=pd.DataFrame(k1)
print(d3)
k3=[
    {
        "naval":[3,5,4],
        "kka":[34,65,4],
        "kaju":[87,5,4]
    },
    {
"naval":[3,5,4],
        "kka":[34,65,4],
        "kaju":[87,5,4]
    }
]
d5=pd.DataFrame(k3)
print(d5)
print("question 3")
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

# Using iterrows()
for index, row in df.iterrows():
    print(row['Name'], row['Age'])

# Using itertuples()
for row in df.itertuples():
    print(row.Name, row.Age)
result = df[df['Age'] >= 25]
print(result)
print(df.iloc[1])
print()
print(df['Name'].head(2))
print()
df_filtered = df[df['Age'] >= 30]
print(df_filtered)
print()
row_list = df.to_dict(orient='records')
print(row_list)