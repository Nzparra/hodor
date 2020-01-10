#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    url = 'http://158.69.76.135/level0.php'
    data = {
        'id': '1190',
        'holdthedoor': 'submit'
    }
    for i in range(1024):
        requests.post(url, data=data)
