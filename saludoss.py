import os
import time
import sys
LENGUAJES = [
    ('el', 'Greek'),
    ('en', 'English'),
    ('eo', 'Esperanto'),
    ('es', 'Spanish'),
    ('it', 'Italian'),
    ('fr', 'French'),
    ('jp', 'Japanese'),
]

SALUDOS = {
    'el': ['Καλημέρα', 'καλό απόγευμα', 'Καλό απόγευμα'],
    'en': ['Good Morning', 'Good Afternoon', 'Good Evening'],
    'eo': ['bonan matenon', 'bonan posttagmezon', 'bonan vesperon'],
    'es': ['Buenos días', 'Buenas tardes', 'Buenas noches'],
    'it': ['Buon giorno', 'buon pomeriggio','buona serata'],
    'fr': ['Bonjour', 'bonne après-midi', 'Bonsoir'],
    'jp': ['おはようございます','こんにちは','こんばんは'],
}
#Agregar Portugues y Catalan a la lista de idiomas
LENGUAJES.extend([('pt', 'Portugues'),('cat', 'Catalan')])
#Agregar saludos en ambos idiomas
SALUDOS.update({'pt': ['Bom Dia', 'Boa Tarde', 'Boa Noite'], 'cat': ['Bon Dia', 'Bona Tarda', 'Bona Nit']})

def encuentra_idioma(opcion):
    try:
        for item in LENGUAJES:
            if opcion in item:
                print(f"\n\n Los saludos en '{item[1]}'")
                # return item[1]
                return True
        if opcion == 'salir':
            print('Saliendo del programa...')
            return 'salir'
        else:
            print('Has seleccionado una opción incorrecta. Vuelve a intentarlo.')
            return False
    except UnboundLocalError as error:
        print(error)
#Definir funcion para ver lista de idiomas
def mostrar_idiomas():
    for item in LENGUAJES:
        print('*', item[0], item[1])
#Definir funcion para ver saludos
def mostrar_saludo(opcion):
    for llave, valor in SALUDOS.items():
        if llave == opcion:
            lista_saludos = valor

    for saludo in lista_saludos:
        print('-', saludo)
#Definir funcion para consultar saludos en otro idioma
def consulta_nuevamente():
    while True:
        repetir = input('¿Te gustaría consultar 3 saludos en algún otro idioma? si/no: ')
        if repetir == 'si':
            os.system('clear')
            mostrar_idiomas()
            respuesta = input('Escribe las iniciales de uno de estos idiomas para ver los saludos: ')
            encuentra_idioma(respuesta)
            mostrar_saludo(respuesta)
            time.sleep(2)
            os.system('clear')
        elif repetir == 'no':
            print('\nEntendido. Saliste del programa. Hasta luego.')
            sys.exit()
        else:
            print('\nSolo puedes ingresar las opciones: si/no. Intenta de nuevo.')
while True:
    print('Esta es tu aplicación de saludos en múltiples idiomas')

    mostrar_idiomas()

    print('Escribe las iniciales de uno de estos idiomas para ver los saludos. \nEscribe "salir" si deseas cerrar la aplicación.')
    respuesta = input('> ')
    
    estado = encuentra_idioma(respuesta)
    
    #Valida un verdadero
    if estado:
        mostrar_saludo(respuesta)
        time.sleep(3)
        os.system('clear')

    elif estado == 'salir':
        print('\nHasta luego.')
        break
    consulta_nuevamente()