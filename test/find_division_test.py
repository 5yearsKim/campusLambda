from config import URL
import requests

def test_find_division_success():
    payload = {'campus': '연세대학교 신촌캠퍼스', 'graduate':"학부", 'department':"공과대학"}
    rsp = requests.get(f'{URL}/find/division', params=payload)  
    print(rsp.text)


if __name__ == '__main__':
    test_find_division_success()

