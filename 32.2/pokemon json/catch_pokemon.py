import json

with open('pokemon.json', mode="r") as file:
    content = file.read() # leitura
    pokemons = json.loads(content)["results"]

# print(pokemons[0])


# Separando os pokemon pelo tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

#Escrevendo o arquivo apenas com pokemons do tipo grama
with open("grass_pokemon_type.json", "w") as file:
    json_to_write = json.dumps(grass_type_pokemons) # converte ed python p/ json
    file.write(json_to_write)

# abre o arquivo para escrita
with open("grass_pokemons.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(grass_type_pokemons, file)