# Assistente Help Desk com IA Simples
# Projeto acadêmico em Python
# Objetivo: simular um atendimento inicial de suporte técnico usando regras simples

print("=== Assistente Help Desk com IA Simples ===")

nome = input("Digite seu nome: ")
setor = input("Digite seu setor: ")
descricao = input("Descreva o problema encontrado: ")

descricao_minuscula = descricao.lower()

categoria = "Outro"
prioridade = "Baixa"
encaminhamento = "Suporte técnico"
resposta_cliente = "Seu chamado foi registrado e será analisado pela equipe de suporte."

if "senha" in descricao_minuscula or "acesso" in descricao_minuscula or "login" in descricao_minuscula:
    categoria = "Acesso ao sistema"
    prioridade = "Média"
    encaminhamento = "Suporte de sistemas"
    resposta_cliente = "Vamos verificar seu acesso, usuário, senha e permissões no sistema."

elif "internet" in descricao_minuscula or "rede" in descricao_minuscula or "wifi" in descricao_minuscula or "wi-fi" in descricao_minuscula:
    categoria = "Rede ou internet"
    prioridade = "Alta"
    encaminhamento = "Suporte de redes"
    resposta_cliente = "Vamos verificar a conexão, sinal de rede, cabos, Wi-Fi e configurações básicas."

elif "lento" in descricao_minuscula or "travando" in descricao_minuscula or "demora" in descricao_minuscula:
    categoria = "Desempenho do computador"
    prioridade = "Média"
    encaminhamento = "Suporte técnico"
    resposta_cliente = "Vamos verificar o desempenho do equipamento, programas em execução e possíveis causas de lentidão."

elif "instalar" in descricao_minuscula or "instalação" in descricao_minuscula or "programa" in descricao_minuscula:
    categoria = "Instalação de programa"
    prioridade = "Baixa"
    encaminhamento = "Suporte técnico"
    resposta_cliente = "Vamos analisar a solicitação de instalação e verificar permissões, compatibilidade e necessidade do programa."

elif "vírus" in descricao_minuscula or "virus" in descricao_minuscula or "phishing" in descricao_minuscula or "segurança" in descricao_minuscula:
    categoria = "Segurança da informação"
    prioridade = "Alta"
    encaminhamento = "Equipe de segurança da informação"
    resposta_cliente = "Vamos tratar a situação com prioridade, verificando possíveis riscos de segurança e orientações preventivas."

print("\n=== Análise do Chamado ===")
print("Usuário:", nome)
print("Setor:", setor)
print("Descrição:", descricao)
print("Categoria sugerida:", categoria)
print("Prioridade sugerida:", prioridade)
print("Encaminhamento sugerido:", encaminhamento)

print("\n=== Resposta inicial ao cliente ===")
print("Olá,", nome + "!")
print(resposta_cliente)
print("Seu chamado foi registrado com sucesso e será acompanhado pela equipe responsável.")
