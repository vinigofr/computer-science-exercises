#Um segundo cenário é onde a função espera o nome de um arquivo e a abertura do mesmo acontece dentro da função.
# pokemon_read.py

import json


def retrieve_pokemons_by_type(type, filepath):
    with open(filepath) as file:
        pokemons = json.load(file)["results"]
        pokemons_by_type = [
            pokemon for pokemon in pokemons if type in pokemon["type"]
        ]
        return pokemons_by_type
# Para escrever este teste, vamos aproveitar da natureza dinâmica da linguagem e substituir o método open em tempo de execução por um objeto mock_open , que já vem embutido na linguagem e se comporta como o open , retornando o que foi definido em read_data como seu conteúdo. Um detalhe interessante é que esse objeto obtido através da função mock_open também possui a capacidade de armazenar informações sobre como foram as chamadas de seus métodos e os parâmetros recebidos.