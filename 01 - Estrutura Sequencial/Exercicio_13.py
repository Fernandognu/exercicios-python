#### Exercício 13

#### Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

#### - Para Megabytes: `Gigabytes * 1024`
#### - Para Kilobytes: `Gigabytes * 1024 * 1024`

#### Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

# Solicita ao usuário o tamanho do arquivo em Gigabytes
gigabytes = float(input("Digite o tamanho do arquivo em Gigabytes: "))
# Converte Gigabytes para Megabytes
megabytes = gigabytes * 1024
# Converte Gigabytes para Kilobytes
kilobytes = gigabytes * 1024 * 1024
# Exibe os resultados
print(f"Tamanho do arquivo em Megabytes: {megabytes} MB")
print(f"Tamanho do arquivo em Kilobytes: {kilobytes} KB")
