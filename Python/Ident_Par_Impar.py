def check_parity(number):
    if number % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
number_typed = int(input("Digite um número inteiro: "))
output_result = check_parity(number_typed)
print(f"\nO número {number_typed} é: {output_result}.")