from chalice import Chalice

app = Chalice(app_name='campusLambda')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/find/campus')
def find_campus():
    pass

@app.route('/find/department')
def find_department():
    pass

@app.route('/find/division')
def find_division():
    pass

