from chalicelib.local_data import campus_dict, domain

def find_campus_handler():
    campus_list = list(campus_dict.keys())
    rsp = {"is_success": True, "message": "get campus list success", "data": campus_list }
    return rsp

def find_department_handler(request):
    data = request.query_params
    try:
        campus = data['campus']
        graduate = data['graduate']
        target = campus_dict[campus][graduate]
        if isinstance(target, set):
            dep_list = list(target)
        else:
            dep_list = list(target.keys())
        rsp = {"is_success": True, "message": "get department list success", "data": dep_list }
        return rsp
    except Exception as e:
        rsp = {"is_success": False, "message": str(e), "error_cd": 10 }
        return rsp


def find_division_handler(request):
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


def get_campusDomain_handler(request):
    data = request.query_params
    try :
        campus = data['campus']
        domain_list = domain[campus]
        rsp = {"is_success": True, "message": "bring domain list success", "data": domain_list }
        return rsp
    except Exception as e:
        rsp = {"is_success": False, "message": str(e), "error_cd": 12 }
        return rsp
