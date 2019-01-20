from SuvApp import db


'''
{ 
 "marital_status" : " Never-married", 
 "occupation" : " Adm-clerical", 
 "capital_loss" : 0,
 "sex" : " Male", 
 "capital_gain" : 2174,
 "class_type" : "<=50K", 
 "fnlwgt" : 77516,
 "education_num" : 13,
 "hours_per_week" : 40, 
 "native_country" : " United-States",
 "class" : " <=50K\n",
 "workclass" : " State-gov", 
 "education" : " Bachelors",
 "race" : " White", 
 "relationship" : " Not-in-family",
 "age" : 39 
 }
 
'''

##created a ORM connection
class survaider(db.Document):
    age = db.IntField()
    workclass = db.StringField(max_length=6000)
    fnlwgt = db.IntField()
    education = db.StringField(max_length=6000)
    education_num = db.IntField()
    marital_status = db.StringField(max_length=6000)
    occupation = db.StringField(max_length=6000)
    relationship = db.StringField(max_length=6000)
    race = db.StringField(max_length=6000)
    sex = db.StringField(max_length=6000)
    capital_gain = db.IntField()
    capital_loss = db.IntField()
    hours_per_week = db.IntField()
    native_country = db.StringField(max_length=6000)
    class_type = db.IntField()