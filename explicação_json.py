import os
import json

def configurar_sistema():
    if not os.path.exists("uploads_projetos"):
        os.makedirs("uploads_projetos")

def listar_projetos():
    arquivos = [f for f in os.listdir("uploads_projetos") if f.endswith(".json")]
    print('\n'+'='*40)
    print(' PROJETOS CADASTRADOS')
    print('='*40)

    if not arquivos:
        print("Nenhum projeto encontrado.")
        return []

    for i, arquivo in enumerate(arquivos, 1):
        nome_exibicao = arquivo.replace("projeto_", "").replace(".json", "").replace("_", " ")
        print(f"{i}. {nome_exibicao}")

    return arquivos
            
def gerenciar_projeto():
    arquivos = listar_projetos()
    if not arquivos:
        return

    try:
        escolha = int(input("\nEscolha o número do projeto para gerenciar (ou 0 para voltar): "))
    except ValueError:
        print("[ERRO] Por favor, insira um número válido.")
        return

    if escolha == 0:
        return

    try:
        nome_arquivo = arquivos[escolha - 1]
    except IndexError:
        print("[ERRO] Escolha inválida. Voltando ao menu.")
        return

    caminho = os.path.join("uploads_projetos", nome_arquivo)

    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[ERRO] Não foi possível ler o projeto: {e}")
        return

    print(f"\n--- Dados Atuais ---")
    print(f"Aluno: {dados.get('aluno', '')}")
    print(f"Projeto: {dados.get('projeto', '')}")

    confirmar = input("\nDeseja alterar as informações desse projeto? (s/n): ").strip().lower()
    if confirmar == 's':
        dados['aluno'] = input(f"Novo nome [{dados.get('aluno', '')}]: ") or dados.get('aluno', '')
        dados['projeto'] = input("Novo resumo: ") or dados.get('projeto', '')

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print("\n[Sucesso] Projeto atualizado com sucesso!")

def fazer_upload_json():
    print('\n'+ '='*40)
    print(' NOVO UPLOADS DE PROJETO')
    print('='*40)
    nome_aluno = input("Nome do aluno:").strip()
    resumo = input("Resumo do projeto:")

    dados = {"aluno": nome_aluno, "projeto": resumo}
    nome_fich = nome_aluno.replace(" ","_").lower()
    caminho = os.path.join("uploads_projetos", f"projeto_{nome_fich}.json")

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print(f"\n[SUCESSO] Projeto de {nome_aluno} guardado!")

def menu():
    configurar_sistema()
    while True:
        print('\n'+'#'*40)
        print(' SISTEMA DE ARQUIVOS JOVEN 3.0 ')
        print('#'*40)
        print("1. Inserir Novo projeto")
        print("2. Listar e Alterar projetos")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            fazer_upload_json()
        elif opcao == "2":
            gerenciar_projeto()
        elif opcao == "0":
            print("Encerrando...Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida!")

if __name__ == "__main__":
    menu()