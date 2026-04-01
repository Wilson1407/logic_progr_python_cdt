'''

r - read = leitura
w - writer = escrever
a - append = adicionar

'''

def ler_arquivo_jovens():
    print('Sistema de upload dos arquivos jovens')
    print('-' * 30)

    with open('arquivo_lido.txt', 'r', encoding= 'utf-8') as arquivo:
        conteudo = arquivo.read() 
        print(conteudo)  

ler_arquivo_jovens()


def sobrescrever_arquivo():
    print('--- Sistema de upload dos arquivos jovens (Modo Sobrescrever) ---')
    
    conteudo_novo = input("Digite o que deseja salvar (ISSO APAGARÁ O QUE ESTAVA LÁ): ")

    with open('arquivo_lido.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo_novo + "\n")
    
    print("\n[AVISO] O arquivo foi limpo e o novo conteúdo foi gravado!")

def ler_arquivo_jovens():
    print('\n--- Lendo o arquivo agora ---')
    try:
        with open('arquivo_lido.txt', 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

sobrescrever_arquivo()
ler_arquivo_jovens()