import xmlrpc.client
import os

print('\nCLIENTE - CARTELERA CINE\n')

IP = input('Escriba el IP del servidor: ')

PUERTO = int(input('Escriba el puerto: '))

servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(IP,PUERTO))

diasemana = 'lunes'

while (diasemana != 'salir'):
    
    diasemana= input('\nEscriba "salir" para finalizar o ingrese día de la semana para consultar: ')
    os.system('cls')
    carteleraFunciones = servidor.cartel(diasemana.lower())

    if carteleraFunciones == '1':
        print('\nPalabra erronea, por favor intente con un día de la semana: ')
    elif carteleraFunciones == '0':
        print('\nGracias por usar nuestro servicio!')
    else:
        print('\nPelículas disponibles:  '+diasemana.upper())
        print('-'*64)
        print(carteleraFunciones)

