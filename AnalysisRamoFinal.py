"""
Parcila II Ciencia de datos 
Yeimer Serrano Navarro 20181020060
José Luis Quintero 20181020061
23/02/2020
"""
import numpy as np
import pandas as pd
import tweepy
import json 
from textblob import TextBlob
import matplotlib.pyplot as plt
import time
from datetime import datetime 
"""
consumer_key = "hctDhZRYK35Ofjd1aBZ54erVK"
consumer_secret = "fu7lwB3FxCdZRzOCVFX4DgT1IcVBjU7KDiScY9DBjIqc3wGuRO"
access_token = "1228054589422931970-SE3EbqQd4O72qYiphTDLzuzSuFCHex"
access_token_secret = "fQAxtonQ1RBnxWYvlz1MrHxRoJDABA5oCblBPeN8rAcE6"
""" 

consumer_key = "bhIm9xUbUZCfZKAolMzZTxGhY"
consumer_secret = "N18wGlNmoNDNCFiTDWgJLgW6U6RQ48663NWWfrZCQw0CXX5G0K"
access_token = "1228080357624426497-lUdYfObZZDEaUwHIwlcr2ftnkCQnva"
access_token_secret = "JlYBrbQPKx8XQSQeTKHl89qSXiwFJsLc5NidZHbpqGfZw"
        
#instanciacion del objeto 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Instanciar objeto de la clase api 
#Atributos para la delimitacion y que el programa no se detenga 
api=tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

#Funcion para retornar el promedio en el pie
def porcentaje(part, whole):
    return 100*float(part)/float(whole)

#Funcion encargada de realizar el analisis de sentimientos a los tweets
def sentimientos(busqueda, cantidad):
    #Variables a usar 
    busqueda = busqueda + " -filter:retweets"
    positivo = 0
    negativo = 0
    neutral = 0
    polaridad = 0
    polarity_list = []
    numbers_list = []
    number = 1
    
    #analisis de los tweets 
    for tweet in tweepy.Cursor(api.search, screen_name = "RamoColombia", 
                                q = busqueda).items(cantidad):
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
    labels = ["Positivo["+str(positivo)+"%]", "Neutral["+str(neutral)+"%]",
                 "Negativo["+str(negativo)+"%]"]
    sizes = [positivo, neutral, negativo]
    colors = ["#0CB1EF","#F0EA35","#ED1C2E"]
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc = "best")
    plt.title("Analisis a los sentimientos")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig('static/feelings1.png')
    plt.cla()
    plt.clf()
    
    #Analisis a sentimientos de tweets 
    for tweet in tweepy.Cursor(api.search, screen_name="RamoColombia", 
                                q = busqueda).items(cantidad):
        try:
            analysis = TextBlob(tweet.text)
            analysis = analysis.sentiment
            polarity = analysis.polarity
            polarity_list.append(polarity)
            numbers_list.append(number)
            number = number + 1
        except tweepy.TweepError as e:
            print(e.reason)
            number = number + 1
        except StopIteration:
            break
        
    #Creacion del plano cartesiano 
    axes = plt.gca()
    axes.set_ylim([-1, 2])
    plt.scatter(numbers_list, polarity_list, color="#ED1C2E")
    #Calcular el promedio de polaridad, (No es promedio ponderado)
    averagePolarity = (sum(polarity_list))/(len(polarity_list))
    averagePolarity = "{0:.0f}%".format(averagePolarity * 100)

    time  = datetime.now().strftime("Hora: %H:%M\nDia: %m-%d-%y")
    #Calculo de promedio ponderado
    weighted_avgPolarity=np.average(polarity_list, weights=numbers_list)
    weighted_avgPolarity = "{0:.0f}%".format(weighted_avgPolarity* 100)  

    #Texto con promedio de sentimiento
    plt.text(5, 0.9, "Promedio Sentimiento:  " + str(averagePolarity) + "\n" + "Promedio ponderado:  " + str(weighted_avgPolarity) + "\n" + time,
             fontsize=12, bbox = dict(facecolor='none', edgecolor='black', boxstyle='square, pad = 1'))
    plt.title("Sentimiento de " + busqueda + " en Twitter")
    plt.xlabel("Número de Tweets")
    plt.ylabel("Sentimiento")
    plt.savefig('static/feelings2.png')
    plt.cla()
    plt.clf()

def ciudades(palabra, cantidad):
    #Variables
    palabra = palabra + " -filter:retweets"
    count = 0
    listaC = []
    #Lista de ubicaciones de los tweets
    users_locs = [[tweet.user.location] for tweet in tweepy.Cursor(api.search, screen_name = "RamoColombia",
                         q = palabra, tweet_mode = "extended").items(cantidad)]
   
    #Analisis a Bogota
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
    
    #Asignacion a 
    valor = cantidad-sum(listaC)
    listaC.append(valor)
    
    ypos = np.arange(len(listaC))
    palabra = ["Bogota", "Medellin", "Barranquilla", "Cali", "Cartagena", "Cucuta", "Otro"]
    prueba = listaC
    #Impresion 
    plt.bar(ypos, prueba, color="#0CB1EF")
    plt.title("Tweets de ciudades")
    plt.xticks(ypos, palabra)
    plt.savefig('static/city.png')
    plt.cla()
    plt.clf()
    
#Funcion para retornar tweets en una fecha especifica
def tweets(palabra, fecha1,fecha2, cantidad):
    topTweet = []
    palabra = palabra 
    cantidad = 20
    for tweet in tweepy.Cursor(api.search, q= palabra + " -filter:retweets", since = fecha1, until = fecha2, tweet_mode = "extended").items(cantidad):
        topTweet.append(tweet._json["full_text"])
    return topTweet
    
