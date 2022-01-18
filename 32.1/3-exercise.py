# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um quadrado feito de asteriscos de lado de tamanho n.

def fazerAsteriscos(numVezes):
  asteriscoString = ''
  for index in range(numVezes):
    asteriscoString += '*'

  for index in range(numVezes):
    print(asteriscoString)

fazerAsteriscos(10)