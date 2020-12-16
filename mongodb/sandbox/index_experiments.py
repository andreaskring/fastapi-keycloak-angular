from pprint import pprint
import pymongo


DBNAME = 'experiments'

client = pymongo.MongoClient('mongodb://localhost:27017')
if DBNAME in client.list_database_names():
    client.drop_database(DBNAME)
db = client[DBNAME]
col_users = db['users']

users = [
    {
        'name': 'bruce',
        'canTeach': [
            {'name': 'kung fu'},
            {'name': 'karate'}
        ],
        'wantsToLearn': [
            {'name': 'cooking'},
            {'name': 'python'}
        ]
    },
    {
        'name': 'chuck',
        'canTeach': [
            {'name': 'judo'},
            {'name': 'karate'}
        ],
        'wantsToLearn': [
            {'name': 'cooking'},
            {'name': 'java'}
        ]
    },
    {
        'name': 'sylvester',
        'canTeach': [
            {'name': 'boxing'},
            {'name': 'survival'}
        ],
        'wantsToLearn': [
            {'name': 'java'},
            {'name': 'python'}
        ]
    },
    {
        'name': 'jean',
        'canTeach': [
            {'name': 'martial arts'},
            {'name': 'fighting'}
        ],
        'wantsToLearn': [
            {'name': 'boxing'},
            {'name': 'java'}
        ]
    }
]

r = col_users.insert_many(users)

# Documents examined without index

r = col_users.find({'canTeach.name': 'karate'}).explain()
print('totalDocsExamined:', r['executionStats']['totalDocsExamined'])

# Documents examined with index

col_users.create_index([('canTeach.name', 1)])
r = col_users.find({'canTeach.name': 'karate'}).explain()
print('totalDocsExamined:', r['executionStats']['totalDocsExamined'])

# Perform regex search

r = col_users.find({'canTeach.name': {'$regex': '^k'}})
for x in r:
    print(x)
