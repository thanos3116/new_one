from faker import Faker
import random
fake=Faker()
name=fake.name()
def names_list(x):
    names1=[]     
    for j in range(0,x):
        user=[fake.name(),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
        names1.append(user)
    return names1
  
    
field=['names','tamil','english','maths']
import pandas as pd

df=pd.read_csv('fake_data.csv')
df['sum']= df['tamil']+df['english']+df['maths']
df[['tamil_percentage', 'english_percentage', 'maths_percentage']] = round(df[['tamil', 'english', 'maths']].apply(lambda x: (x/x.sum())*100, axis=1),2)
df["average"]=(df[['sum']].apply(lambda x: x/3, axis=1))

print(df.to_string())
