# Lista de estudantes válidos com matrícula (pode ser carregada de um arquivo JSON em um sistema real)
estudantes_validos = [
    {"nome": "Ana Souza", "matricula": "987654", "curso": "Artes Cênicas"},
    {"nome": "Carlos Pereira", "matricula": "123789", "curso": "Educação Física"},
]

def verificar_estudante(matricula):
    return any(estudante['matricula'] == matricula for estudante in estudantes_validos)

def aplicar_desconto(preco, is_estudante):
    return preco * 0.5 if is_estudante else preco  # 50% de desconto para estudantes

def main():
    print("Bem-vindo ao sistema de venda de ingressos inteiros do Circo!")
    987654
    matricula = input("Digite sua matrícula: ")
    preco_ingresso = float(input("Digite o preço do ingresso inteiro: R$ "))
    
    is_estudante = verificar_estudante(matricula)
    preco_final = aplicar_desconto(preco_ingresso, is_estudante)

    if is_estudante:
        print("Você é um estudante validado. Desconto de 50% aplicado!")
    else:
        print("Você não é um estudante validado. Preço normal aplicado.")

    print(f"Preço final do ingresso: R$ {preco_final:.2f}")

if __name__ == "__main__":
    main()
