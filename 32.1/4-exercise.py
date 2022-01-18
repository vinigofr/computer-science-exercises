# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda".

from multiprocessing.dummy import current_process


def findBiggestName(names):
  currentbiggestName = ''
  for name in names:
    if len(currentbiggestName) < len(name):
      currentbiggestName = name
  print(currentbiggestName)

findBiggestName(["José", "Vinicius Gouveia", "Nádia", "Fernanda", "Cairo", "Joana"])


