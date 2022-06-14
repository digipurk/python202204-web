from flask import Flask, request, render_template, jsonify
import random
from db import get_database
from bson.json_util import dumps

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return 'Test'

@app.route('/dices')
def dices():
    dice_count = request.args.get('dice_count', default = 1, type = int)
    dices = []
    total = 0
    for dice in range(dice_count):
        random_num = random.randint(1, 6)
        dices.append(random_num)
        total += random_num
    return render_template('dices.html', dice_count = dice_count, dices = dices, total = total)

@app.route('/api/v1/resources/rannad/all', methods = ['GET'])
def api_rand_all():
    dbclient = get_database()
    collection = dbclient['rand']
    ret = jsonify(dumps(collection.find()))
    return ret

@app.route('/api/v1/resources/rannad/<nimi>', methods = ['GET'])
def api_rand(nimi):
    dbclient = get_database()
    collection = dbclient['rand']
    ret = jsonify(dumps(collection.find({'nimi': nimi})))
    return ret

if __name__ == '__main__':
    app.run(debug = True)