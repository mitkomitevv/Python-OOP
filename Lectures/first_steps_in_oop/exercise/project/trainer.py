from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        # p = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        for p in self.pokemons:
            if pokemon_name == p.name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}\n"
                  f"Pokemon count {len(self.pokemons)}"]

        for pokemon in self.pokemons:
            result.append(f"- {pokemon.pokemon_details()}")

        return '\n'.join(result)
