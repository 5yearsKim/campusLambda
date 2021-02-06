from config import URL
import requests

def test_find_campus_success():
    rsp = requests.get(f'{URL}/find/campus')  
    print(rsp.text)


if __name__ == '__main__':
    test_find_campus_success()

