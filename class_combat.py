import random
import time


class Combat():
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
    def lancer_combat(self):
        print(f"Le combat commence entre {self.pokemon1.get_name()} et {self.pokemon2.get_name()} !")
    
        while self.check_victory() is None:
            self.attack(self.pokemon1)
            print(f"{self.pokemon1.get_name()} a attaqué ! {self.pokemon2.get_name()} a {self.pokemon2.get_hp()} points de vie restants.")
            time.sleep(1)
            if self.check_victory() is not None:
                break
            
            self.attack(self.pokemon2)
            print(f"{self.pokemon2.get_name()} a attaqué ! {self.pokemon1.get_name()} a {self.pokemon1.get_hp()} points de vie restants.")
            time.sleep(1)
        print(f"{self.get_winner()} a gagné le combat !")
        # self.afficher_menu()

    def check_victory(self):
        if self.pokemon1.get_hp() <= 0:
            return self.pokemon2.get_name()
        elif self.pokemon2.get_hp() <= 0:
            return self.pokemon1.get_name()
        else:
            return None
    
    def get_winner(self):
        if self.pokemon1.get_hp() <= 0:
            return self.pokemon2.get_name()
        elif self.pokemon2.get_hp() <= 0:
            return self.pokemon1.get_name()
        else:
            return "Match nul"
    
    def attack(self, pokemon):
        attack_chance = random.randint(0, 1)
        print(f"{pokemon.get_name()} a une chance de {attack_chance} d'attaquer !")
        if attack_chance == 1:
            attack_power = pokemon.attack * self.get_attack_multiplier(pokemon.pokemon_type, self.get_opponent_type(pokemon))
            self.pokemon2.set_hp(self.pokemon2.get_hp() - max(0, attack_power - self.pokemon2.defense))
        else:
            print(f"{pokemon.get_name()} a manqué son attaque !")

    
    def get_opponent_type(self, pokemon):
        if self.pokemon1 == pokemon:
            return self.pokemon2.pokemon_type
        else:
            return self.pokemon1.pokemon_type
    
    def get_attack_multiplier(self, attacker_type, opponent_type):
        if attacker_type == "Feu":
            if opponent_type == "Eau":
                return 0.5
            elif opponent_type == "Terre":
                return 2
            else:
                return 1
        elif attacker_type == "Eau":
            if opponent_type == "Terre":
                return 0.5
            elif opponent_type == "Feu":
                return 2
            else:
                return 1
        elif attacker_type == "Terre":
            if opponent_type == "Feu":
                return 0.5
            elif opponent_type == "Eau":
                return 2
            else:
                return 1
        elif attacker_type == "Normal":
            if opponent_type in ("Eau", "Terre", "Feu"):
                return 0.75
            else:
                return 1
        else:
            return 1

    
    def lose_hp(self, pokemon, damage):
        pokemon.set_hp(pokemon.get_hp() - damage)
    
    def get_loser(self):
        if self.pokemon1.get_hp() <= 0:
            return self.pokemon1.get_name()
        elif self.pokemon2.get_hp() <= 0:
            return self.pokemon2.get_name()
        else:
            return None
    
    def save_to_pokedex(self, pokemon):
        # Ajoute le pokemon à votre Pokédex
        pass # code pour sauvegarder le pokemon dans le pokedex
