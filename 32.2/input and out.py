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

# Tratando numeros de ponto flutuante
print(f"{x} / {y} = {x / y:.2f}")  # saída: 5 / 2 = 1.67
# {x} é substituído por 5
# {y} é substituído por 3
# {x / y:.2f} O que vem após os dois pontos são formatadores, como nesse exemplo, duas casas decimais (.2f).
print(f"{x:.^3}")  # saída: ".5."