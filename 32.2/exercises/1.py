# Exercício 1: Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida.

def invertLadderName(name):
  for index in reversed(range(len(name) + 1)):
    print(name[slice(index)])

print(invertLadderName('francisco'))
