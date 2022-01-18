# Exemplos de inputs no python

numero = input("Digite um numero ->")
print(numero)

# Print em duas linhas?
# Join do print
print("Maria", "Joao", sep=", ")

# Remove pulo de linha
print("Na mesma", end="")
print("Linha")

# Controlando saida pradrao de erro
import sys
err = "Arquivo nao encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr)

import sys

# Este exemplo manda o nome do arquivo no qual estamos
# executando
if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)