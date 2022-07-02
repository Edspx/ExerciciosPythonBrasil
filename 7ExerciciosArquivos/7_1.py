"""
1. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um
relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4
[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256"""
path = ('D:\\Eder\\OneDrive\\Scripts Biblioteca\\Python\\ExerciciosPythonBrasil\\7.ExerciciosArquivos\\')
arquivo = open(path+'ips.txt')
ip = None
ip_valido = []
ip_invalido = []
for i in arquivo:
    ip = i.strip()
    range_ip = ip.count('.')
    if range_ip == 3:
        rede_classe  = int(ip.split('.')[0])
        host1 = int(ip.split('.')[1])
        host2 = int(ip.split('.')[2])
        host3 = int(ip.split('.')[3])
    
        if rede_classe >= 1 and rede_classe <= 126:
            #IP Classe A
            if (host1 >=0 and host1 <= 255) and (host2 >=0 and host2 <= 255) and (host3 >=0 and host3 <= 255):
                if (host1+host2+host3) != '000':
                    ip_valido.append(ip)
                else:
                    ip_invalido.append(ip)
            else:
                ip_invalido.append(ip)
            
        elif rede_classe >= 128 and rede_classe <= 191:
            #IP Classe B
            if (host1 >=0 and host1 <= 225) and (host2 >=0 and host2 <= 255) and (host3 >=0 and host3 <= 255):
                if (host2+host3) != '00':
                    ip_valido.append(ip)
                else:
                    ip_invalido.append(ip)
            else:
                ip_invalido.append(ip)

        elif rede_classe >= 192 and rede_classe <= 223:
            #IP Classe c
            if (host1 >=0 and host1 <= 225) and (host2 >=0 and host2 <= 225) and (host3 >=1 and host3 <= 254):
                ip_valido.append(ip)
            else:
                ip_invalido.append(ip)
        else:
            ip_invalido.append(ip)

    else:
        #IP Invalido por numero de casas
        ip_invalido.append(ip)

file_output = 'relatorio_ips.txt'
arquivo = open(path+file_output, 'w')

arquivo.write('[Endereços válidos:]')
arquivo.write('\n')
for i in ip_valido:
    arquivo.write(i)
    arquivo.write('\n')

arquivo.write('\n')
arquivo.write('[Endereços inválidos:]')
arquivo.write('\n')
for i in ip_invalido:
    arquivo.write(i)
    arquivo.write('\n')

arquivo.close() 


