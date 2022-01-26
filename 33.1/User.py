# Momento em que se cria uma entidade (classe) se chama abstracao

# Encapsulamento: eh voce nao precisar saber como funciona um metodo de uma classe

# Objeto: Entidade "específica", criada a partir das regras definidas pela entidade "geral". Pense que a classe é o molde e o objeto a escultura que o molde faz!

# Instância: esse é novo! Sabe quando criamos um objeto a partir de uma classe! Então! Dizemos que esse objeto é uma instância dessa classe! Ou, também, dizemos que a classe instanciou um objeto!

# Atributo: outro novo! Um atributo é uma informação de uma instância que você criou. O nome de um User, por exemplo.

# Mensagem: Forma com que objetos interagem - chamando funções uns dos outros. Um chamado como esse é um envio de mensagem a outro objeto. "User, resete sua senha!"

# Abstração: Pilar da Programação Orientada a Objetos. Se refere a sempre criar entidades que farão as ações que resolverão seu problema.

# Encapsulamento: Pilar da Programação Orientada a Objetos. Se refere a poder instanciar uma entidade e enviar mensagens a ela sem saber como ela funciona por dentro

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        print("Envia email de reset de senha")

meu_user = User("Vinicius", "vini@vini.com", "vini")
meu_user.reset_password()
