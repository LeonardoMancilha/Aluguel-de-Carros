KM = float(input('\033[7;30;47mDigite a quantidade de Km (quilômetros) percorridos pelo carro'))
dias = int(input('Digite a quantidade de dias pelo qual o carro foi alugado'))
print('O carro percorreu\033[7;30;44m {}Km\033[7;30;47m em \033[7;30;43m{} Dia(s)\033[7;30;47m e devera pagar um total de \033[7;30;41mR${:.2f}\033[m'.format(KM, dias, (0.15 * KM) + (60 * dias)))
