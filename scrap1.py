import requests

url = "https://api.stackexchange.com/2.1/questions"
params = {
    "order": "desc",
    "sort": "activity",
    "tagged": "python",
    "site": "stackoverflow"
}

resp = requests.get(url, params=params)
data = resp.json()

for item in data.get('items', []):
    print(item['title'])
