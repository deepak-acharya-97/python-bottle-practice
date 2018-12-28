from bottle import Bottle, run,template
app=Bottle()
@app.route('/hello')
def hello():
    return "<h1>Hello World</h1>"

@app.route('/')
@app.route('/test/<name>')
def test(name='Deepak Acharya'):
    return template('<h3>Hello {{name}}, Welcome to Bottle World!</h3>',name=name)

run(app, host='localhost', port=5556, debug=True)