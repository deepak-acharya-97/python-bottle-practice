from bottle import route, run

@route('/hello')
def hello():
    return "<h1>Hello World</h1>"

run(host='localhost', port=5555, debug=True)