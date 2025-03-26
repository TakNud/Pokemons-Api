from flask import Flask, jsonify
import csv

app = Flask(__name__)

def load_pokemon_data():
    pokemons = []
    with open("pokemons.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            pokemons.append(row)
    return pokemons

@app.route("/pokemons", methods=["GET"])
def get_pokemons():
    return jsonify(load_pokemon_data())

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
