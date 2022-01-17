# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.?

def mediaAritmetica(*values):
	total = 0
	for value in values:
		total = total + value
	return total / len(values)


result = mediaAritmetica(1, 5, 6, 12, 18, 6)

print(result, "linha 12")