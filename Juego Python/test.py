DictPreguntasRespuestas={'Las galletas Oreo son más antiguas que las galletas de chips de chocolate':'Verdadero, Oreo fue inventado en 1912',
'Napoleon Bonaparte era extremadamente bajo':'Falso, aunque mucha gente cree que era bajito, media 1.70 m','El protagonista de One Piece se llama Monkey D Adame':'Falso, se llama Monkey D Luffy',
'Los conejos son roedores':'Falso, los conejos son lagormorfos','La muralla China se ve desde el epsacio':'Falso, aunque muchos creen que se ve desde el espacio, solamente alcanza a verse a una altitud de 36km',
'Los encendedores fueron inventados antes que los cerillos':'Verdadero, los encendedores fueron inventados en 1823 mientras que los cerrillos en 1826',
'Will Smith progatonizo Matrix':'Falso, es protagonizada por Keanu Reeves','El personaje de Goku estuvo inspirado por un mono':'Verdadero, Akira Toriyama se inspiro en un mono para crear a Goku',
'La gema verde del infinito representa el poder':'Falso, representa el tiempo','El creador de Bob Esponja es un cientifico':'Verdadero, Stephen Hillenburg fue Biologo Marino',
'El guitarrista de Led Zeppelin se llama Slash':'Falso, se llama Jimmy Page','Krillin murio un total de 3 veces en Dragon Ball Z':'Verdadero, Krillin murio un total de 3 veces',
'El protagonista de Death Note se llama Night':'Falso, se llama Light','Cristiano Ronaldo es conocido como el Comandante':'Verdadero, SIIIIIIUUUUUUU'}

def NuevoJuego():
    guess=[]
    correcto=[]
    num_pregunta=0

    for key in DictPreguntasRespuestas:
        print(key)