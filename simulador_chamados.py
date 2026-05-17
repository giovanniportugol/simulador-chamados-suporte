# Simulador de Chamados de Suporte Técnico
# Projeto acadêmico em Python
# Objetivo: praticar lógica de programação em um contexto de suporte técnico

print("=== Simulador de Chamados de Suporte Técnico ===")

nome = input("Digite o nome do usuário: ")
setor = input("Digite o setor do usuário: ")

print("\nTipos de problema:")
print("1 - Acesso ao sistema")
print("2 - Problema de internet/rede")
print("3 - Computador lento")
print("4 - Instalação de programa")
print("5 - Outro")

opcao = input("Escolha o tipo de problema: ")

if opcao == "1":
    tipo_problema = "Acesso ao sistema"
elif opcao == "2":
    tipo_problema = "Problema de internet/rede"
elif opcao == "3":
    tipo_problema = "Computador lento"
elif opcao == "4":
    tipo_problema = "Instalação de programa"
else:
    tipo_problema = "Outro"

descricao = input("Descreva brevemente o problema: ")

print("\nNíveis de prioridade:")
print("1 - Baixa")
print("2 - Média")
print("3 - Alta")

prioridade_opcao = input("Escolha a prioridade do chamado: ")

if prioridade_opcao == "1":
    prioridade = "Baixa"
elif prioridade_opcao == "2":
    prioridade = "Média"
elif prioridade_opcao == "3":
    prioridade = "Alta"
else:
    prioridade = "Não definida"

print("\n=== Resumo do Chamado ===")
print("Usuário:", nome)
print("Setor:", setor)
print("Tipo de problema:", tipo_problema)
print("Descrição:", descricao)
print("Prioridade:", prioridade)
print("Status: Chamado registrado para análise.")
