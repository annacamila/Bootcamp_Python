# declaração das variáveis
inicio = 0
fim = 100
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)

inicio = 100
fim = 501
for numero in range(inicio, fim):
    if numero % 2 == 0 and numero % 5 == 0 and numero % 7 == 0:
        print(numero)

divisor = 3
for numero in range(0, 1000, divisor):
    print(numero)

# variáveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

nome = nome.upper()
cidade = cidade.upper()
cpf = cpf.upper()
print(nome)
print(cidade)
print(cpf)

nome = nome.lower()
cidade = cidade.lower()
cpf = cpf.lower()
print(nome)
print(cidade)
print(cpf)

posicao_nome = nome.find('ã')
posicao_cidade = cidade.find('ã')
posicao_cpf = cpf.find('ã')
print("Posição de 'ã' em nome:", posicao_nome)
print("Posição de 'ã' em cidade:", posicao_cidade)
print("Posição de 'ã' em cpf:", posicao_cpf)

tamanho_nome = len(nome)
tamanho_cidade = len(cidade)
tamanho_cpf = len(cpf)
print("Número de caracteres em nome:", tamanho_nome)
print("Número de caracteres em cidade:", tamanho_cidade)
print("Número de caracteres em cpf:", tamanho_cpf)

cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
print(cpf)

numero = '127957'
soma = 0

for caractere in numero:
    valor = int(caractere)
    soma += valor
print("A soma dos caracteres é:", soma)
