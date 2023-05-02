import json
from random import choice
from typing import Self
from class_pokemon import NormalPokemon, FeuPokemon, EauPokemon, TerrePokemon
from class_combat import Combat

class Menu():
    def __init__(self):
        try:
            with open('pokemon.json', 'r') as f:
                self.pokedex = json.load(f)
        except FileNotFoundError:
            self.pokedex = {}
        
    def afficher_menu(self):
        print("=== Menu Pokémon ===")
        print("1. Lancer une partie")
        print("2. Ajouter un Pokémon")
        print("3. Accéder à son Pokédex")
        print("0. Quitter")
        choix = input("Entrez le numéro de votre choix : ")
        if choix == "1":
            self.lancer_partie()
        elif choix == "2":
            self.ajouter_pokemon()
        elif choix == "3":
            self.show_pokedex()
        elif choix == "0":
            return

    def lancer_partie(self):
        print("=== Lancer une partie ===")
        choix = input("1. Créer un nouveau Pokémon\n2. Sélectionner un Pokémon existant\nEntrez le numéro de votre choix : ")
        
        if choix == "1":
            nom_pokemon1 = input("Entrez le nom de votre Pokémon : ")
            pokemon_type1 = input("Entrez le type de votre Pokémon (Normal, Feu, Eau ou Terre) : ")
            pokemon1 = self.ajouter_pokemon(nom_pokemon1, pokemon_type1)
        elif choix == "2":
            print("Sélectionnez un Pokémon :")
            for i, pokemon_data in enumerate(self.pokedex.values()):
                print(f"{i+1}. {pokemon_data['name']} - Niveau : {pokemon_data['level']} - Type : {pokemon_data['Pokemon_type']} - HP : {pokemon_data['hp']} - Attaque : {pokemon_data['attack']} - Défense : {pokemon_data['defense']}")
            choix_pokemon = int(input("Entrez le numéro du Pokémon : "))
            pokemon_data = list(self.pokedex.values())[choix_pokemon-1]
            nom_pokemon1 = pokemon_data['name']
            pokemon_type1 = pokemon_data['Pokemon_type']
            pokemon1 = self.creer_pokemon(nom_pokemon1, pokemon_type1)
        else:
            print("Choix invalide.")
            return
        
        # récupérer un Pokémon aléatoire du Pokédex
        nom_pokemon2, pokemon_data2 = choice(list(self.pokedex.items()))
        pokemon_type2 = pokemon_data2['Pokemon_type']
        pokemon2 = self.creer_pokemon(nom_pokemon2, pokemon_type2)
            
        combat = Combat(pokemon1, pokemon2)
        combat.lancer_combat()
    
    def creer_pokemon(self, nom, pokemon_type):
        if pokemon_type == "Normal":
            pokemon = NormalPokemon(nom)
        elif pokemon_type == "Feu":
            pokemon = FeuPokemon(nom)
        elif pokemon_type == "Eau":
            pokemon = EauPokemon(nom)
        elif pokemon_type == "Terre":
            pokemon = TerrePokemon(nom)
        else:
            raise ValueError("Type de Pokémon invalide.")
        return pokemon
    
    def ajouter_pokemon(self, nom_pokemon=None, pokemon_type=None):
        if nom_pokemon is None:
            nom_pokemon = input("Entrez le nom du Pokémon : ")
        if pokemon_type is None:
            pokemon_type = input("Entrez le type du Pokémon (Normal, Feu, Eau ou Terre) : ")
        pokemon = self.creer_pokemon(nom_pokemon, pokemon_type)
        self.enregistrer_pokemon(pokemon)
        print("Votre Pokemon est ajouté a votre Pokedex")
        return pokemon
    
    def enregistrer_pokemon(self, pokemon):
        self.pokedex[pokemon.get_name()] = pokemon.to_dict()
        with open("pokemon.json", "w") as f:
            json.dump(self.pokedex, f)

    def show_pokedex(self):
        try:
            with open('pokemon.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Votre Pokédex est vide !")
            return
        if not data:
            print("Votre Pokédex est vide !")
        else:
            print("Voici les Pokémon que vous avez rencontrés :")
            for pokemon_data in data.values():
                pokemon_type = pokemon_data.get('pokemon_type', 'Type inconnu')
                print(f"- Nom du Pokemon : {pokemon_data['name']} - Niveau : {pokemon_data['level']} - Type : {pokemon_data['Pokemon_type']} - HP : {pokemon_data['hp']} - Attaque : {pokemon_data['attack']} - Défense : {pokemon_data['defense']}")
            return
menu = Menu()
menu.afficher_menu()

