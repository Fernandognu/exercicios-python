#### Exercício 18

#### Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# Solicita o tamanho do arquivo em MB
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
# Solicita a velocidade do link de Internet em Mbps
velocidade_link_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))
# Converte a velocidade de Mbps para MBps (1 byte = 8 bits)
velocidade_link_mbps_em_MBps = velocidade_link_mbps / 8
# Calcula o tempo de download em segundos
tempo_download_segundos = tamanho_arquivo_mb / velocidade_link_mbps_em_MBps
# Converte o tempo de download para minutos
tempo_download_minutos = tempo_download_segundos / 60
# Exibe o tempo aproximado de download em minutos
print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")