# Veremos neste arquivo como funciona o tratamento de excessoes no python


# Há pelo menos dois tipos de erros que podem ser destacados: erros de sintaxe e exceções.

# Exceções
# Já as exceções, ocorrem durante a execução e acabam resultando em mensagem de erro. Veja exemplos de exceções:

# print(10 * (1 / 0))
# Traceback (most recent call last): "(" was not closed
# File "<stdin>", line 1, in <module> Unexpected identation
# ZeroDivisionError: division by zero
# print(4 + spam * 3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'spam' is not defined
# print('2' + 2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str

# Tratamento de excesspes no Python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# Lidando com excessoes manipulando arquivos
try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")

#  Caso o open() for utilizado com parametro escrita o arquivo sera criado e clausula de try sera ignorada. A else e finally serao executadas
