from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/teine', methods = ['GET'])
@app.route('/2', methods = ['POST'])
@app.route('/molemad', methods = ['GET', 'POST'])
def teine():
    return '<h1>See on yks teine leht</h1>'

@app.route('/dynaamiline/<number>/<arv>')
def dynaamiline(number, arv):
    return '<p>Oled lehekyljel ' + number + '</p><p>' + arv + '</p>'

@app.route('/dynaamiline2', methods = ['GET'])
def dynaamiline2():
    min = request.args.get('min', default = 1, type = int)
    max = request.args.get('max', default = 100, type = int)
    return 'MIN: ' + str(min) + ', MAX: ' + str(max)

@app.route('/juhuslik')
def juhuslik():
    juhuslik_arv = randint(1, 10000)
    return render_template('index.html', arv = juhuslik_arv)
    pass

if __name__ == '__main__':
    app.run(debug = True)