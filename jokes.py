import requests

def get_jokes(term=""):
    jokes = []
    if term!="":
        url = "https://icanhazdadjoke.com/search"
        response = requests.get(url,params={"term":term},headers={"Accept":"application/json"})
        data = response.json()['results']
        for item in data:
            jokes.append(item['joke'])
    else:
        response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        jokes.append(response.json()['joke'])
    return jokes

data = get_jokes("pickle")
print(data)
