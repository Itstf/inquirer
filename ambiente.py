from time import sleep
from tqdm import tqdm
import time
import os
import sys
sys.path.append(os.path.realpath("."))
import inquirer  
# -------------------------------------------------------
class Ambiente():
    def __init__(self, som, iluminacao):
        self.__som = som
        self.__iluminacao = iluminacao
        
    def get_som(self):
        return self.__som
    def set_som(self, som):
        self.__som = som
    def get_iluminacao(self):
        return self.__iluminacao
    def set_iluminacao(self, iluminacao):
        self.__iluminacao = iluminacao
        
    def falar(self):
        print('\33[33mPREPARANDO O AMBIENTE. . . . .\33[m')
        sleep(0.5)
        for i in tqdm(range(5)):
            time.sleep(0.2)
        sleep(0.5)
        os.system('cls')

ambiente = Ambiente('','')

ambiente.falar()

som = [
    inquirer.List(
        'Barulho do Ambiente',
        message="\33[35mComo está o som do ambiente?\33[m",
        choices=['Barulheira', 'Silêncio', 'Mediano'],
    ),
]

answers = inquirer.prompt(som)['Barulho do Ambiente']
ambiente.set_som(som)
if answers == 'Barulheira':
    print('Você não irá conseguir se concentrar! Espere tudo ficar mais calmo')
elif answers == 'Silêncio':
    print('\33[95mColocando um lofi . . .\33[m' )
    sleep(0.5) 
    print('Pronto para programar!@~')
elif answers == 'Mediano':
    concentrar = int(input('''\33[35mVocê vai conseguir se concentrar na programação?\33[m 
                           [1]Sim
                           [2]Não
                           '''))
    if concentrar == 1:
        print(f'Som ao redor: \33[32m{answers}\33[m.')
        sleep(1) 
        print('Começando a codar. . .')
    else:
        sleep(1)
        os.system('cls')
        print('Espere um pouco para começar, programe com vontade, paciência e calma.')
