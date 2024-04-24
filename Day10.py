# Logo do aplicativo calculadora
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# Imprime o logo da calculadora
print(logo)

# Flag para continuar o loop principal
keep_going = True

# Funções para as operações matemáticas básicas
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero.")  # Correção para divisão por zero
    return n1 / n2

# Dicionário que associa símbolos de operações com suas respectivas funções
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

#Calculadora
def calculator():
    keep_going = True

    # Solicita ao usuário para digitar o primeiro número
    while True:
        n1 = input("Type the first number: ")
        
        if n1.isnumeric():  # Verifica se é um número
            n1 = int(n1)  # Converte para inteiro
            break
        else:
            print("Please enter only numbers.")  # Mensagem para entrada inválida

    # Loop principal da calculadora
    while keep_going:
        while True:
            # Exibe as operações disponíveis
            for ops in operations:
                print(ops)
            # Solicita que o usuário selecione uma operação
            selected_operation = input("Select one operation above: ")
            if not selected_operation in operations:  # Verifica se a operação é válida
                print("Select a valid operation.")  # Mensagem para entrada inválida
            else:
                break
                    
        # Solicita ao usuário para digitar o próximo número
        while True:
            n2 = input("Type the next number: ") 
            if n2.isnumeric():  # Verifica se é um número
                n2 = int(n2)  # Converte para inteiro
                break
            else:
                print("Please enter only numbers.")  # Mensagem para entrada inválida

        # Realiza a operação selecionada
        calculation = operations[selected_operation]
        result = calculation(n1, n2)  # Calcula o resultado

        # Exibe o resultado da operação
        print(f"{n1} {selected_operation} {n2} = {result}")
        
        # Atualiza o valor do primeiro número para o resultado
        n1 = result

        # Pergunta se o usuário deseja continuar
        keep = input("Type [y] if you want to continue calculating, Type [c] if you want to start a new calculation or anything else to stop: ").lower()
        
        # Verifica se o usuário deseja parar
        if keep == "y":  
            print("\nKeep going\n")
        elif keep == "c":
            print("\nStarting a new calculator...\n")
            keep_going = False
            calculator()
        else:
            print("\nBye!")
            keep_going = False

calculator()