perguntas = [
    ["Qual a capital da França?", "Paris", "Londres", "Berlim", "Roma", 1],
    ["Qual o resultado de 8 + 5?", "12", "13", "15", "18", 2],
    ["Quem pintou a Mona Lisa?", "Van Gogh", "Picasso", "Da Vinci", "Monet", 3]
]

pontuacao = 0

print("--- Bem-vindo ao Quiz! ---")

for i, pergunta in enumerate(perguntas):
    print(f"\nPergunta {i+1}: {pergunta[0]}")
    print(f"1. {pergunta[1]}")
    print(f"2. {pergunta[2]}")
    print(f"3. {pergunta[3]}")
    print(f"4. {pergunta[4]}")

    # Pega a resposta do usuário
    resposta_usuario = int(input("Digite o número da sua resposta (1-4): "))

    # Verifica a resposta
    indice_correto = pergunta[5]
    if resposta_usuario == indice_correto:
        print("Correto!")
        pontuacao += 1
    else:
        print(f"Errado! A resposta correta era: {pergunta[indice_correto]}")

print(f"\n--- Fim do Quiz ---")
print(f"Sua pontuação final: {pontuacao}/{len(perguntas)}")
