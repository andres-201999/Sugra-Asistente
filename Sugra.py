import wolframalpha as wf
from urllib.request import urlopen
import requests
import json
import random
import pyttsx3
import datetime
# Importamos el reconocimienti de la voz
import speech_recognition as sr
# Importamos la libreria wikipedia
import wikipedia as wiki
# Importación para el correo del protocolo
import smtplib
# import web browser
import webbrowser as wb
# Sensores de cpu y bateria
import psutil
# biblioteca de chistes
import chistesESP as chiste
# Importaion sistema operativo
import os
# Para realizar screeshots
import pyautogui
# Inicializamos la importacion pyttsx3
engine = pyttsx3.init()

import wolframalpha
wolframalpha_app_id='XHYE6K-AGJEUQ6X7G'
# Definimos la función para que pueda hablar

import time 

def speak(audio):
    # Llamamos al mensaje
    engine.say(audio)
    # Corremos la funcion
    engine.runAndWait()


#speak('Hola mi perro')
# Importamos la fecha
def time_():
    # Para un reloj de 24 horas importamos la hora
    # Si deseas fortmato 12 horas cambiamos la H por una I
    Time = datetime.datetime.now().strftime("%H: %M: %S:")
    speak("Actualmente son las:")
    speak(Time)

# Ejecutamos la función para indicar la fecha


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak('La fecha de hoy es:')
    speak(day)
    speak('del')
    speak(month)
    speak('del año')
    speak(year)

# Ejecutamos las dos funciones anteriores
# Realiza las peticiones sin reconocimiento de voz


def wishme():
    '''speak('Hola de nuevo Andy')
    date_()'''

    hour = datetime.datetime.now().hour
    # Asignamos los saludos
    if hour >= 5 and hour <= 12:
        speak('Buenos días Andy')
    if hour >= 12 and hour <= 18:
        speak('Buenas tardes Andy')
    if hour >= 18 and hour < 24:
        speak('Buenas noches Andy')
    else:
        speak('Espero que te acuestes pronto, está tarde')

    time_()

    speak('Sugra está a tu servicio,dime en que puedo ayudarte')

# Definimos el nombre del asistente


def name():
    name = 'sugra'
    speak('Mi nombre es:')
    speak(name)

# wishme()


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Por favor indiqueme que desea...')
        # Esperamos hasta que reconozca la voz
        r.pause_threshold = 1
        Gaudio = r.listen(source)

    try:
        print('Reconociendo la tarea')
        query = r.recognize_google(Gaudio, language='es-es')
        # speak(query)
        print(query)

    except Exception as e:
        print(e)
        speak('No le entendí, puede repetir por favor...')
        return "None"
    return query
# TakeCommand()


def sendMail_(to, content):
    # host
    server = smtplib.SMTP('smtp@gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Para esta función activaremos baja serguridad en el gmail

    server.login('andres201999@gmail.com', 'Andres.2017')
    server.sendmail('pruebasethical97@gmail.com', to, content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak('El uso de la CPU está en:' + usage)
    speak('porciento')


# ARREGLAR
def battery():
    battery = psutil.sensors_battery()
    speak('La batería está en:')
    speak(battery)
    speak('porciento')


def joke():
    speak(chiste.get_random_chiste())


def screenshot():
    strTime = datetime.datetime.now().strftime("%H_%M")
    date1 = str(datetime.datetime.now().month)
    speak('wiskhey')
    img = pyautogui.screenshot()
    img.save('C:/Users/andre/Desktop/Universidad/Cursos/Jarvis/screenshot_' +
    strTime+'_M'+date1+'.png')
    speak('pantallazo guardado jefecito')


if __name__ == "__main__":
    wishme()

    while True:
        # Dejamos las indicaciones en minúscula
        query = TakeCommand().lower()

        # Todos los comandos que tendremos en el query
        # para un reconocimiento sencillo

        if 'hora' in query:
            time_()
        elif 'fecha' in query:
            date_()
        elif 'nombre' in query:
            name()
        elif 'wikipedia' in query:
            wiki.set_lang("es")
            try:
                speak('Estoy buscando, un momento')
                query = query.replace('wikipedia', '')
                result = wiki.summary(query, sentences=2)
                speak('El resultado según wikipedia es...')
                print(result)
                speak(result)
            except Exception as e:
                print(e)
                speak('Hay más de un resultado, ¿Podría ser más especifico?')
        elif 'enviar correo' in query:
            try:
                speak('Que quieres que contenga el correo')
                content = TakeCommand()
                #
                speak('Quien será el destinatario?')

                reciever = input("Ingrese los corresos:")

                to = reciever
                sendMail_(to, content)
                speak(content)
                speak('El mensaje fue enviado')

            except Exception as e:
                print(e)
                speak('No se pudo mandar el mensaje')

        elif 'buscar en navegador' in query:
            speak('Que es lo que desea buscar?')
            operapath = 'C:/Users/andre/AppData/Local/Programs/Opera GX/launcher.exe %s'
            search = TakeCommand().lower()
            wb.get(operapath).open_new_tab(
                'https://www.google.com/search?q='+search)

        elif 'buscar en youtube' in query:
            speak('Que es lo que desea buscar?')
            operapath = 'C:/Users/andre/AppData/Local/Programs/Opera GX/launcher.exe %s'
            search = TakeCommand().lower()
            wb.get(operapath).open_new_tab(
                'https://www.youtube.com/search?q='+search)

        elif 'buscar en spotify' in query:
            speak('Que es lo que desea buscar?')
            operapath = 'C:/Users/andre/AppData/Local/Programs/Opera GX/launcher.exe %s'
            search = TakeCommand().lower()
            wb.get(operapath).open_new_tab(
                'https://open.spotify.com/search/'+search)

        elif 'cpu' in query:
            cpu()
        elif 'batería' in query:
            battery()

        elif 'chiste' in query:
            joke()
        elif 'apagar' in query:
            speak('Ya te cansaste de mí?, no me apagues por favor')
            quit()

        elif 'microsoft word' in query:
            speak('Abriendo word')
            msword = r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
            os.startfile(msword)

        elif 'abrir spotify' in query:
            speak('Abriendo spotify')
            spotify = r'spotify'
            os.startfile(spotify)

        elif 'escribir una nota' in query:
            strTime = datetime.datetime.now().strftime("%H_%M")
            date1 = str(datetime.datetime.now().month)
            speak('¿Que deseas escribir?')
            notes = TakeCommand()
            file = open('notes_'+strTime+'_M'+date1+'.txt', 'w')
            speak('Jefe,La nota fue guardada correctamente')

        elif 'tomar pantallazo' in query:
            screenshot()

        elif 'recuerda esto' in query:
            strTime = datetime.datetime.now().strftime("%H_%M")
            date1 = str(datetime.datetime.now().month)
            speak('Jefe, que quieres que recuerde?')
            memory = TakeCommand()
            speak('Quieres que recuerde esto'+memory)
            remember = open('asset/memos'+strTime+'_M'+date1+'.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'noticias' in query:
            try:
                jsonObj = urlopen(
                    "https://webhose.io/filterWebContent?token=21eef9ed-bb45-4ecb-8976-d9a66534b04d&format=json&sort=crawled&q=language%3Aspanish")
                data= json.load(jsonObj)
                i=1
                
                speak('Estos son algunos de los titulares de las noticias')
                print('========TITULARES========')
                
                for item in data['posts']:
                    print(str(i)+'. '+item['title']+'\n')
                    
                    if item['title']!= None:
                        speak(item['title'])
                        i+= 1
                    if i== 10:
                        break
                    
            except Exception as e:
                print(e)
        
        elif 'dónde está' in query:
            query= query.replace('dónde está',"")
            location =query
            speak('Preguntaste por:'+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'ir a' in query:
            query= query.replace('ir a',"")        
            location =query
            speak('quieres ir a:'+location)
            wb.open_new_tab("https://www.google.com/maps/dir/home/"+location)
        elif 'calcular' in query:
            client= wolframalpha.Client(wolframalpha_app_id)
            index = query.lower().split().index('calcular')
            query= query.split()[index+ 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('La respuesta es:'+ answer)

        elif 'parar de escuchar' in query or 'silenciar' in query:
            speak('Durante cuando tiempo quiere silenciarme')
            ans= int(TakeCommand())
            time.sleep(ans)
            print(ans)
                