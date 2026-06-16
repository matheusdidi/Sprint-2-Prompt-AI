# ==========================================
# GOODWE EV ASSISTANT
# ==========================================

print("=" * 50)
print("GOODWE EV ASSISTANT")
print("EV Challenge 2026")
print("=" * 50)
print("Digite 'sair' para encerrar.\n")

while True:

    pergunta = input("Você: ").lower()

    if pergunta == "sair":
        print("\nChat encerrado.")
        break

    elif ("compartilhamento" in pergunta or
          "compartilhar" in pergunta or
          "carregadores" in pergunta):

        print("""
GoodWe:
O sistema EV ChargeOps permite que vários moradores
utilizem os mesmos carregadores, registrando o consumo
individual de cada usuário.
""")

    elif ("energia" in pergunta or
          "pagamento" in pergunta or
          "faturamento" in pergunta):

        print("""
GoodWe:
Cada usuário pode ser cobrado de acordo com a energia
consumida durante suas sessões de carregamento.
""")

    elif ("historico" in pergunta or
          "histórico" in pergunta or
          "consumo" in pergunta):

        print("""
GoodWe:
O sistema mantém registros das recargas realizadas,
permitindo consulta do histórico de utilização.
""")

    elif ("recarga" in pergunta or
          "recargas" in pergunta):

        print("""
GoodWe:
Sim. Todas as sessões de carregamento podem ser
registradas para controle e auditoria.
""")

    elif ("vantagem" in pergunta or
          "beneficio" in pergunta):

        print("""
GoodWe:
A principal vantagem do EV ChargeOps é facilitar
o gerenciamento dos carregadores compartilhados
e o controle dos custos de energia.
""")

    elif ("sindico" in pergunta or
          "síndico" in pergunta):

        print("""
GoodWe:
O síndico pode acompanhar o uso dos carregadores
e verificar informações de consumo dos usuários.
""")

    else:

        print("""
GoodWe:
Desculpe, essa pergunta está fora do escopo do
EV ChargeOps. Posso responder dúvidas sobre:

- carregadores elétricos
- consumo de energia
- faturamento
- histórico de recargas
- compartilhamento de carregadores
""")
