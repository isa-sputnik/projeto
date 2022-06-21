from telainicial import inicio
from boat import sair


def fale_conosco():
    escolha2 = int(input('\nComo posso ajudar nesse caso?\n 1. Contato\n 2. App M&M\n 3. Encontre Agências\n 4. Retorne ao início\n Escolha: '))
    if escolha2 == 4:
        inicio()
    elif escolha2 == 1:
        print('\nVocê pode nos contatar por essas vias:\n  Central de atendimento: 0800 123 321 (segunda a sexta das 08:00 às 18:00\n  e-mail: suporte@mmfinanceira.com.br\n')
        opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha:'))
        if opcoes_saida == 1:
            sair()
        elif opcoes_saida == 2:
            inicio()
    elif escolha2 == 2:
        print('\nBaixe o nosso app e tenha o seu serviço disponível na palma da sua mão!\n  Disponível para Androis, IOS e Windows: www.mmfinanceira.com/App\n')
        opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha: '))
        if opcoes_saida == 1:
            sair()
        elif opcoes_saida == 2:
            inicio()
    elif escolha2 == 3:
        print('\nEncontre um de nossos respresentantes mais perto de você pelo "M&M perto de você!"\n  Acesse em: www.mmfinanceira.com/Pertodevoce\n')
        opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha: '))
        if opcoes_saida == 1:
            sair()
        elif opcoes_saida == 2:
            inicio()