import requests
import csv

def fetch_pokemon_data():
    url = "https://pokeapi.co/api/v2/type/electric"
    response = requests.get(url).json()
    pokemons = []

    for pokemon in response["pokemon"]:
        details = requests.get(pokemon["pokemon"]["url"]).json()
        weight = details["weight"]
        height = details["height"]
        image = details["sprites"]["front_default"]

        if weight < 10000:  # משקל בפורמט של 10x גרם
            pokemons.append([details["name"], height, weight, image])

    return pokemons

def save_to_csv(pokemons):
    with open("pokemons.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Height", "Weight", "Image"])
        writer.writerows(pokemons)

if __name__ == "__main__":
    data = fetch_pokemon_data()
    save_to_csv(data)
    print("Data saved to pokemons.csv")
