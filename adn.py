def obtener_complemento(base):
    """
     (str) -> str

    >>> obtener_complemento('A')
    'T'
    >>> obtener_complemento('T')
    'A'
    >>> obtener_complemento('C')
    'G'
    >>> obtener_complemento('R')
    Traceback (most recent call last):
    Exception: No es una base
    
    Genera el complemento correspondiente a una base ingresada

    :param base: recibe un complemento para definir su base
    :return: retorna el complemento de la base
    """
    if not es_base(base):
        raise Exception("No es una base")
    if base == "A":
        return "T"
    elif base == "T":
        return "A"
    elif base == "C":
        return "G"
    elif base == "G":
        return "C"
   

def generar_cadena_complementaria(adn):
    '''
    (string) -> string

    >>> generar_cadena_complementaria("ATTTCG")
    'TAAAGC'

    >>> generar_cadena_complementaria("CGTCGA")
    'GCAGCT'

    >>> generar_cadena_complementaria("CGTX1")
    Traceback (most recent call last):
    Exception: La cadena de ADN ingresada no es valida


    Genera cadena con los complementos de la cadena de ADN ingresada
    
    :param adn: string contiene la cadena de ADN de la cual se requiere obtener la cadena complemento

    :return: string retorna la cadena complementaria de la cadena de ADN ingresada
    '''
    if not es_cadena_valida(adn):
        raise Exception("La cadena de ADN ingresada no es valida")
    result = ""
    for caracter in adn:
        complemento = obtener_complemento(caracter)
        result = result + complemento
    return result


def calcular_correspondencia(adn1, adn2):
    """
    (str,str)-> num
    Calcula el porcentaje de correspondencia de 2 cadenas dadas
    >>> calcular_correspondencia("A","TGTA")
    25.0
    >>> calcular_correspondencia("TTTTT","ACGATTTA")
    25.0
    >>> calcular_correspondencia("AGTAT","ATATA")
    60.0

    :param adn1: str:primera cadena de adn a comparar para su porcentaje
    :param adn2: str:segunda cadena recibida para comparar su porcentaje
    :return:num: retorna el porcentaje total en termino de reales
    """
    caracter_correspondiente = 0.0
    cadena_menor = min(len(adn1),len(adn2))
    for indice in range(cadena_menor):
        complemento_caracter_adn1 = obtener_complemento(adn1[indice])
        if adn2[indice] == complemento_caracter_adn1:
            caracter_correspondiente = caracter_correspondiente + 1.0
    cadena_mayor = max(len(adn1),len(adn2))
    porcentaje_correspondencia = 100.0 * caracter_correspondiente / cadena_mayor
    return porcentaje_correspondencia
    

def corresponden(adn1, adn2):
    '''
    (string, string) -> bool

    >>> corresponden("AGTA","TCAT")
    True

    >>> corresponden("CGCG","GCGA")
    False

    >>> corresponden("ATTCC","TAA")
    False

    Valida si una cadena de ADN es complemento de otra cadena de ADN
    :param adn1: string cadena de ADN de la cual se quiere evaluar si adn2 es la cadena complementaria
    :param adn2: string cadena de ADN de la cual se quiere evaluar si es igual a la cadena complementaria de adn1

    :return: bool retorna True en caso de que la cadena de adn2 sea igual a la cadena complementaria de la cadena de adn1 o False en caso de que no lo sea
    '''
    cadena_complementaria = generar_cadena_complementaria(adn1)
    if adn2 == cadena_complementaria:
        return True
    else:
        return False


def es_cadena_valida(adn):
    """
    (str)-> boolean

    >>> es_cadena_valida("ACT")
    True
    >>> es_cadena_valida("XYZ")
    False
    >>> es_cadena_valida("TSG")
    False

    Valida si una cadena es valida o no

    :param adn: String La cadena ingresada a evaluar
    :return: retorna Boolean TRUE si la cadena es valida o FLASE si es incorrecta
    """
    for caracter in adn:
        if not es_base(caracter):
            return False
    return True


def es_base(caracter):
    """
    (string) -> bool

    >>> es_base("A")
    True
    >>> es_base("x")
    False
    >>> es_base("0")
    False
    
    Valida si un caracter ingresado corresponde o no a una base 

    :param caracter: string Caracter ingresado sobre el cual se requiere identificar si corresponde o no a una base
    :return: retorna boolean TRUE si es una base o False si no lo es
    """
    if caracter in ["A","T","C","G"]:
        return True
    else:
        return False


def es_subcadena(adn1, adn2):
    """
    (str, str) -> bool

    >>> es_subcadena('gatc', 'tta')
    False
    >>> es_subcadena('gtattt', 'atcgta')
    False

    :param:adn1:str:primera cadena a comparar
    :param:adn2:str:segunda cadena a comparar
    :return:bool:verificacion si una es subcadena de la otra
    """
    if adn2 in adn1:
        return True
    else:
        return False


def reparar_dano(adn, base):
    """
    (string, string) -> string

    >>> reparar_dano("ATTTCVG","C")
    'ATTTCCG'
    >>> reparar_dano("XXX0TA","C")
    'CCCCTA'
    >>> reparar_dano("ATC1","G")
    'ATCG'

    Repara una cadena de adn de tiene caracteres que no son base reemplazandolos con la base ingresada

    :param adn: string cadena de adn ingresa para que se repare el daño
    :param base: string base ingresada con la que se reemplazan los caracteres de una cadena de adn considerados como daño
    :return: retorna string cadena con daños reparados 
    """
    if not es_base(base):
        raise Exception("La base ingresada para reparar dano no es una base")
    reparado = ""
    for caracter in adn:
        if es_base(caracter):
            reparado = reparado + caracter
        else:
            reparado = reparado + base
    return reparado


def obtener_secciones(adn, n):
    """
    (str, num) -> list of str

    >>> obtener_secciones('AATCGAATCC',5)
    ['AA', 'TC', 'GA', 'AT', 'CC']
    >>> obtener_secciones('ATTGCTAAC',3)
    ['ATT', 'GCT', 'AAC']
    >>> obtener_secciones('GAGATCTCAGT',2)
    ['GAGAT', 'CTCAGT']

    obtiene secciones de una cadena conforme con la catidad requerida

    :param adn:cadena de adn
    :param n: numero de secciones que desea la cadena
    :return:cadena de adn en secciones
    """
    longitud_cadena_grupos=len(adn)//n
    resultado_seccion = []
    for grupo in range(n):
        resultado_grupo = ""
        for caracter in range(longitud_cadena_grupos):
            indice_caracter_adn = grupo * longitud_cadena_grupos + caracter
            resultado_grupo = resultado_grupo + adn[indice_caracter_adn]
        resultado_seccion.append(resultado_grupo)
    if n*longitud_cadena_grupos < len(adn):
        inicio_residuo = n*longitud_cadena_grupos
        fin_residuo = len(adn)
        ultimo_grupo = n-1
        for indice in range(inicio_residuo, fin_residuo):
            resultado_seccion[ultimo_grupo] = resultado_seccion[ultimo_grupo] + adn[indice]
    return resultado_seccion


def obtener_complementos(lista_adn):
    """
    (list of string) -> list of string

    >>> obtener_complementos(["ATT","CCAG","AC"])
    ['TAA', 'GGTC', 'TG']
    >>> obtener_complementos(["CG","ATT"])
    ['GC', 'TAA']
    >>> obtener_complementos(["TT","CC1"])
    Traceback (most recent call last):
    Exception: La cadena de ADN ingresada no es valida

    Obtiene lista de complementos para un listado de adn

    :param lista_adn: string listado de adn de los cuales se busca obtener un listado de complementos
    :return: listado de complementos correspondientes al listado de adn ingresado
    """ 
    lista_complementos = []
    for adn in lista_adn:
        complemento_adn = generar_cadena_complementaria(adn)
        lista_complementos.append(complemento_adn)
    return lista_complementos
   

def unir_cadena(lista_adn):
    """
    (list of string) -> string
    >>> unir_cadena(['TTA', 'CATG', 'AGAT'])
    'TTACATGAGAT'
    >>> unir_cadena(['GGCC', 'TTAA', 'AGTA'])
    'GGCCTTAAAGTA'

    Une cadenas de una lista de adn
    
    :param lista_adn: list of str que representa la cadenas de adn en una lista 
    :return:str con la union de las dos cadenas
    """
    resultado_cadenas = ""
    for cadena in lista_adn:
        for caracter in cadena:
            resultado_cadenas = resultado_cadenas + caracter
    return resultado_cadenas

    
def complementar_cadenas(lista_adn):
    """
    (list of string) -> string

    >>> complementar_cadenas(["ATT","TTA"])
    'TAAAAT'
    >>> complementar_cadenas(["CT","TA","CC"])
    'GAATGG'
    >>> complementar_cadenas(["1CC","TATA","TA"])
    Traceback (most recent call last):
    Exception: La cadena de ADN ingresada no es valida

    Obtiene la cadena con los complementos de las cadenas de ADN ingresadas
    :param Lista_adn: string listado de adn
    :return: cadena con los complementos de la lista de adn ingresada
    """
    lista_complementos = obtener_complementos(lista_adn)
    cadena_complementos = unir_cadena(lista_complementos)
    return cadena_complementos

