import sys
import string
from itertools import combinations_with_replacement
import time

def main(args):

    valors = string.ascii_letters
    valors = string.digits
    valors = string.punctuation
    tamanho = 8

    ini_t = time.time()
    gerar_senhas(valors, tamanho)
    fin_t = time.time()

    print(f"Tempo: {str(fin_t - ini_t)}s")

def gerar_senhas(valors, tamanho):
    comb = combinations_with_replacement(valors, tamanho)
    print(f"Combinações: {len(list(comb))}")
if __name__ == '__main__':
    main(sys.argv[1:])

