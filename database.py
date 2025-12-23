from pymongo import MongoClient
from config import MONGO_URI

mongo = MongoClient(MONGO_URI)
db = mongo['mega_bot']

fsub = db['fsub']
bans = db['bans']
warnings = db['warnings']
filters_db = db['filters']
locks = db['locks']
welcome_db = db['welcome']
rules_db = db['rules']
connections_db = db['connections']
