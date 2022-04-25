import random
import time
contador_taches=0
contador_wins=0


sss
def borraConsola():
    os.system("cls" if os.name == 'nt' else 'clear')

def PreguntadosCiencia():
    print("Bienvenido", n,'es hora de jugar Preguntados ciencia')
    s=input('estas list@?')
    if s=='Si':
        
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Tiempo agotado')
    contador_taches=contador_taches+1
        
    

countdown(int(t))


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 10)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)

n=input('Dame un nombre ')
print('Hola',n,'Esto es un juego de preguntados, porfavor del siguiente menu elige el tema')
print('++'*5,'--'*5)

print('1','Ciencia','*'*10)
print('2','Cultura','*'*10)
d=input('Elegir tema')

#Llamas los prints, y despues que se elige el tema llamas a la funcion para limpiar pantalla y corres la funcion asociada a la series de preguntas
