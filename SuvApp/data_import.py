from pymongo import MongoClient

def insertdata(df):
    client = MongoClient('localhost')
    db = client.test
    db.survaider.insert_many(df)

'''
{ 
 "marital_status" : "Never-married", 
 "occupation" : "Adm-clerical", 
 "capital_loss" : 0,
 "sex" : " Male", 
 "capital_gain" : 2174,
 "class_type" : "<=50K", 
 "fnlwgt" : 77516,
 "education_num" : 13,
 "hours_per_week" : 40, 
 "native_country" : "United-States",
 "class" : " <=50K",
 "workclass" : "State-gov", 
 "education" : "Bachelors",
 "race" : "White", 
 "relationship" : "Not-in-family",
 "age" : 39 
 }
 
'''


file = open("adult_data.txt", "r")
data_list =[]
for i in file:
    data_list.append(
          {
            'age': int(i.split(',')[0].strip()),
            'workclass' : i.split(',')[1].strip(),
            'fnlwgt' : int(i.split(',')[2].strip()),
            'education': i.split(',')[3].strip(),
            'education_num': int(i.split(',')[4].strip()),
            'marital_status': i.split(',')[5].strip(),
            'occupation': i.split(',')[6].strip(),
            'relationship' : i.split(',')[7].strip(),
            'race' : i.split(',')[8].strip(),
            'sex' : i.split(',')[9].strip(),
            'capital_gain' : int(i.split(',')[10].strip()),
            'capital_loss' : int(i.split(',')[11].strip()),
            'hours_per_week' : int(i.split(',')[12].strip()),
            'native_country' : i.split(',')[13].strip(),
            'class_type' : i.split(',')[14].strip()

          }
       )


insertdata(data_list)

