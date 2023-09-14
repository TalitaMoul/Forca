import random

# Lista do bonequinho enforcado 
enforcado = [
    '''
       +---+
           |
           |
           |
          ===
    ''',
    '''
       +---+
       O   |
           |
           |
          ===
    ''',
    '''
       +---+
       O   |
       |   |
           |
          ===
    ''',
    '''
       +---+
       O   |
      /|   |
           |
          ===
    ''',
    '''
       +---+
       O   |
      /|\\  |
           |
          ===
    ''',
    '''
       +---+
       O   |
      /|\\  |
      /    |
          ===
    ''',
    '''
       +---+
       O   |
      /|\\  |
      / \\  |
          ===
    '''
]


# Palavras que serão sorteadas
palavras_forca = ["Casa", "Gato", "Cachorro", "Mesa", "Amigo", "Livro", "Computador",
                   "Janela", "Caminho", "Telefone", "Caneta","Carro", "Praia",
                   "Flor", "Arvore", "Chocolate", "Foto","Maca", "Pao", "Caneca"]

# Sorteio das palavras via random.choice
palavra_aleatoria = random.choice(palavras_forca).upper()


# Variáveis do jogo
letras_adivinhadas = []
chances = 6
bonequinho = 0

print(f"{'-'*10} JOGO DA FORCA {'-'*10}")


while True:

    # Solicitando a letra ao jogador
    tentativa = input("\nDigite uma letra: ").upper()
    letras_adivinhadas.append(tentativa)

    for letra in palavra_aleatoria:
        if letra in letras_adivinhadas:
            print(letra, end=' ')
        else:
            print('_', end=' ')

    if tentativa not in palavra_aleatoria:
        chances -= 1
        bonequinho += 1
    print(f"\n{enforcado[bonequinho]}")
    print(f'\nVocê tem {chances} chances.') 
    

    ganhou = True

    for letra in palavra_aleatoria:
        if letra not in letras_adivinhadas:
            ganhou = False
           

    if chances == 0 or ganhou: 
        break

if ganhou:
    print(f"\nParabéns! A palavra sorteada era {palavra_aleatoria}")

else:
    print(f"\nVocê perdeu. A palavra sorteada era {palavra_aleatoria}")
    