'''18.Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho = int(input('Qual o Tamanho do arquivo para Download em MBs: '))
velocidade = int(input('Qual e a Velocidade o seu Link de Internet em Mbps: '))
velocidade_mgbs = velocidade / 8
tempo_download = (tamanho / velocidade_mgbs) / 60
print('\n')
print('-'*40)
print('Com um link de {}Mbps a Velocidade o seu Download para o arquivo de {} será de {} Minutos'.format(velocidade,tamanho,tempo_download))
print('-'*40)
    