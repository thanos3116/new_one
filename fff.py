from faker import Faker
fake=Faker()
name=fake.name()
def names_list(x):
    names1=[]     
    for j in range(0,x):
        user={fake.name(),'Tamil','English','Maths'}
        names1.append(user)
        return names1

    
    
field=['names','subject1','subject2','subject3']
import csv
with open('fake_data.csv','w',newline='') as csvfile:
    csv_fake_data=csv.writer(csvfile)
    csv_fake_data.writerow(field)
    for i in names_list(4):
        csv_fake_data.writerow(i)
    