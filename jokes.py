#!/bin/env python3 
import requests

def get_jokes(term=""):
    jokes = []
    headers={"Accept":"application/json"}
    if term!="":
        url = "https://icanhazdadjoke.com/search"
        response = requests.get(url,params={"term":term},headers=headers)
        data = response.json()['results']
        for item in data:
            jokes.append(item['joke'])
    else:
        response = requests.get("https://icanhazdadjoke.com/", headers=headers)
        jokes.append(response.json()['joke'])
    if len(jokes)==0:
        jokes = ['No jokes for the term: \"'+term + '\"']
    return jokes

prompt = input("Please tell me what joke subject you are looking for...\nPressing ENTER will give you a random joke.\n")
jokes = get_jokes(prompt)
for joke in jokes:
    print(joke)
