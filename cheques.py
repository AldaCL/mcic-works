unidades = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
decenas1 = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
decenas2 = ['veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
centenas = ['ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
singulares = ['un millón', 'un billón', 'un trillón', 'un cuatrillón', 'un quintillón']
plurales = ['millones', 'billones', 'trillones', 'cuatrillones', 'quintillones']

def num_to_text(numero: float):
    """
    Converts a given number into its textual representation in Spanish.

    Args:
        numero (float): The number to convert.

    Returns:
        str: The textual representation of the number in Spanish.

    Raises:
        ValueError: If the input is not a number.
        ValueError: If the input is not a positive integer or float.
    """
    
    try:
        numero = int(numero)
    except ValueError:
        print('El valor ingresado no es un número')
        
    if numero < 0:
        raise ValueError('El número debe ser positivo')

    # units
    if numero < 10:
        return unidades[numero]
    # numbers from 10 to 19
    if numero < 20:
        return decenas1[numero - 10]
    # numbers from 20 to 29
    if numero < 30:
        if numero % 10 == 0:
            return 'veinte'
        else:
            return 'veinti' + unidades[numero % 10]
    # numbers from 30 to 99
    if numero < 100:
        if numero % 10 == 0:
            return decenas2[numero // 10 - 2]
        else:
            return decenas2[numero // 10 - 2] + ' y ' + unidades[numero % 10]
    # numbers from 100 to 999
    if numero < 1000:
        if numero == 100:
            return 'cien'
        if numero % 100 == 0:
            return centenas[numero // 100 - 1]
        else:
            return centenas[numero // 100 - 1] + ' ' + num_to_text(numero % 100)
    # numbers from 1000 to 999999
    if numero < 1000000:
        if numero == 1000:
            return 'un mil'
        if numero < 2000:
            return 'un mil ' + num_to_text(numero % 1000)
        if numero % 1000 == 0:
            return num_to_text(numero // 1000) + ' mil'
        else:
            return num_to_text(numero // 1000) + ' mil ' + num_to_text(numero % 1000)
    # numbers biggers than 999999
    for i in range(0, len(singulares)):
        base = 1000000 ** (i + 1)
        limite = base * 1000000
        if numero < limite:
            if numero == base:
                return singulares[i]
            if numero < 2 * base:
                return singulares[i] + ' ' + num_to_text(numero % base)

            if numero % base == 0:
                return num_to_text(numero // base) + ' ' + plurales[i]
            else:
                return num_to_text(numero // base) + ' ' + plurales[i] + ' ' + num_to_text(numero % base)

    return 'un número muuuuuuuy grande'

def get_decimal(numero):
    """
    Given a number, returns its decimal part as a fraction of 100.
    If the input is not a number or is negative, raises an exception.

    Args:
        numero (float): The number to extract the decimal part from.

    Returns:
        str: The decimal part of the number as a fraction of 100.

    Raises:
        ValueError: If the input is not a number or is negative.
    """
    try:
        numero = float(numero)
    except ValueError:
        print('El valor ingresado no es un número')
        
    if numero < 0:
        raise ValueError('El número debe ser positivo')

    # Get decimal part and convert it to text
    decimal = numero - int(numero)

    decimal = str(decimal).split('.')[1][:2]
    return decimal + '/100'
    
if __name__ == "__main__":
    numero = float(input('Ingrese un número: '))
    entero = num_to_text(numero)
    decimal = get_decimal(numero)
    print( entero + ' ' + decimal + " M.N")