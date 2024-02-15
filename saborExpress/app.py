import os

# Lista
# restaurantes = ['Gurmesan Sushi', 'Confra Grill']

# Dicionarios
restaurantes = [{'nome': 'Gurmesan Sushi', 'categoria': 'Japonesa', 'ativo':False },
                 {'nome': 'Confra Grill', 'categoria': 'Churrascaria', 'ativo':True },
                 {'nome': 'Doce café', 'categoria': 'Cafeteria', 'ativo':False }]
                #  chave : valor         ,   Chave :      valor   ,  Chave : valor

def exibir_nome():
    print('''

    ▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
    ░▀▀▀▄▄ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 ▒█▀▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
    ▒█▄▄▄█ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀
    ''')

# Funções do sistema !! 
    
def exibir_opcoes():
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurantes')
    print('3 - Ativar Restaurante')
    print('4 - Sair \n')

# Utilização de IF, ELIF e ELSE
def escolher_opcao():
    try:
        opcao_usuario = int(input('Escolha uma opção: '))
        if opcao_usuario == 1:
            cadastra_restaurante()
        elif opcao_usuario == 2:
            listar_restaurante()
        elif opcao_usuario == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def alternar_estado_restaurante():
    exibir_subtitulos('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
        
    voltar_menu_principal()



def cadastra_restaurante():
    exibir_subtitulos('Cadastro novos restaurantes')
    
    nome_restaurante  = input('Digite o nome do restaurante que deseja cadastrar: \n')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: \n')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} foi cadastrado com sucesso! \n')
    voltar_menu_principal()

def listar_restaurante():
    exibir_subtitulos('Lista de restaurantes \n')

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo} ')
    voltar_menu_principal()

def opcao_invalida():
    print('Opção invalida! \n')
    voltar_menu_principal()

def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal! ')
    main()

def finalizar_app():
    exibir_subtitulos('Encerrando App \n')

# Utilização de Match (CASE)
    
#def escolher_opcao:      
# opcao_escolhida = int(input('Escolha uma opção: '))
# match opcao_escolhida:
#     case 1:
#         print('Adicionar restaurante')
#     case 2:
#         print('Listar restaurantes')
#     case 3:
#         print('Ativar restaurante')
#     case 4:
#         print('Finalizar app')
#     case _:
#         print('Opção inválida!')


def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()



    