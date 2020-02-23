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
#api.get_user("RamoColombia")
###########################Buscar Tweets#######################################
filtro = busqueda + " -filter:retweets"


#caracter(caracter1, caracter2, caracter3, busqueda, cantidad)

for tweet in tweepy.Cursor(api.search, screen_name = "RamoColombia",q = filtro, 
                           tweet_mode = "extended").items(cantidad):
    #print(json.dumps(tweet._json, indent=2))
    api.get_user("RamoColombia").statuses_count
    #print(tweet._json["full_text"])
    #print()
#print("\n"*10)
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

###################Diagrama de barras#########################################

users_locs = [[tweet.user.location] for tweet in tweepy.Cursor(api.search, screen_name = "RamoColombia", q = "chocoramo", 
                           tweet_mode = "extended").items(100)]
#users_locs

#Analisis a Bogota
count = 0
listaC = []
count += users_locs.count(['Bogotá'])
count += users_locs.count(['Bogotá, D.C., Colombia'])
count += users_locs.count(['Bogotá '])
count += users_locs.count(['Bogotá, D.C.'])
count += users_locs.count(['Bta'])
count += users_locs.count(['Bogotá, Colombia'])
count += users_locs.count(['Bogotá - Colombia'])
count += users_locs.count(['bogota COLOMBIA'])
count += users_locs.count(['Madrid / Bogotá D.C., Colombia'])
listaC.append(count+1)

#Analisis Medellin
count = 0
count += users_locs.count(['Medellín, Colombia'])
count += users_locs.count(['Medellín'])
count += users_locs.count(['Colombia, Medellin'])
count += users_locs.count(['Manizales - CO'])
listaC.append(count+1)


#Analisis Barranquilla
count = 0
count += users_locs.count(['Barranquilla, Colombia'])
count += users_locs.count(['Barranquilla'])
count += users_locs.count(['Colombia, Barranquilla'])
count += users_locs.count(['Barranquilla - Colombia'])
count += users_locs.count(['barranquilla - CO'])
count += users_locs.count(['barranquilla'])
count += users_locs.count(['Barranquilla '])
listaC.append(count+1)

#Analisis cali
count = 0
count += users_locs.count(['Cali, Colombia'])
count += users_locs.count(['Cali'])
count += users_locs.count(['Colombia, Cali'])
count += users_locs.count(['cali - CO'])
count += users_locs.count(['Cali - Colombia'])
count += users_locs.count(['cali'])
count += users_locs.count(['Cali '])
listaC.append(count+1)

#Analisis Cartagena
count = 0
count += users_locs.count(['Cartagena, Colombia'])
count += users_locs.count(['Cartagena'])
count += users_locs.count(['Colombia, Cartagena'])
count += users_locs.count(['cartagena - CO'])
count += users_locs.count(['Cartagena - Colombia'])
count += users_locs.count(['cartagena'])
count += users_locs.count(['Cartagena '])
listaC.append(count+1)

##Analisis Cucuta
count = 0
count += users_locs.count(['Cucuta, Colombia'])
count += users_locs.count(['Cucuta'])
count += users_locs.count(['Colombia, Cucuta'])
count += users_locs.count(['cucuta - CO'])
count += users_locs.count(['Cucuta - Colombia'])
count += users_locs.count(['cucuta'])
count += users_locs.count(['Cucuta '])
listaC.append(count+1)


valor = 100-sum(listaC)
listaC.append(valor)

ypos = np.arange(len(listaC))
palabraAdicional = [0, 1, 2, 3, 4, 5, 6]
palabra = ["Bogota", "Medellin", "Barranquilla", "Cali", "Cartagena", "Cucuta", "Otro"]
prueba = listaC
#Impresion 
plt.bar(ypos, prueba)
plt.xticks(ypos, palabra)
plt.show()

#Filtro para fechas
for tweet in tweepy.Cursor(api.user_timeline, screen_name="RamoColombia", tweet_mode = "extended",
                           since="2020-02-20", until="2020-02-22").items(10):
    print(tweet._json["full_text"])
    print()
    
