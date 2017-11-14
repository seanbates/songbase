@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/user/<string:name>/')
def get_user(name):
    return 'hello %s %d' % (name, 3)

@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    if request.method=='GET':
        first_name = request.args.get_user('first_name')
        return render_template('form-demo.html')

    if request.method=='POST':
        first_name = request.form['first_name']
        return render_template('form-demo.html')
