import random 

entidades = {'AG':'Aguascalientes',
             'BC':'Baja California',
             'BS':'Baja California Sur',
             'CC':'Campeche',
             'CL':'Coahuila',
             'CM':'Colima',
             'CS':'Chiapas',
             'CH':'Chihuahua',
             'DF':'Ciudad de México',
             'DG':'Durango',
             'GT':'Guanajuato',
             'GR':'Guerrero',
             'HG':'Hidalgo',
             'JC':'Jalisco',
             'MC':'México',
             'MN':'Michoacán',
             'MS':'Morelos',
             'NT':'Nayarit',
             'NL':'Nuevo León',
             'OC':'Oaxaca',
             'PL':'Puebla',
             'QT':'Querétaro',
             'QR':'Quintana Roo',
             'SP':'San Luis Potosí',
             'SL':'Sinaloa',
             'SR':'Sonora',
             'TC':'Tabasco',
             'TS':'Tamaulipas',
             'TL':'Tlaxcala',
             'VZ':'Veracruz',
             'YN':'Yucatán',
             'ZS':'Zacatecas'}

altisonantes = {
    "BUEI": "BUEX",
    "CACA": "CACX",
    "CACA": "CACO",
    "CAGA": "CAGX",
    "CAGO": "CAGX",
    "CAKA": "CAKX",
    "CAKA": "CAKO",
    "COGE": "COGX",
    "COJA": "COJX",
    "COJE": "COJX",
    "COJI": "COJX",
    "COJO": "COJX",
    "CULO": "CULX",
    "FETO": "FETX",
    "GUEY": "GUEX",
    "JOTO": "JOTX",
    "KACA": "KACX",
    "KACA": "KACO",
    "KAGA": "KAGX",
    "KAGO": "KAGX",
    "KOGE": "KOGX",
    "KOJO": "KOJX",
    "KAKA": "KAKX",
    "KULO": "KULX",
    "MAME": "MAMX",
    "MAME": "MAMO",
    "MEAR": "MEAX",
    "MEAR": "MEAS",
    "MEON": "MEOX",
    "MION": "MIOX",
    "MOCO": "MOCX",
    "MULA": "MULX",
    "PEDA": "PEDX",
    "PEDO": "PEDX",
    "PENE": "PENX",
    "PUTA": "PUTX",
    "PUTO": "PUTX",
    "QULO": "QULX",
    "RATA": "RATX",
    "RUIN": "RUIX"
}

nombres_comunes = ["MARIA", "LUIS"]

def leer_entidad():
    """
    Lee la entidad federativa de nacimiento.
    """
    
    print('¿En que entidad federativa naciste?\n(2 letras mayúsculas, \
    por ejemplo: DF; ? para ver la lista de entidades)')
    entidad = input('>>>').upper()
    while entidad not in entidades:
        if entidad == '?':
            for clave, valor in entidades.items():
                print(clave, ':', valor)
            print('')

        entidad = input('>>>').upper()
    return entidad

def leer_nombres():
    """Lee los nombres"""
    print('¿Cuáles son tus nombres? (Mayúsculas y sin acentos)')
    nombres = input('>>>').upper()
    return nombres

def leer_apellidos():
    """Lee los apellidos"""
    print('¿Cuáles son tus apellidos? (Mayúsculas y sin acentos)')
    primer_apellido = input('Primer apellido: ').upper()
    segundo_apellido = input('Segundo apellido: ').upper()
    return primer_apellido, segundo_apellido

def leer_anio_nacimiento():
    """Lee el año de nacimiento"""
    print('¿En qué año naciste? (4 dígitos)')
    anio_nacimiento = input('>>>')
    while not anio_nacimiento.isnumeric() or len(anio_nacimiento) != 4:
        anio_nacimiento = input('>>>')
    return anio_nacimiento

def leer_mes_nacimiento():
    """Lee el mes de nacimiento"""
    print('¿En qué mes naciste? (2 dígitos)')
    mes_nacimiento = input('>>>')
    while not mes_nacimiento.isnumeric() or len(mes_nacimiento) != 2:
        mes_nacimiento = input('>>>')
    return mes_nacimiento

def leer_dia_nacimiento():
    """Lee el día de nacimiento"""
    print('¿En qué día naciste? (2 dígitos)')
    dia_nacimiento = input('>>>')
    while not dia_nacimiento.isnumeric() or len(dia_nacimiento) != 2:
        dia_nacimiento = input('>>>')
    return dia_nacimiento

def leer_sexo():
    """Lee el sexo"""
    print('¿Cuál es tu sexo? (H/M)')
    sexo = input('>>>').upper()
    while sexo not in ['H', 'M']:
        sexo = input('>>>').upper()
    return sexo

def siguiente_consonante(palabra: str) -> str:
    """Busca la primera consonante de una palabra"""
    for letra in palabra:
        if letra not in ['A', 'E', 'I', 'O', 'U']:
            return letra
    return 'X'

def siguiente_vocal(palabra: str) -> str:
    """Busca la primera vocal de una palabra"""
    for letra in palabra:
        if letra in ['A', 'E', 'I', 'O', 'U']:
            return letra
    return 'X'

def leer_datos():
    """Lee los datos del usuario"""
    nombres = leer_nombres()
    primer_apellido, segundo_apellido = leer_apellidos()
    anio_nacimiento = leer_anio_nacimiento()
    mes_nacimiento = leer_mes_nacimiento()
    dia_nacimiento = leer_dia_nacimiento()
    sexo = leer_sexo()
    entidad = leer_entidad()
    return nombres, primer_apellido, segundo_apellido, anio_nacimiento, \
        mes_nacimiento, dia_nacimiento, sexo, entidad

def curp_parte_1(primer_apellido: str,
                 segundo_apellido: str,
                 nombres: str) -> str:
    """Calcula la primera parte de la CURP"""
    
    """
    Valida si el primer nombre se encuentra en la lista de nombres comunes segun
    https://www.gob.mx/cms/uploads/attachment/file/681698/reglas_para_la_ejecucion_de_los_procedimientos_asignacion_de_la_curp.pdf
    Entonces se considera la primer letra del segundo nombre, de existir
    """
    if nombres.split(" ")[0] in nombres_comunes and len(nombres.split(" ")) > 1:
        curp = primer_apellido[0:1] + siguiente_vocal(primer_apellido[1:]) + segundo_apellido[0:1] + nombres.split(" ")[1][1]
    else:
        curp = primer_apellido[0:1] + siguiente_vocal(primer_apellido[1:]) + segundo_apellido[0:1] + nombres[0:1]
    if curp in altisonantes:
        curp = altisonantes[curp]
    return curp

def curp_parte_2(anio_nacimiento: str,
                 mes_nacimiento: str,
                 dia_nacimiento: str) -> str:
    """Calcula la segunda parte de la CURP"""
    curp = anio_nacimiento[2:4] + mes_nacimiento + dia_nacimiento
    return curp

def curp_parte_5(primer_apellido: str, segundo_apellido: str, nombres: str) -> str:
    """Calcula la quinta parte de la CURP"""
    curp = siguiente_consonante(primer_apellido[2:]) + \
        siguiente_consonante(segundo_apellido[1:]) + \
        siguiente_consonante(nombres[1:])
    return curp

def get_random_differenciator(anio_nacimiento: str):
    """Calcula los digitos diferenciadores 17 y 18 segun la regla del DOF:
    https://www.dof.gob.mx/nota_detalle.php?codigo=5526717&fecha=18/06/2018#gsc.tab=0
    
    Carácter diferenciador de homonimia y siglo asignado por la aplicación: 0-9 para 
    fechas de nacimiento hasta el 31 de diciembre de 1999, y A-J para fechas de nacimiento
    a partir del día 01 de enero del año 2000 (numérica o alfabética)
    
    Corresponde al dígito verificador, el cual es un carácter asignado por 
    la Secretaría de Gobernación, a través de la aplicación de un algoritmo que
    permite calcular y verificar la correcta conformación de la clave
    """
    
    # Generar un numero aleatorio entre 0 y 9 si la fecha de nacimiento es anterior al 31 de diciembre de 1999
    digito_17 = str(random.randint(0, 9)) if int(anio_nacimiento) < 2000 else random.choice('ABCDEFGHIJ')
    # Generar un caracter alfanumerico aleatorio
    digito_18 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return digito_17 + digito_18

def curp(nombres: str, primer_apellido: str, segundo_apellido: str, anio_nacimiento: str, 
    mes_nacimiento: str, dia_nacimiento: str, sexo: str, entidad: str) -> str:
    """Calcula la CURP"""
    curp = curp_parte_1(primer_apellido, segundo_apellido, nombres) + \
        curp_parte_2(anio_nacimiento, mes_nacimiento, dia_nacimiento) + \
        sexo + entidad + \
        curp_parte_5(primer_apellido, segundo_apellido, nombres) + get_random_differenciator(anio_nacimiento)
    return curp
        
if __name__ == "__main__":
    print(curp(*leer_datos()))
    