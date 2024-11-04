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
    'it': ['Buon giorno', 'buon pomeriggio', 'buona serata'],  
    'fr': ['Bonjour', 'bonne après-midi', 'Bonsoir'],  
    'jp': ['おはようございます', 'こんにちは', 'こんばんは'],  
}  
# Agregar Portugués y Catalán a la lista de idiomas  
LENGUAJES.extend([('pt', 'Portuguese'), ('cat', 'Catalan')])  
# Agregar saludos en ambos idiomas  
SALUDOS.update({'pt': ['Bom Dia', 'Boa Tarde', 'Boa Noite'], 'cat': ['Bon Dia', 'Bona Tarda', 'Bona Nit']})  

def encuentra_idioma(opcion):  
    for item in LENGUAJES:  
        if opcion in item:  
            print(f"\n\nLos saludos en '{item[1]}':")  
            return item[0]  # Retorna solo el código del idioma  
    if opcion == 'salir':  
        print('Saliendo del programa...')  
        return 'salir'  
    else:  
        print('Has seleccionado una opción incorrecta. Vuelve a intentarlo.')  
        return False  

# Definir función para ver lista de idiomas  
def mostrar_idiomas():  
    for item in LENGUAJES:  
        print('*', item[0], item[1])  

# Definir función para ver saludos  
def mostrar_saludos(opciones):  
    for opcion in opciones:  
        if opcion in SALUDOS:  
            lista_saludos = SALUDOS[opcion]  
            print(f"\nSaludos en '{opcion}':")  
            for saludo in lista_saludos:  
                print('-', saludo)  

# Función para quitar un idioma  
def quitar_idioma():  
    mostrar_idiomas()  
    idioma_a_quitar = input('Escribe las iniciales del idioma que deseas quitar: ')  
    for i, item in enumerate(LENGUAJES):  
        if item[0] == idioma_a_quitar:  
            LENGUAJES.pop(i)  # Quita el idioma de la lista  
            del SALUDOS[idioma_a_quitar]  # Quita los saludos   
            print(f'Idioma "{item[1]}" ha sido eliminado.')  
            return  
    print('Idioma no encontrado.')  

# Definir función para consultar saludos en otro idioma  
def consulta_nuevamente():  
    while True:  
        repetir = input('¿Te gustaría consultar 3 saludos en algún otro idioma? si/no: ')  
        if repetir.lower() == 'si':  
            os.system('clear')  
            mostrar_idiomas()  
            respuesta = input('Escribe las iniciales de uno de estos idiomas para ver los saludos: ')  
            idioma_encontrado = encuentra_idioma(respuesta)  
            if idioma_encontrado:  
                mostrar_saludos([idioma_encontrado])  
            time.sleep(2)  
            os.system('clear')  
        elif repetir.lower() == 'no':  
            print('\nEntendido. Saliste del programa. Hasta luego.')  
            sys.exit()  
        else:  
            print('\nSolo puedes ingresar las opciones: si/no. Intenta de nuevo.')  

while True:  
    print('Esta es tu aplicación de saludos en múltiples idiomas')  

    mostrar_idiomas()  

    print('Seleccione una opción:')  
    print('1. Ver saludos en un idioma')  
    print('2. Ver saludos en dos idiomas al mismo tiempo')  
    print('3. Quitar un idioma')  
    print('Escribe "salir" si deseas cerrar la aplicación.')  

    respuesta = input('> ')  
    
    if respuesta == 'salir':  
        print('\nHasta luego.')  
        break  
    elif respuesta == '1':  
        idioma = input('Escribe las iniciales de uno de estos idiomas para ver los saludos: ')  
        estado = encuentra_idioma(idioma)  
        if estado:  
            mostrar_saludos([estado])  
            time.sleep(3)  
            os.system('clear')  
    elif respuesta == '2':  
        print('Selecciona dos idiomas (separados por una coma):')  
        mostrar_idiomas()  
        idiomas = input('Ejemplo: en, es\n> ').split(',')  
        idiomas = [idioma.strip() for idioma in idiomas]  # Limpiar espacios en blanco  
        mostrar_saludos(idiomas)  
        time.sleep(3)  
        os.system('clear')  
    elif respuesta == '3':  
        quitar_idioma()  
    else:  
        print('Has seleccionado una opción incorrecta. Vuelve a intentarlo.')