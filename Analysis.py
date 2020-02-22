import numpy as np
import pandas as pd
import tweepy
import json 
from textblob import TextBlob
import matplotlib.pyplot as plt

#Funcion para retornar la cantidad en porcentajes 
def porcentaje(part, whole):
    return 100*float(part)/float(whole)

#Declaracion de variables para determinar los porcentajes 
positivo = 0
negativo = 0
neutral = 0
polaridad = 0

#Cadenas para realizar la auntentificacion
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
        
#instanciacion del objeto 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


#Instanciar opjeto de la clase api 
#Atributos para la delimitacion y que el programa no se detenga 
api=tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

##Ingreso de parametros a buscar (palabras/tweets)
busqueda = input("Ingrese la palabra a buscar: ")
cantidad = int(input("Ingrese la cantidad de Tweets a analizar: "))   
caracter1 = input("Ingrese una parabra clave: ")
caracter2 = input("Ingrese una parabra clave: ")
caracter3 = input("Ingrese una parabra clave: ")
###########################Buscar Tweets#######################################
filtro = busqueda + " -filter:retweets"

for tweet in tweepy.Cursor(api.search, screen_name = "RamoColombia",q = filtro, 
                           tweet_mode = "extended").items(cantidad):
    api.get_user("RamoColombia").statuses_count

for tweet in tweepy.Cursor(api.search, screen_name = "RamoColombia",
                           q = filtro).items(cantidad):
    #analisis de los tweets 
    analysis = TextBlob(tweet.text)
    polaridad += analysis.sentiment.polarity
    if(analysis.sentiment.polarity == 0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0.00):
        negativo += 1
    elif(analysis.sentiment.polarity > 0.00):
        positivo += 1
    

#Asignacion de porcentajes 
positivo = porcentaje(positivo, cantidad)
negativo = porcentaje(negativo, cantidad)
neutral = porcentaje(neutral, cantidad)

#Asignacion a dos decimales 
positivo = format(positivo, ".2f")
negativo = format(negativo, ".2f")
neutral = format(neutral, ".2f")

#Impresion de la torta de porcentajes 
labels = ["Positivo["+str(positivo)+"%]", "Neutral["+str(neutral)+"%]", "Negativo["+str(negativo)+"%]"]
sizes = [positivo, neutral, negativo]
colors = ["green","gold","red"]
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc = "best")
plt.title("Analisis")
plt.axis("equal")
plt.tight_layout()
plt.show()

###############################################################################
##VA DENTRO DE UNA FUNCION 
filtro2 = busqueda +" " +caracter1
lista=[]
suma=0
for tweet in tweepy.Cursor(api.search, screen_name = "RamoColombia", q = filtro2, 
                          tweet_mode = "extended").items(cantidad):
    suma += 1
lista.append(suma)
    #ista.add.reduce(suma)

filtro2 = busqueda +" " +caracter2
suma=0
for tweet in tweepy.Cursor(api.search, screen_name = "RamoColombia", q = filtro2, 
                           tweet_mode = "extended").items(cantidad):
    suma += 1
lista.append(suma)

    
filtro2 = busqueda + " " + caracter3
suma=0
for tweet in tweepy.Cursor(api.search, screen_name = "RamoColombia", q = filtro2, 
                           tweet_mode = "extended").items(cantidad):
    suma += 1
lista.append(suma)
    
ypos = np.arange(cantidad)
palabraAdicional = [1, 2, 3]
palabra = [caracter1, caracter2, caracter3]
prueba = lista
    
plt.bar(palabraAdicional, prueba)
plt.xticks(palabraAdicional, palabra)
plt.show()
