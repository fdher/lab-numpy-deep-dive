import random
import string
import re
import numpy as np
DictPreguntasRespuestasPop={'Las galletas Oreo son más antiguas que las galletas de chips de chocolate':'Verdadero, Oreo fue inventado en 1912',
'Napoleon Bonaparte era extremadamente bajo':'Falso, Aunque mucha gente cree que era bajito media 1.70 m','El protagonista de One Piece se llama Monkey D Adame':'Falso, Se llama Monkey D Luffy',
'Los conejos son roedores':'Falso, Los conejos son lagomorfos','La muralla China se ve desde el espacio':'Falso, Aunque muchos creen que se ve desde el espacio solamente alcanza a verse a una altitud de 36km',
'Los encendedores fueron inventados antes que los cerillos':'Verdadero, Los encendedores fueron inventados en 1823 mientras que los cerrillos en 1826',
'Will Smith progatonizo Matrix':'Falso, Es protagonizada por Keanu Reeves','El personaje de Goku estuvo inspirado por un mono':'Verdadero, Akira Toriyama se inspiro en un mono para crear a Goku',
'La gema verde del infinito representa el poder':'Falso, Representa el tiempo','El creador de Bob Esponja es un cientifico':'Verdadero, Stephen Hillenburg fue Biologo Marino',
'El guitarrista de Led Zeppelin se llama Slash':'Falso, Se llama Jimmy Page','Krillin murio un total de 3 veces en Dragon Ball Z':'Verdadero, Krillin murio un total de 3 veces',
'El protagonista de Death Note se llama Night':'Falso, Se llama Light','Cristiano Ronaldo es conocido como el Comandante':'Verdadero, SIIIIIIUUUUUUU'}
DictPreguntasRespuestasCiencia = {"¿El cuerpo humano tiene 206 huesos?":"VERDADERO, Tenemos 206 huesos articulados entre sí", 
"¿Durante la fotosíntesis las plantas transforman O2 en azúcares?":"FALSO, En realidad transforman en CO2 en O2",
"¿Es verdad que existen entre 700 y 900 especies de dinosaurios?": "VERDADERO, Sin embargo solo la mitad se basan en muestras completas", 
"¿El cerebro es el órgano que consume más energía":"VERDADERO, El cerebro consume más del 20% de la energía que generamos", 
"¿La ballena jorobada es el animal más grande del mundo?":"FALSO, se trata de la ballena azul con 29 m de largo.", 
"¿El Sol es el planeta más grande del sistema?":"FALSO, el Sol no es un planeta, si no una estrella", 
"¿El Germanio es un elemento de la tabla periódica?":"VERDADERO, Es un elemento químico con número atómico 32, y símbolo Ge ", 
"¿Los cloroplastos se encuentran dentro del núcleo de la célula vegetal?": "FALSO, Se encuentran distribuidos en el citoplasma",
"¿El núcleo es el centro de un átomo?":"VERDADERO, Está compuesto de protones y neutrones, y posee casi la totalidad de la masa del átomo. ", 
"¿Una batería convierte energía química en energía eléctrica?": "FALSO, es al contrario", 
"¿El Hidrógeno es el segundo elemento menos denso de la tabla periódica?": "FALSO, en realidad es el menos denso" , 
"¿El ornitorrinco es un mamífero?": "VERDADERO, Es una especie de mamífero semiacuático", 
"¿Las bases nitrogenadas de los nucleótidos son moléculas inorgánicas?":"FALSO, Son moléculas orgánicas",
"¿Las secuencia de DNA generalmente se transcriben en dirección 5'3'?":"VERDADERO, Significa que el nucleótido del extremo 5' es el primero y el  del extremo 3' el úlitmo." ,
"¿Los -273°C es la temperatura más baja que se puede alcanzar?": "VERDADERO, es el cero absoluto en la escala Kelvin"}
def NuevoJuego(): #funcion main
    guesses=[]
    numcorrectos=0
    num_pregunta=0
    error = 0
    print("Bienvenido a IronTrivia!\n")
    while True:
        nombre= input("Por favor, coloca tu nombre: ")
        if nombre.isalpha()== True:
            print(f"Hola {nombre}!")
            break
        else:
            print("Nombre no válido")
                
    print(f"Elige el tema de tu preferencia:\n\
           Presiona 1 para Ciencias.\n\
           Presiona 2 para Cultura Pop.\n\
           Presiona 0 para salir.")
    choice=input("")
    if choice=="1":
        print("Has seleccionado preguntas de Ciencia!")
        #guess=input('Porfavor inserta verdadero o falso ')
        pregunta=np.random.choice(list(DictPreguntasRespuestasCiencia.keys()),10)
        for keys in pregunta:
            if numcorrectos<3:
                print('-'*20)
                print(keys)
                while True:
                    guess=input('Verdadero o Falso?               ')
                    if guess.isalpha():
                        guess=guess.upper()
                        guesses.append(guess)
                        if check_answer(DictPreguntasRespuestasCiencia.get(keys),guess)==1:
                            numcorrectos+=1 #Acumula las wins
                        else:
                            error+=1
                        print(f'Tienes {numcorrectos} puntos')
                        print(error)
                        if error==3:
                            print("Perdiste!")
                            respuesta=input("Quieres jugar de nuevo? (y/n)")
                            respuesta=respuesta.upper()
                            if respuesta=='Y':
                                return NuevoJuego()
                            else:
                                print("Gracias por jugar!")
                        break
                    else:
                        print("Caracter no valido")
        print("Ganaste!")
        respuesta=input("Quieres jugar de nuevo? (y/n)")
        respuesta=respuesta.upper()
        if respuesta=='Y':
            return NuevoJuego()
        else:
            print("Gracias por jugar!")
                    
    elif choice=="2":
        print("Has seleccionado preguntas pop!")
        pregunta=np.random.choice(list(DictPreguntasRespuestasPop.keys()),8)
        for keys in pregunta:
        
            #random.choice(print(DictPreguntasRespuestas.keys()))
            print('-'*20)
            print(keys)
            while True:
                guess=input('Verdadero o Falso?      ')
                if guess.isalpha():
                    guess=guess.upper()
                    guesses.append(guess)
                    numcorrectos+=check_answer(DictPreguntasRespuestasPop.get(keys),guess) #Acumula las wins
                    print(f'Tienes {numcorrectos} puntos')
                    num_pregunta+=1
                    break
                else:
                    print("Caracter no valido")
    else:
        print("Gracias por jugar!")
        
def check_answer(answer,guess):
    if guess.upper() in answer.upper():
        y=answer.split(", ")
        print("Correcto!",y[1])
        return 1
    else:
        y=answer.split(", ")
        print("Incorrecto!",y[1])
        return 0
    
NuevoJuego()