"""
2. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o
seguinte arquivo, chamado "usuarios.txt":
alexandre 456123789
anderson 1245698456
antonio 123456456
carlos 91257581
cesar 987458
rosemary 789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um
relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc. Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr. Usuário Espaço utilizado % do uso
1 alexandre 434,99 MB 16,85%
2 anderson 1187,99 MB 46,02%
3 antonio 117,73 MB 4,56%
4 carlos 87,03 MB 3,37%
5 cesar 0,94 MB 0,04%
6 rosemary 752,88 MB 29,16%
09/10/2020 ExerciciosArquivos - PythonBrasil
https://wiki.python.org.br/ExerciciosArquivos 2/2
Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de
forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser
feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também
deverá ser feito através de uma função, que será chamada pelo programa principal.
Voltar para a ListaDeExercicios
Sobre esta página
ExerciciosArquivos (editada pela última vez em 2008-09-26 14:07:41 por localhost)
Visualizar Texto | Visualizar Impressão | Information | Fazer Usuário Acompanhar | Anexos
"Python" e os logos de Python são marcas registradas da Python Software Foundation, usadas aqui mediante permissão da mesma. O conteúdo
deste site está disponível sob os termos da Creative Commons Attribution 2.5 exceto quando explicitamente especificado outra licença."""
import re
path = ('D:\\Eder\\OneDrive\\Scripts Biblioteca\\Python\\ExerciciosPythonBrasil\\7.ExerciciosArquivos\\')
arquivo = open(path+'usuarios.txt')
   


def byte_to_megabyte(byte):
    r = round(byte/1024/1024,2)
    return r

def percentual_ocupado(usuario = 0, disco = 0):
    r = round(usuario/disco * 100,2) 
    return r

user = None
size = None
usuario = []
armazenamendo_byte = []
armazenamendo_mb = []
percentual_ocupado_mb = []


for i in arquivo:
    n = re.search(r'\w+', i.strip())
    s = re.search(r'\d+', i.strip())
    user = n.group()
    size = s.group()
    usuario.append(user)
    armazenamendo_byte.append(int(size))


for i in armazenamendo_byte:
    armazenamendo_mb.append(byte_to_megabyte(i))

soma_mb = sum(armazenamendo_mb)

for i in armazenamendo_mb:
    percentual_ocupado_mb.append(percentual_ocupado(i,soma_mb))

print(usuario)
print(armazenamendo_byte)
print(armazenamendo_mb)
print(percentual_ocupado_mb)

relatorio = open(path+'relatório.txt', 'w')
relatorio.write('ACME Inc.               Uso do espaço em disco pelos usuários')
relatorio.write('\n')
relatorio.write('\n')
for i in range(72):
    relatorio.write('-')

relatorio.write('\n')
relatorio.write('\n')

titulo = 'Nr.  Usuário        Espaço utilizado     % do uso\n'
relatorio.write(titulo)
relatorio.write('\n')
n = 0
for i in range(len(usuario)):
    n += 1
    relatorio.write(str(n))
    for a in range(4):
        relatorio.write(' ')
    relatorio.write(usuario[i])

    mb = str(armazenamendo_mb[i]) + ' MB'
    t_espaco_user = 28 - (len(usuario[i]) + len(mb))
    for b in range(t_espaco_user):
        relatorio.write(' ')
    relatorio.write(mb)

    percent = str(percentual_ocupado_mb[i]) + '%'
    t_espaco_user = 16 - len(percent)
    for b in range(t_espaco_user):
        relatorio.write(' ')
    relatorio.write(percent)
    relatorio.write('\n')

relatorio.write('\n')
total_mb ='Espaço total ocupado: '+ str(sum(armazenamendo_mb) )+ ' MB\n'
media_mb ='Espaço médio ocupado:  '+ str(round(sum(armazenamendo_mb) / len(armazenamendo_mb),2)) + ' MB\n'
relatorio.write(total_mb)
relatorio.write(media_mb)
relatorio.close()