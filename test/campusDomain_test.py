from config import URL
import requests

def test_campusDomain_success():
    payload = {'campus': '연세대학교 신촌캠퍼스'}
    rsp = requests.get(f'{URL}/campusDomain', params=payload)  
    print(rsp.text)


if __name__ == '__main__':
    test_campusDomain_success()

