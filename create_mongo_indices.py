import pymongo
DATABASE = "waitercaller"
account = "ecloud"
password = "ecloud123"
client = pymongo.MongoClient(['123.56.21.248'], port=27017)
db = client[DATABASE]
db.authenticate(account, password)
print(db.users.create_index("email", unique=True))
print(db.requests.create_index("table_id", unique=True))
