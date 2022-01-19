import csv
# O módulo csv , contêm duas principais funções:
# Um leitor ( reader ) que nos ajuda a ler o conteúdo, já fazendo as transformações dos valores para Python;
# E um escritor ( writer ) para facilitar a escrita nesse formato.

with open("balneabilidade.csv") as file:
    beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
    header, teste, *data = beach_status_reader

print(header) # cabecalho
print(data) # dados