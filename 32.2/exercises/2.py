from email.contentmanager import raw_data_manager
import random


def word_game(*words):
    remaining_attempts = 3
    word = random.choice(words) #escolhe a palavra de forma aleatoria
    scrambled_word = "".join(random.sample(word, len(word))) # embaralha a palavra
    print(f"Voce consegue adivinhar que palavra eh essa?--> {scrambled_word} <--")
    while True:
        user_input = input(f"Digite sua resposta --->") # pergunta ao usuario e espera pelo input
        if user_input == word:
            print("Parabens, voce acertou!")
            break
        elif remaining_attempts > 1:
            remaining_attempts = remaining_attempts - 1
            print(f"Voce errou, mas voce ainda tem {remaining_attempts} chances restantes")
        else:
            print("Infelizmente suas chances acabaram :( - ", "Mais sorte da proxima")
            break

word_game('vinicius', 'gouveia', 'freitas')