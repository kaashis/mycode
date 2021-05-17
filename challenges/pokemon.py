#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    api_url="https://pokeapi.co/api/v2/pokemon/"
    pokeapi = requests.get(api_url).json()

    print("Please enter a pokemon of your choice to lookup:")
    pokemon=input()
    print(api_url+pokemon)
    pokeapi = requests.get(api_url+pokemon).json()
    
   # picurl=pokeapi[pokeman]["front_default"]
   # wget.download(picurl,"/home/student/static")

    #gamecount = len(pokeapi["game_indices"])

    #print(f"{pokechoice} has been in {gamecount} games.")

    #print("moves:", [item['move']['name'] for item in pokeapi['moves']])

    #print(pokeapi)
main()
