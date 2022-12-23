import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

#print(myclient.list_database_names())

#dblist = myclient.list_database_names()
#if "mydatabase" in dblist:
#    print("The database exists.")
#else:
#    print("Not Found")

mycol = mydb["customers"]
'''mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
'''
#x = mycol.insert_many(mylist)

#fx = mycol.find_one()
#for i in mycol.find():
#    print(i)
print(myclient.list_database_names())
#for x in mycol.find({},{"_id":0,"name":1,"address":1}):
#    print(x)
#for x in mycol.find({},{"address":0}):
#    print(x)
'''
q1 = {"name":"Amy"}
n1 = mycol.find(q1)
for i in n1:
    print(i)
q2 = {"address":{"$gt":"M"}}
n2 = mycol.find(q2)
for i in n2:
    print(i)
q3 = {"address":{"$regex":"8$"}}
n3 = mycol.find(q3)
for i in n3:
    print(i)
fx = mycol.find_one()
print(fx)'''
#new_record = {"_id":15,"name":"Naman","address":"Noida"}
#mycol.insert_one(new_record)
'''
mydoc = mycol.find().sort("_id",-1)
for i in mydoc:
    print(i)
'''
#q4 = {"name":"Vicky"}
#mycol.delete_one(q4)

prev = {"name":"Viola"}
new = {"$set":{"name":"Rachel","address":"Central Perk"}}
mycol.update_one(prev,new)
for x in mycol.find({},{"_id":0,"name":1,"address":1}):
    print(x)

result = mycol.find().limit(5)
for i in  result:
    print(i)