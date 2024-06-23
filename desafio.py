# 1 - Solicite ao usuário que digite seu nome
var_nome_usuario = input('Digite seu nome: ')

# 2 - Solicite ao usuário que digite o valor de seu salário
    # Converte a entrada para um número de ponto flutuante
var_salario_usuario = float(input('Digite seu salário: '))

# 3 - Solicite ao usuário que digite o valor do bônus recebido
    # Converte a entrada para um número de ponto flutuante
var_bonus_usuario = float(input('Digite o valor do bônus recebido: '))

# 4 - Calcule o valor do bônus final
CONSTANTE_BONUS = 1000
var_kpi_bonus_usuario = CONSTANTE_BONUS + var_salario_usuario * var_bonus_usuario

# 5 - Imprima o cálculo do KPI para o usuário
print(var_kpi_bonus_usuario)

# 6 - Imprime uma mensagem personalizada incluindo o nome do usuário
print(f"O usuário {var_nome_usuario} possui o bonus de {var_kpi_bonus_usuario}")