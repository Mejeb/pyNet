import requests
import sys

for word in sys.stdin:
    res = requests.get(url=f"http://10.10.11.161/{word}")

    print(res)
    data = res.json()

    print(data)