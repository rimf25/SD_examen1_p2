from xmlrpc.server import SimpleXMLRPCServer

print ('\tSERVIDOR CARTELERA CINE ACTIVO')

IP = '127.0.1.0'
PUERTO = 9099

def cartel (dias):
    if dias == 'lunes':
        return 'Los lunes todas las entradas cuentan con un 50% de descuento:\n\nThor: Amor y Trueno (Sub): 12:00pm - 3:00 pm - 6:00 pm - 8:00 m | Entrada: 17 Bss.\nThor: Amor y Trueno (Esp): 11:00 am - 2:00 pm - 5:00 pm - 7:00 m | Entrada: 17 Bss.\nAline: La voz del Amor (Sub): 5:00 pm - 7:00 pm - 10:00 pm | Entrada: 17 Bss.\nELVIS (Sub): 5:00 pm - 7:30 pm - 9:30 pm | Entrada: 17 Bss.\nMINIONS: NACE UN VILLANO(Sub): 10:00 am - 12:00 pm - 2:30 pm- 4:30 pm- 6:00 pm | Entrada: 17 Bss.'
    elif dias == 'martes':
        return 'Los martes las cotufas vienen gratis con la entrada:\n\nThor: Amor y Trueno (Sub): 12:00pm - 3:00 pm - 6:00 pm - 8:00 m | Entrada: 17 Bss.\nThor: Amor y Trueno (Esp): 11:00 am - 2:00 pm - 5:00 pm - 7:00 m | Entrada: 17 Bss.\nAline: La voz del Amor (Sub): 5:00 pm - 7:00 pm - 10:00 pm | Entrada: 17 Bss.\nELVIS (Sub): 5:00 pm - 7:30 pm - 9:30 pm | Entrada: 17 Bss.\nMINIONS: NACE UN VILLANO(Sub): 10:00 am - 12:00 pm - 2:30 pm- 4:30 pm- 6:00 pm | Entrada: 17 Bss.'
    elif dias == 'miercoles':
        return 'Los miercoles las personas de tercera edad y niños tienen un 60% de descuento:\n\nThor: Amor y Trueno (Sub): 12:00pm - 3:00 pm - 6:00 pm - 8:00 m | Entrada: 17 Bss.\nThor: Amor y Trueno (Esp): 11:00 am - 2:00 pm - 5:00 pm - 7:00 m | Entrada: 17 Bss.\nAline: La voz del Amor (Sub): 5:00 pm - 7:00 pm - 10:00 pm | Entrada: 17 Bss.\nELVIS (Sub): 5:00 pm - 7:30 pm - 9:30 pm | Entrada: 17 Bss.\nMINIONS: NACE UN VILLANO(Sub): 10:00 am - 12:00 pm - 2:30 pm- 4:30 pm- 6:00 pm | Entrada: 17 Bss.'
    elif dias == 'jueves':
        return 'Thor: Amor y Trueno (Sub): 12:00pm - 3:00 pm - 6:00 pm - 8:00 m | Entrada: 17 Bss.\nThor: Amor y Trueno (Esp): 11:00 am - 2:00 pm - 5:00 pm - 7:00 m | Entrada: 17 Bss.\nAline: La voz del Amor (Sub): 5:00 pm - 7:00 pm - 10:00 pm | Entrada: 17 Bss.\nELVIS (Sub): 5:00 pm - 7:30 pm - 9:30 pm | Entrada: 17 Bss.\nMINIONS: NACE UN VILLANO(Sub): 10:00 am - 12:00 pm - 2:30 pm- 4:30 pm- 6:00 pm | Entrada: 17 Bss.'
    elif dias == 'viernes':
        return 'Thor: Amor y Trueno (Sub): 12:00pm - 3:00 pm - 6:00 pm - 8:00 m | Entrada: 17 Bss.nThor: Amor y Trueno (Esp): 11:00 am - 2:00 pm - 5:00 pm - 7:00 m | Entrada: 17 Bss.\nAline: La voz del Amor (Sub): 5:00 pm - 7:00 pm - 10:00 pm | Entrada: 17 Bss.\nELVIS (Sub): 5:00 pm - 7:30 pm - 9:30 pm | Entrada: 17 Bss.\nMINIONS: NACE UN VILLANO(Sub): 10:00 am - 12:00 pm - 2:30 pm- 4:30 pm- 6:00 pm | Entrada: 17 Bss.'
    elif dias == 'sabado':
        return 'Thor: Amor y Trueno (Sub): 12:00pm - 3:00 pm - 6:00 pm - 8:00 m | Entrada: 17 Bss.\nThor: Amor y Trueno (Esp): 11:00 am - 2:00 pm - 5:00 pm - 7:00 m | Entrada: 17 Bss.\nAline: La voz del Amor (Sub): 5:00 pm - 7:00 pm - 10:00 pm | Entrada: 17 Bss.\nELVIS (Sub): 5:00 pm - 7:30 pm - 9:30 pm | Entrada: 17 Bss.\nMINIONS: NACE UN VILLANO(Sub): 10:00 am - 12:00 pm - 2:30 pm- 4:30 pm- 6:00 pm | Entrada: 17 Bss.'
    elif dias == 'domingo':
        return 'Thor: Amor y Trueno (Sub): 12:00pm - 3:00 pm - 6:00 pm - 8:00 m | Entrada: 17 Bss.\nThor: Amor y Trueno (Esp): 11:00 am - 2:00 pm - 5:00 pm - 7:00 m | Entrada: 17 Bss.\nAline: La voz del Amor (Sub): 5:00 pm - 7:00 pm - 10:00 pm | Entrada: 17 Bss.\nELVIS (Sub): 5:00 pm - 7:30 pm - 9:30 pm | Entrada: 17 Bss.\nMINIONS: NACE UN VILLANO(Sub): 10:00 am - 12:00 pm - 2:30 pm- 4:30 pm- 6:00 pm | Entrada: 17 Bss.'
    elif dias == 'salir':
        return '0'
    else:
        return '1'

print('\nRespuesta cliente:')

servidor = SimpleXMLRPCServer ((IP, PUERTO))

servidor.register_function(cartel, "cartel")

servidor.serve_forever()



