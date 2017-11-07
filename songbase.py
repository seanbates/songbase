@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/user/<string:name>/')
def get_user(name):
    return 'hello %s %d' % (name, 3)
