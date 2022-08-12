#!/bin/env python3 
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

prompt = input("Please tell me what joke subject you are looking for...\nPressing ENTER will give you a random joke.\n")
jokes = get_jokes(prompt)
for joke in jokes:
    print(joke)
