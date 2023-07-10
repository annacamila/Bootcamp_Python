import processalista

# relação dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano',
         'Julieta', 'Maria', 'Fernando', 'Cláudio']
# estrutura que irá armazenar o número de letras de cada nome
qtd_letras = {}
# calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
for nome in nomes:
    qtd_letras[nome] = len(nome)

qtd_letras = {nome: len(nome) for nome in nomes}
print(qtd_letras)


def area(r, pi=3.14):
    return pi * (r ** 2)


# Utilização da função sem declarar pi
# Neste caso o valor de pi será 3.14
print(area(8))  # Resultado: 3.14 * (8 ** 2)
# Utilização da função declarando explicitamente o valor de pi
# Neste caso o valor de pi será 3.141592
print(area(8, 3.141592))  # Resultado: 3.141592 * (8 ** 2)


def area(r, pi=3.14): return pi * (r ** 2)


print(area(8))  # Utilização da função sem declarar pi (valor padrão de 3.14)
# Utilização da função declarando explicitamente o valor de pi
print(area(8, 3.141592))


lista_numeros = [2, 5, 9, 4, 7, 12]

maior = processalista.maior_impar(lista_numeros)
print("Maior número ímpar:", maior)

menor = processalista.menor_impar(lista_numeros)
print("Menor número ímpar:", menor)

maior, menor = processalista.maior_e_menor_impar(lista_numeros)
print("Maior número ímpar:", maior, "Menor número ímpar:", menor)


# Relação de dias da semana que cada médico atende
cardiologista = {'terca', 'quarta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}


def disp_dois_especialistas(medico01, medico02):
    dias_disponiveis = medico01.intersection(medico02)
    return dias_disponiveis


def disp_tres_especialistas(medico01, medico02, medico03):
    dias_disponiveis = medico01.intersection(medico02, medico03)
    return dias_disponiveis


dias_disponiveis_dois_medicos = disp_dois_especialistas(
    ortopedista, neurologista)
print("Dias disponíveis para dois médicos:", dias_disponiveis_dois_medicos)

dias_disponiveis_tres_medicos = disp_tres_especialistas(
    dermatologista, neurologista, psiquiatra)
print("Dias disponíveis para três médicos:", dias_disponiveis_tres_medicos)
