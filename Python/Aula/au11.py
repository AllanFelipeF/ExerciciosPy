''' 
Padrão ANSI(escape sequence) - padrão de normalização internacional
Tudo em ANSI começa com \ 
Codigo para cores(melhor para python é 033)
\033[m < codigo para cores, entre o [ e o m é onde eu coloco os parametros de Style, text e background, para console.
exemplo de codigo: \033[0:33:44m
Abaixo será os códigos que melhores funcionam para cada um dos parametros na console:
    Style:
        0: none
        1: bold
        4: underline
        7: negative(inverte as configurações, o que eu coloquei pra letra, vai pra fundo e o que eu coloquei pra fundo vai pra letra)
    Text:
        30: branco
        31: vermelho
        32: verde
        33: amarelo
        34: azul
        35: magenta
        36: ciano
        37: cinza
    background:
        40: branco
        41: vermelho
        42: verde
        43: amarelo
        44: azul
        45: magenta
        46: ciano
        47: cinza
'''
print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[1;30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')