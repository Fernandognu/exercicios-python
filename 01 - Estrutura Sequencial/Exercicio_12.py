#### Exercício 12

#### Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

#### ```math title="Formula"
#### Gigabytes * 1024
#### ```

# Solicita ao usuário o tamanho do arquivo em Gigabytes
gigabytes = float(input("Digite o tamanho do arquivo em Gigabytes: "))
# Converte Gigabytes para Megabytes
megabytes = gigabytes * 1024
# Exibe o resultado
print(f"O tamanho do arquivo em Megabytes é: {megabytes} MB")