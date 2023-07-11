import pandas as pd

# Carregar o dataset
df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")

tamanho_dataset = df.shape
print("Tamanho do dataset:", tamanho_dataset)

media_windspeed = df['windspeed'].mean()
print("Média da coluna windspeed:", media_windspeed)

media_temp = df['temp'].mean()
print("Média da coluna temp:", media_temp)

registros_2011 = df['year'].value_counts()[0]
print("Número de registros para o ano de 2011:", registros_2011)

registros_2012 = df['year'].value_counts()[1]
print("Número de registros para o ano de 2012:", registros_2012)

locacoes_2011 = df.loc[df['year'] == 0, 'total_count'].sum()
print("Total de locações de bicicletas em 2011:", locacoes_2011)

locacoes_2012 = df.loc[df['year'] == 1, 'total_count'].sum()
print("Total de locações de bicicletas em 2012:", locacoes_2012)

estacao_maior_media = df.groupby('season')['total_count'].mean().idxmax()
print("Estação do ano com a maior média de locações de bicicletas:",
      estacao_maior_media)

estacao_menor_media = df.groupby('season')['total_count'].mean().idxmin()
print("Estação do ano com a menor média de locações de bicicletas:",
      estacao_menor_media)

horario_maior_media = df.groupby('hour')['total_count'].mean().idxmax()
print("Horário do dia com a maior média de locações de bicicletas:",
      horario_maior_media)

horario_menor_media = df.groupby('hour')['total_count'].mean().idxmin()
print("Horário do dia com a menor média de locações de bicicletas:",
      horario_menor_media)

dia_semana_maior_media = df.groupby('weekday')['total_count'].mean().idxmax()
print("Dia da semana com a maior média de locações de bicicletas:",
      dia_semana_maior_media)

dia_semana_menor_media = df.groupby('weekday')['total_count'].mean().idxmin()
print("Dia da semana com a menor média de locações de bicicletas:",
      dia_semana_menor_media)

horario_quartas_maior_media = df.loc[df['weekday'] == 3].groupby('hour')[
    'total_count'].mean().idxmax()
print("Horário do dia com a maior média de locações de bicicletas às quartas-feiras:",
      horario_quartas_maior_media)

horario_sabados_maior_media = df.loc[df['weekday'] == 6].groupby('hour')[
    'total_count'].mean().idxmax()
print("Horário do dia com a maior média de locações de bicicletas aos sábados:",
      horario_sabados_maior_media)

