from os import system
from datetime import datetime

print('Início da execução {}'.format(datetime.now().strtime('%d-%m%Y %H:%M:%S')))
system('apt-get uptdade')