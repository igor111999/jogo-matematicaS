import random

def jogo_subtracao():
    """
    Um jogo de subtração simples para praticar matemática.
    """
    pontuacao = 0
    tentativas = 0
    print("Bem-vindo ao Jogo de Subtração!")
    print("Tente resolver o máximo de subtrações que conseguir.")

    # O loop principal do jogo continua indefinidamente até o usuário decidir parar
    while True:
        # Gera dois números aleatórios entre 1 e 100
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        # Garante que o primeiro número seja maior ou igual ao segundo para evitar resultados negativos neste exemplo simples
        if num1 < num2:
            num1, num2 = num2, num1

        resposta_correta = num1 - num2

        try:
            # Pede a resposta do usuário
            resposta_usuario = int(input(f"Qual é o resultado de {num1} - {num2}? "))
            
            tentativas += 1

            # Verifica se a resposta está correta
            if resposta_usuario == resposta_correta:
                print("Correto! 🎉")
                pontuacao += 1
            else:
                print(f"Incorreto. A resposta correta era {resposta_correta}. 😢")

        except ValueError:
            # Lida com entradas não numéricas
            print("Entrada inválida. Por favor, insira um número inteiro.")
            continue # Continua para a próxima iteração do loop, sem contar como tentativa válida

        # Pergunta ao usuário se deseja continuar jogando
        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != 's':
            print(f"Fim de jogo! Sua pontuação final foi: {pontuacao} de {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_subtracao()

