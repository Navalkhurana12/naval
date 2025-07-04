import re
passwords = ['Password123!', 'weakpass', 'Strong1@']
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
for pwd in passwords:
    print(pwd, '->', bool(re.match(pattern, pwd)))

print(bool(re.match(r"hello","hello world")))
print(re.findall(r"\d+","order 123 on 2024-07-01"))
text="welcome to python programing"
print(re.sub(r"\s","-",text))
print("question no 2")
import pandas as pd
date_range=pd.date_range(start="2023-06-09",periods=10,freq='D')
df=pd.DataFrame({'date':date_range})
print(df)
print(df['date'].dt.year)
print(df['date'].dt.month)
print(df['date'].dt.day_name())
print("question no 3")
import pandas as pd
import numpy as np
df =pd.read_csv("annual-enterprise-survey-2023-financial-year-provisional.csv")
print(df.describe())
gd=df.groupby('Year').count()
print(df.columns)

print(df['Year'])
print(gd)