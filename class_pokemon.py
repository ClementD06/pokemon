import json
from random import choice
from typing import Self

class Pokemon:
    def __init__(self, name, pokemon_type, hp, level=1, attack=0, defense=0):
        self.name = name
        self.hp = hp
        self.pokemon_type = pokemon_type
        self.level = level
        self.attack = attack
        self.defense = defense
    
    def to_dict(self):
            return {"name": self.name, "Pokemon_type": self.pokemon_type, "hp": self.hp, "level": self.level, "attack": self.attack, "defense": self.defense}

    def __str__(self):
        return f"{self.name} ({self.pokemon_type}), {self.hp} HP,  {self.level} Level, {self.attack} attack, {self.defense} defense"

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp
    
    def get_attack_power(self, opponent):
        attack_power = self.attack
        if self.pokemon_type == "Feu":
            if opponent.pokemon_type == "Eau":
                attack_power *= 0.5
            elif opponent.pokemon_type == "Terre":
                attack_power *= 2
        elif self.pokemon_type == "Eau":
            if opponent.pokemon_type == "Terre":
                attack_power *= 0.5
            elif opponent.pokemon_type == "Feu":
                attack_power *= 2
        elif self.pokemon_type == "Terre":
            if opponent.pokemon_type == "Feu":
                attack_power *= 0.5
            elif opponent.pokemon_type == "Eau":
                attack_power *= 2
        return attack_power

class NormalPokemon(Pokemon):
    def __init__(self, name, hp=100, level=1, attack=1, defense=0):
        super().__init__(name, "Normal", hp, level, attack, defense)
        self.hp = hp + (0 * level)
        self.attack = attack + (5 * level)
        self.defense = defense + (0 * level)

class FeuPokemon(Pokemon):
    def __init__(self, name, hp=100, level=1, attack=1, defense=0):
        super().__init__(name, "Feu", hp, level, attack, defense)
        self._hp = hp + (0 * level)
        self.attack = attack + (5 * level)
        self.defense = defense + (0 * level)

class EauPokemon(Pokemon):
    def __init__(self, name, hp=100, level=1, attack=1, defense=0):
        super().__init__(name, "Eau", hp, level, attack, defense)
        self._hp = hp + (0 * level)
        self.attack = attack + (5 * level)
        self.defense = defense + (0 * level)

class TerrePokemon(Pokemon):
    def __init__(self, name, hp=100, level=1, attack=1, defense=0):
        super().__init__(name, "Terre", hp, level, attack, defense)
        self._hp = hp + (0 * level)
        self.attack = attack + (5 * level)
        self.defense = defense + (0 * level)