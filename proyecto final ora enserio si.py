import random
import time

a =[]
h =[]
e =[]
g =[]
#Preguntas de cada categoría
preg_arte = [
['¿Quién pintó las escenas bíblicas de la Capilla Sixtina?','a)Miguel Ángel\tb)Claude Monet\tc)Da Vinci','a'],
['Es un color primario','a)rojo\tb)naranja\tc)rosa','a'],
['Fue el pintor del famoso retrato "La Mona Lisa"','a)Paulo Coelho\tb)Vincent van Gogh\tc)Da Vinci','c'],
['¿Quién escribió "Cien años de soledad"?','a)Oscar Wilde\tb)Gabriel García Márquez\tc)Julio Cortázar','b'],
['Ciudad considerada como la ciudad de la moda','a)Los Angeles\tb)Londres\tc)París','c']]
preg_hist = [
['¿Qué civilación antigua inventó el papel y la pólvora?','a)Egipto\tb)China\tc)Olmeca','b'],
['¿Cómo se escribe el número 10 en números romanos?','a)X\tb)V\tc)L','a'],
['¿En qué año llegó Cristóbal Colón a América?','a)1942\tb)1492\tc)1785','b'],
['¿Quién es considerado como el padre de la Patria?','a)Vicente Guerrero\tb)Andrés Manuel\tc)Miguel Hidalgo','c'],
['Presidente que duró más de 30 años en el poder','a)Porfirio Díaz\tb)Felipe Calderón\tc)Benito Juárez','a']]
preg_ent = [
['¿A qué banda pertenecía John Lennon?','a)The Beatles\tb)The Strokes\tc)KISS','a'],
['¿Cómo se llama el personaje principal de Nintendo?','a)Kirby\tb)Mickey Mouse\tc)Mario','c'],
['¿Quién es el hijo de mufasa en la película El rey león?','a)Nala\tb)Simba\tc)Pumba','b'],
['Personaje animado cuya frase icónica es "Eso es todo amigos"','a)Mickey Mouse\tb)Porky\tc)Winnie the Pooh','b'],
['Película de Disney en la que hay un genio y una lámpara','a)Coco\tb)El rey león\tc)Aladdin','c']]
preg_geo = [
['¿Cuál es el país más grande del mundo?','a)Rusia\tb)México\tc)Canadá','a'],
['¿Cuántos continentes hay en el mundo?','a)4\tb)7\tc)5','c'],
['¿Qué animal está en el pico del águila en la bandera de México?','a)Alacrán\tb)Serpiente\tc)Es una flor','b'],
['¿En qué lugar del mundo se encuentra la esfinge?','a)Egipto\tb)Alemania\tc)Estados Unidos','a'],
['¿Cuál es la moneda oficial de Estados Unidos?','a)Euro\tb)Balboa\tc)Dólar','c']]
#Función para la introduccion del programa
def main():
    my_file=open('Introducción.txt','r')
    content=my_file.read()
    my_file.close()
    print(content)
    time.sleep(2)
    print('A continuación, tendrá la opción de elgir entre las siguientes categorías: \n Arte \n Historia \n Entretenimiento \n Geografía')
#Funcion para preguntas en la categoría de arte
def arte(a):    
    print('Ha seleccionado la categoría de Arte')
    np = random.randint(0,4)
    pregunta = (preg_arte[np])
    planteamiento=(preg_arte[np][0])
    print(planteamiento)
    respuestas = (preg_arte[np][1])
    print(respuestas)
    vidas=2
    #El programa detecta si la respuesta es correcta o incorrecta y el usuario pierde una vida si es incorrecta
    while True:
        respuesta_usuario = input('Introduce tu respuesta: ')
        if respuesta_usuario == 'a' or respuesta_usuario == 'b' or respuesta_usuario == 'c': 
            if respuesta_usuario == pregunta[2]:
                print(f'Correcto\n\n{pregunta[2]}\n')
                print("""
          --------------         
       -------------------       
    -------------------------    
  -----------------------------  
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
---------------------------------
---------------------------------
----- &&&&&&&&&&&&&&&&&&&&&&&----
------- &&& ----------- &&&------
  ------- &&& ------- &&&--------
    ------- &&&&&&&&&&&----------
       ----------------------       
        ------------------        
""")

                break
            else:
                if vidas > 0:
                    print(f'Incorrecto\n\n{pregunta[0]}\n{pregunta[1]}\n')
                    print("""
          --------------         
       -------------------       
    -------------------------    
  -----------------------------  
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
---------------------------------
---------------------------------
------------&&&&&&&&&&&----------
--------- &&& ------- &&& -------
  ----- &&& ----------- &&& -----
    -----------------------------
       ----------------------       
        ------------------  
""")
                    print('Te quedan ' + str(vidas) + ' vidas')
                    vidas = vidas-1 
                else:
                    print(f'Incorrecto\n\n')
                    print('Fin del juego')
                    exit()
        else:
            print('Respuesta inválida, ingrese una respuesta entre a, b ó c')
#Funcion para preguntas en la categoría de historia     
def historia(h):    
    print('Ha seleccionado la categoría de Historia')
    np = random.randint(0,4)
    pregunta = (preg_hist[np])
    planteamiento=(preg_hist[np][0])
    print(planteamiento)
    respuestas = (preg_hist[np][1])
    print(respuestas)
    vidas=2
    #El programa detecta si la respuesta es correcta o incorrecta y el usuario pierde una vida si es incorrecta
    while True:
        respuesta_usuario = input('Introduce tu respuesta: ')
        if respuesta_usuario == 'a' or respuesta_usuario == 'b' or respuesta_usuario == 'c': 
            if respuesta_usuario == pregunta[2]:
                print(f'Correcto\n\n{pregunta[2]}\n')
                print("""
          --------------         
       -------------------       
    -------------------------    
  -----------------------------  
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
---------------------------------
---------------------------------
----- &&&&&&&&&&&&&&&&&&&&&&&----
------- &&& ----------- &&&------
  ------- &&& ------- &&&--------
    ------- &&&&&&&&&&&----------
       ----------------------       
        ------------------        
""")

                break
            else:
                if vidas > 0:
                    print(f'Incorrecto\n\n{pregunta[0]}\n{pregunta[1]}\n')
                    print("""
          --------------         
       -------------------       
    -------------------------    
  -----------------------------  
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
---------------------------------
---------------------------------
------------&&&&&&&&&&&----------
--------- &&& ------- &&& -------
  ----- &&& ----------- &&& -----
    -----------------------------
       ----------------------       
        ------------------  
""")
                    print('Te quedan ' + str(vidas) + ' vidas')
                    vidas = vidas-1 
                else:
                    print(f'Incorrecto\n\n')
                    print('Fin del juego')
                    exit()
        else:
            print('Respuesta inválida, ingrese una respuesta entre a, b ó c')
#Funcion para preguntas en la categoría de entretenimiento
def entretenimiento(e):    
    print('Ha seleccionado la categoría de Entretenimiento')
    np = random.randint(0,4)
    pregunta = (preg_ent[np])
    planteamiento=(preg_ent[np][0])
    print(planteamiento)
    respuestas = (preg_ent[np][1])
    print(respuestas)
    vidas=2
    #El programa detecta si la respuesta es correcta o incorrecta y el usuario pierde una vida si es incorrecta
    while True:
        respuesta_usuario = input('Introduce tu respuesta: ')
        if respuesta_usuario == 'a' or respuesta_usuario == 'b' or respuesta_usuario == 'c': 
            if respuesta_usuario == pregunta[2]:
                print(f'Correcto\n\n{pregunta[2]}\n')
                print("""
          --------------         
       -------------------       
    -------------------------    
  -----------------------------  
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
---------------------------------
---------------------------------
----- &&&&&&&&&&&&&&&&&&&&&&&----
------- &&& ----------- &&&------
  ------- &&& ------- &&&--------
    ------- &&&&&&&&&&&----------
       ----------------------       
        ------------------        
""")
                break
            else:
                if vidas > 0:
                    print(f'Incorrecto\n\n{pregunta[0]}\n{pregunta[1]}\n')
                    print("""
          --------------         
       -------------------       
    -------------------------    
  -----------------------------  
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
---------------------------------
---------------------------------
------------&&&&&&&&&&&----------
--------- &&& ------- &&& -------
  ----- &&& ----------- &&& -----
    -----------------------------
       ----------------------       
        ------------------  
""")
                    print('Te quedan ' + str(vidas) + ' vidas')
                    vidas = vidas-1
                else:
                    print(f'Incorrecto\n\n')
                    print('Fin del juego')
                    exit()
        else:
            print('Respuesta inválida, ingrese una respuesta entre a, b ó c')
#Funcion para preguntas en la categoría de geografía
def geografia(g):    
    print('Ha seleccionado la categoría de Geografía')
    np = random.randint(0,4)
    pregunta = (preg_geo[np])
    planteamiento=(preg_geo[np][0])
    print(planteamiento)
    respuestas = (preg_geo[np][1])
    print(respuestas)
    vidas=2
    #El programa detecta si la respuesta es correcta o incorrecta y el usuario pierde una vida si es incorrecta
    while True:
        respuesta_usuario = input('Introduce tu respuesta: ')
        if respuesta_usuario == 'a' or respuesta_usuario == 'b' or respuesta_usuario == 'c': 
            if respuesta_usuario == pregunta[2]:
                print(f'Correcto\n\n{pregunta[2]}\n')
                print("""
          --------------         
       -------------------       
    -------------------------    
  -----------------------------  
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
---------------------------------
---------------------------------
----- &&&&&&&&&&&&&&&&&&&&&&&----
------- &&& ----------- &&&------
  ------- &&& ------- &&&--------
    ------- &&&&&&&&&&&----------
       ----------------------       
        ------------------        
""")

                break
            else:
                if vidas > 0:
                    print(f'Incorrecto\n\n{pregunta[0]}\n{pregunta[1]}\n')
                    print("""
          --------------         
       -------------------       
    -------------------------    
  -----------------------------  
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
------- &&&& ------- &&&& -------
---------------------------------
---------------------------------
------------&&&&&&&&&&&----------
--------- &&& ------- &&& -------
  ----- &&& ----------- &&& -----
    -----------------------------
       ----------------------       
        ------------------  
""")
                    print('Te quedan ' + str(vidas) + ' vidas')
                    vidas = vidas-1 
                else:
                    print(f'Incorrecto\n\n')
                    print('Fin del juego')
                    exit()
        else:
            print('Respuesta inválida, ingrese una respuesta entre a, b ó c')
#Se manda a traer la funcion de introduccion del programa  
main()
#Se le pide al usuario que elija una categoría
cat_seleccionada=input('Si quiere la categoría de Arte, presione a \n Si quiere la categoría de Historia, presione h \n Si quiere la categoría de Entretenimiento, presione e \n Si quiere la categoría de Geografía, presione g \n')
#El programa corre mandando a traer cada funcion de cada categoria cuando el usuario elija una categoría
while True:
    if cat_seleccionada == 'a':
        for i in range(0,5):
            arte(cat_seleccionada)
        else:
            print('Has contestado toda las preguntas')
            break
        
    elif cat_seleccionada == 'h':
        for i in range(0,5):
            historia(cat_seleccionada)
        else:
            print('Has contestado todas las preguntas')
            break
    
    elif cat_seleccionada == 'e':
        for i in range(0,5):
            entretenimiento(cat_seleccionada)
        else:
            print('Has contestado todas las preguntas')
            break
    
    elif cat_seleccionada == 'g':
        for i in range(0,5):
            geografia(cat_seleccionada)
        else:
            print('Has contestado todas las preguntas')
            break
    else:
        print('Opcion invalida, seleccione una categoria')
        cat_seleccionada=input('Si quiere la categoría de Arte, presione a \n Si quiere la categoría de Historia, presione h \n Si quiere la categoría de Entretenimiento, presione e \n Si quiere la categoría de Geografía, presione g')