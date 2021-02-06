from chalice import Chalice
from chalicelib.campus_info import campus_dict

app = Chalice(app_name='campusLambda')
app.api.cors =True

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/find/campus', methods=["GET"])
def find_campus():
    campus_list = list(campus_dict.keys())
    rsp = {"is_success": True, "message": "get campus list success", "data": campus_list }
    return rsp

@app.route('/find/department', methods=["GET"])
def find_department():
    request = app.current_request
    data = request.query_params
    try:
        campus = data['campus']
        graduate = data['graduate']
        dep_list = list(campus_dict[campus][graduate].keys())
        rsp = {"is_success": True, "message": "get department list success", "data": dep_list }
        return rsp
    except Exception as e:
        rsp = {"is_success": False, "message": str(e), "error_cd": 10 }
        return rsp
        

@app.route('/find/division', methods=["GET"])
def find_division():
    request = app.current_request
    data = request.query_params
    try:
        campus = data['campus']
        graduate = data['graduate']
        if graduate != '학부':
            raise Exception('only support for undergraduate')
        department = data['department']
        div_list = list(campus_dict[campus][graduate][department])
        rsp = {"is_success": True, "message": "get division list success", "data": div_list }
        return rsp
    except Exception as e:
        rsp = {"is_success": False, "message": str(e), "error_cd": 11 }
        return rsp

