# O with é a palavra reservada para gerenciamento de contexto. Este gerenciamento ( with ) é utilizado para encapsular a utilização de um recurso, garantindo que certas ações sejam tomadas independentemente se ocorreu ou não um erro naquele contexto.

# A função open retorna um objeto que se comporta como um gerenciador de contexto de arquivo que será responsável por abrir e fechar o mesmo. Isto significa que o arquivo possui mecanismos especiais que, quando invocados, utilizando with , alocam um determinado recurso, no caso um arquivo, e, quando o bloco for terminado, este recurso será liberado automaticamente

# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
with open("arquivo.txt", "w") as file:
    file.write("Vincius Gouveia\n")
# como estamos fora do contexto, o arquivo foi fechado. Eliminando necessidade do file.close()