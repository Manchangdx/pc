from pymongo import MongoClient

client = MongoClient('localhost', 27017)

l = [{
 'user_id': 1000,
 'name': 'Shiyan',
 'pass': 10,
 'study_time': 50,
},
{
 'user_id': 2000,
 'name': 'Lou',
 'pass': 15,
 'study_time': 171,
}]

col = client.louplus.users
col.insert_many(l)
