from chalice import Chalice
from chalicelib.info_handler import *
app = Chalice(app_name='campusLambda')
app.api.cors =True

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/find/campus', methods=["GET"])
def find_campus():
    return find_campus_handler()

@app.route('/find/department', methods=["GET"])
def find_department(): 
    return find_department_handler(app.current_request) 

@app.route('/find/division', methods=["GET"])
def find_division():
    return find_division_handler(app.current_request)

@app.route('/campusDomain', methods=['GET'])
def get_campusDomain():
    return get_campusDomain_handler(app.current_request) 
