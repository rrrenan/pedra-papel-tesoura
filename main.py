import random
from random import choice

# Opções do computador em lista
escolha_pc = ['Pedra', 'Papel', 'Tesoura']

loop = True

while loop:
    # Escolha do computador
    escolha_pc_choice = choice(escolha_pc)
    print('Eu escolhi a minha jogada. Escolha a sua, irmão!')

    print(""" 
    MENU DE OPÇÕES:
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura
    [4] - Sair do jogo
    """)

    escolha_player = str(input('Escolha a sua jogada: '))

    # Verifica se o jogador deseja sair
    if escolha_player == '4':
        print('Saindo do jogo...')
        loop = False
        continue

    # Escolha player - pedra
    if escolha_player == '1':
        if escolha_pc_choice == 'Pedra':
            resultado = 'EMPATE!'
        elif escolha_pc_choice == 'Papel':
            resultado = 'COMPUTADOR VENCEU!'
        else:
            resultado = 'HUMANO VENCEU!'

    # Escolha player - papel
    elif escolha_player == '2':
        if escolha_pc_choice == 'Pedra':
            resultado = 'HUMANO VENCEU!'
        elif escolha_pc_choice == 'Papel':
            resultado = 'EMPATE!'
        else:
            resultado = 'COMPUTADOR VENCEU!'

    # Escolha player - tesoura
    elif escolha_player == '3':
        if escolha_pc_choice == 'Pedra':
            resultado = 'COMPUTADOR VENCEU!'
        elif escolha_pc_choice == 'Papel':
            resultado = 'HUMANO VENCEU!'
        else:
            resultado = 'EMPATE!'

    else:
        print('[ERRO!] Opção inválida!')
        continue

    # Exibe o resultado
    print('ESCOLHA DO COMPUTADOR: ', escolha_pc_choice)
    print('-=' * 20)
    print('RESULTADO:', resultado)
    print('-=' * 20)
