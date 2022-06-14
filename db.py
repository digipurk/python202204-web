from pymongo import MongoClient
from dateutil.parser import parse

CONNECT_STRING = 'mongodb+srv://dbuser:dbuser@cluster0.shazi.mongodb.net/?retryWrites=true&w=majority'

def get_database():
    client = MongoClient(CONNECT_STRING)
    return client['python202204-web']

if __name__ == '__main__':
    with open('rannailm.csv', encoding = 'UTF-8') as file:
        dbclient = get_database()
        collection = dbclient['rand']
        i = 0
        for row in file:
            if i > 0:
                cells = row.strip().split(';')
                existing = collection.find_one({'nimi': cells[0]})
                if existing is None:
                    rand = {
                        'nimi': cells[0],
                        'kuupaev': parse(cells[1] + ' ' + cells[2]),
                        'ohk': int(cells[3]),
                        'vesi': int(cells[4]),
                        'rahvaarv': int(cells[5])
                    }
                    collection.insert_one(rand)
                    print(rand)
                else:
                    collection.update_one(
                        {'nimi': cells[0]},
                        {'$set': {
                            'kuupaev': parse(cells[1] + ' ' + cells[2]),
                            'ohk': int(cells[3]),
                            'vesi': int(cells[4]),
                            'rahvaarv': int(cells[5])
                        }}
                    )
            i += 1
        file.close()
