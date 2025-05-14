import json
import hashlib
from pathlib import Path

# Caminho do arquivo JSON
CRIAR_JSON = Path("credenciais.json")

def crip_senha(senha: str) -> str:
    #Gera hash SHA-256 para a senha.
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()

def carregar_usuario() -> dict:
    #Carrega o JSON de credenciais; retorna lista vazia se não houver arquivo.
    if not CRIAR_JSON.exists():
        return {"credenciais": []}
    with CRIAR_JSON.open("r", encoding="utf-8") as f:
        return json.load(f)

def salvar_usuario(data: dict):
    #Salva o dicionário de credenciais no arquivo JSON."""
    with CRIAR_JSON.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def verificar_usuario(username: str) -> bool:
    #Verifica se já existe credencial com o mesmo usuário."""
    data = carregar_usuario()
    return any(cred["usuario"] == username for cred in data["credenciais"])

def adicionar_usuario(usuario: str, nome_completo: str, senha: str):
    #Adiciona um novo usuário com nome completo e senha (armazenada como hash).
    data = carregar_usuario()
    senha_hash = crip_senha(senha)
    data["credenciais"].append({
        "usuario": usuario,
        "nome_completo": nome_completo,
        "senha_hash": senha_hash
    })
    salvar_usuario(data)

def novo_usuario():
    #Fluxo interativo para cadastrar novo login, nome completo e senha.
    # 1) Solicita usuário e checa existência
    while True:
        usuario = input("Escolha um nome de usuário (login): ").strip()
        if not usuario:
            print("❌ Login não pode ficar vazio. Tente de novo.")
        elif verificar_usuario(usuario):
            print(f"❌ Já existe um usuário com o login '{usuario}'. Tente outro.")
        else:
            break

    # 2) Solicita nome completo
    while True:
        nome_completo = input("Digite seu nome completo: ").strip()
        if not nome_completo:
            print("❌ Nome completo não pode ficar vazio.")
        else:
            break

    # 3) Solicita senha e confirmação
    while True:
        senha = input("Digite sua senha: ")
        conf_senha = input("Confirme sua senha: ")
        if senha != conf_senha:
            print("❌ As senhas não conferem. Digite novamente.")
        elif not senha:
            print("❌ Senha não pode ficar vazia.")
        else:
            break

    # 4) Adiciona no JSON
    adicionar_usuario(usuario, nome_completo, senha)
    print("✅ Usuário cadastrado com sucesso!")

def carregar_dados():
    #Fluxo de login: solicita usuário e senha, valida e retorna dados.
    #Retorna um dict com 'usuario' e 'nome_completo' se sucesso, ou None se falhar.
    
    data = carregar_usuario()
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ")
    senha_hash = crip_senha(senha)

    for cred in data["credenciais"]:
        if cred["usuario"] == usuario and cred["senha_hash"] == senha_hash:
            # Extrai apenas o primeiro nome
            primeiro_nome = cred["nome_completo"].split()[0]
            print(f"✅ Bem‑vindo(a), {primeiro_nome}!")
            return {
                "usuario": cred["usuario"],
                "nome_completo": cred["nome_completo"]
            }

    # Se não encontrou correspondência
    print("❌ Usuário ou senha inválidos.")
    return None

def menu_login():
    print("1) Cadastrar novo usuário")
    print("2) Fazer login")
    escolha = input("Escolha uma opção: ").strip()
    if escolha == "1":
        novo_usuario()
    elif escolha == "2":
        carregar_dados()
    else:
        print("Opção inválida.")

menu_login()