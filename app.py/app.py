# Quantidade de entrevistados
TOTAL_ENTREVISTADOS = 10

# Contadores de opiniões
excelente = 0
bom = 0
ruim = 0

print("=" * 45)
print("       TUDOWEB - PESQUISA DE SATISFAÇÃO")
print("=" * 45)
print(f"Quantidade de entrevistados: {TOTAL_ENTREVISTADOS}\n")

# Repetição para coletar as respostas
for i in range(1, TOTAL_ENTREVISTADOS + 1):

    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")

    # Coleta dos dados
    nome = input("Digite seu nome: ")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade > 0:
                break
            print("A idade deve ser maior que zero.")
        except ValueError:
            print("Digite uma idade válida.")

    # Coleta e validação da opinião
    while True:
        print("\nComo você avalia nosso atendimento?")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")

        try:
            opiniao = int(input("Digite sua opção (1, 2 ou 3): "))

            if opiniao in [1, 2, 3]:
                break
            else:
                print("Opção inválida! Escolha 1, 2 ou 3.")
        except ValueError:
            print("Digite apenas números.")

    # Estruturas de decisão para verificar a opinião
    if opiniao == 1:
        excelente += 1
        resposta = "EXCELENTE"
    elif opiniao == 2:
        bom += 1
        resposta = "BOM"
    else:
        ruim += 1
        resposta = "RUIM"

    # Exibição dos dados coletados
    print("\nResposta registrada com sucesso!")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Opinião: {resposta}")

# Relatório final da pesquisa
print("\n" + "=" * 45)
print("       RESULTADO FINAL DA PESQUISA")
print("=" * 45)
print(f"Total de entrevistados: {TOTAL_ENTREVISTADOS}")
print(f"Respostas EXCELENTE: {excelente}")
print(f"Respostas BOM: {bom}")
print(f"Respostas RUIM: {ruim}")
print("=" * 45)