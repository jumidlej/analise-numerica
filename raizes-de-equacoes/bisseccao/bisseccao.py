import math
import numpy as np
from utils import solve_func
from utils import intervalo_zero

# Definir o número de casas de precisão pra fazer os cálculos
# Verificação de loop infinito? Limite de iterações?
def bisseccao(funcao, a, b, precisao=None, distancia_absoluta=None, distancia_relativa=None):
    # Garantir que existe uma raíz nesse intervalo
    if not intervalo_zero(funcao, a, b):
        return None, None

    # Inicialização
    it = []

    iteracao = 0
    f_a = solve_func(a, funcao)
    f_b = solve_func(b, funcao)
    d_absoluta = abs(a-b)
    if a != 0:
        d_relativa = abs((a-b)/a)
    else:
        d_relativa = None

    it.append([iteracao, a, b, f_a, f_b, d_absoluta, d_relativa])

    # Verificação de condição de parada (precisão/distância)
    # Se houver mais de uma condição, todas devem ser satisfeitas
    repeat = False
    if (distancia_absoluta != None and d_absoluta > distancia_absoluta):
        repeat = True
    if (a != 0 and distancia_relativa != None and d_relativa > distancia_relativa):
        repeat = True
    if (precisao != None and abs(f_a) > precisao and abs(f_b) > precisao):
        repeat = True

    while(repeat and abs(a-b) > 10**-12):
        iteracao += 1

        # Escolher uma metade
        c = (a+b)/2
        f_c = solve_func(c, funcao)

        if f_a*f_c < 0.0:
            b = c
            f_b = solve_func(b, funcao)
        else:
            a = c
            f_a = solve_func(a, funcao)
        
        d_absoluta = abs(a-b)
        if a != 0:
            d_relativa = abs((a-b)/a)
        else:
            d_relativa = None

        it.append([iteracao, a, b, f_a, f_b, d_absoluta, d_relativa])

        # Verificação de condição de parada (precisão/distância)
        # Se houver mais de uma condição, todas devem ser satisfeitas
        repeat = False
        if (distancia_absoluta != None and d_absoluta > distancia_absoluta):
            repeat = True
        if (a != 0 and distancia_relativa != None and d_relativa > distancia_relativa):
            repeat = True
        if (precisao != None and abs(f_c) > precisao):
            repeat = True
        
    # escolher o menor
    if abs(f_a) < abs(f_b):
        x = a
    else:
        x = b
    
    return x, it

# Definir o número de iterações necessárias
def iteracoes_bisseccao(a, b, distancia_absoluta):
    i = abs(a-b)
    n = (math.log(i)-math.log(distancia_absoluta))/math.log(2)
    return n

def main():
    input_txt = open('input-bisec.txt', 'r')
    output_txt = open('output-bisec.txt', 'w')
    np.set_printoptions(precision=6)
    np.set_printoptions(suppress=True)  

    for line in input_txt:
        if line[-1] == '\n':
            line = line[:-1]
        # output_txt.write(line+' ')
        line = line.split(',')
        func = line[0].split('=')[1]
        a = float(line[1].split('=')[1])
        b = float(line[2].split('=')[1])
        precisao = line[3].split('=')[1]
        distancia_absoluta = line[4].split('=')[1]
        distancia_relativa = line[5].split('=')[1]
        if precisao == 'None':
            precisao = None
        else:
            precisao = float(line[3].split('=')[1])
        if distancia_absoluta == 'None':
            distancia_absoluta = None
        else:
            distancia_absoluta = float(line[4].split('=')[1])
        if distancia_relativa == 'None':
            distancia_relativa = None
        else:
            distancia_relativa = float(line[5].split('=')[1])

        x, iteracoes = bisseccao(func, a, b, precisao, distancia_absoluta, distancia_relativa)
        if x != None:
            iteracoes = np.asarray(iteracoes)
            # Verificação
            f_x = solve_func(x, func)
            x = np.asarray([x])
            f_x = np.asarray([f_x])
            output_txt.write("iteracoes="+str(len(iteracoes))+",x="+str(x)+",f(x)="+str(f_x)+'\n')
        else:
            print("intervalo inválido")
            output_txt.write("intervalo invalido\n")

    input_txt.close()
    output_txt.close()

main()