import os
from time import sleep
import sys
sys.path.append(os.path.realpath("."))
import inquirer
# -------------------------------------------------------
class Computador:
    def __init__(self, processador, memoriaRam, placaVideo, fonte, placaMae):
        self.__processador = processador
        self.__memoriaRam = memoriaRam
        self.__placaVideo = placaVideo
        self.__fonte = fonte
        self.__placaMae = placaMae
        
    def get_processador(self):
        return self.__processador
    def set_processador(self,processador):
        self.__processador = processador
    def get_memoria(self):
        return self.__memoriaRam
    def set_memoria(self,memoriaRam):
        self.__memoriaRam = memoriaRam
    def get_placaV(self):
        return self.__placaVideo
    def set_placaV(self,placaVideo):
        self.__placaVideo = placaVideo  
    def get_fonte(self):
        return self.__fonte
    def set_fonte(self, fonte):
        self.__fonte = fonte
    def get_placaM(self):
        return self.__placaMae
    def set_placaM(self, placaMae):
        self.__placaMae = placaMae
        
    def falar(self):
        print('Listando...')
        
computador = Computador('','','','','')

os.system('cls')

processador = input('\n🔍Informe o processador: ')
computador.set_processador(processador)
placaVd = input('\n🔍Informe a Placa de Vídeo: ')
computador.set_placaV(placaVd)
fonte = input('\n🔍Informe a Fonte: ')
computador.set_fonte(fonte)
placamae = input('\n🔍Informe a Placa Mãe: ')
computador.set_placaM(placamae)

sleep(1)
os.system('cls')

computador.falar()
print('\n📋Itens:')
print(f'\t✒️ Processador: {computador.get_processador()}\n\t✒️ Placa de Vídeo: {computador.get_placaV()}\n\t✒️ Fonte para o computador: {computador.get_fonte()}\n\t✒️ Placa Mãe: {computador.get_placaM()}\n')

sleep(1)
os.system('cls')

funcionamento_on_off = [
    inquirer.List(
        'Computador',
        message='\33[35mComputador\33[m',
        choices=['on', 'off'],
    ),
]
answers = inquirer.prompt(funcionamento_on_off)['Computador']
if answers == 'on':
    print('Ligando computador..') 
else:
    print('Computador desligado.')
