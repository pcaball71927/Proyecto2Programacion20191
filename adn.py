def obtener_complemento(base):
    """
     (str) -> str

    >>> obtener_complemento('A')
    'T'
    >>> obtener_complemento('T')
    'A'
    >>> obtener_complemento('C')
    'G'
    >>> obtener_complemento('G')
    'C'
    :param base: recibe un complemento para definir su base
   :return: retorna el complemento de la base
   """
   
def generar_cadena_complementaria(adn):
    '''
    (string) -> string

    >>>generar_cadena_complementaria("ATTTCG")
    "TAAAGC"

    >>>generar_cadena_complementaria("CGTCGA")
    "GCAGCT"

    >>>generar_cadena_complementaria("CGTX1")
    Traceback (most recent call last):
    Exception: La cadena de ADN ingresada no es valida

    Genera cadena con los complementos de la cadena de ADN ingresada
    
    :param adn: string contiene la cadena de ADN de la cual se requiere obtener la cadena complemento

    :return: string retorna la cadena complementaria de la cadena de ADN ingresada
    '''


def calcular_correspondencia(adn1, adn2):
    """
    (str,str)-> num
    Calcula el porcentaje de correspondencia de 2 cadenas dadas
    >>> calcular_correspondencia("AT","TA")
    TA
    2
    100.0
    >>> calcular_correspondencia("CG","GT")
    GC
    2
    50.0
    >>> calcular_correspondencia("AAA","GCG")
    TTT
    3
    0.0
    :param adn1: str:primera cadena de adn a comparar para su porcentaje
    :param adn2: str:segunda cadena recibida para comparar su porcentaje
    :return:num: retorna el porcentaje total en termino de reales
    """

def corresponden(adn1, adn2):
    '''
    (string, string) -> bool

    >>>corresponden("AGTA,TCAT")
    True

    >>>corresponden("CGCG,GCGA")
    False

    >>>corresponden("ATTCC,TAA")
    False

    Valida si una cadena de ADN es complemento de otra cadena de ADN
    :param adn1: string cadena de ADN de la cual se quiere evaluar si adn2 es la cadena complementaria
    :param adn2: string cadena de ADN de la cual se quiere evaluar si es igual a la cadena complementaria de adn1

    :return: bool retorna True en caso de que la cadena de adn2 sea igual a la cadena complementaria de la cadena de adn1 o False en caso de que no lo sea
    '''


def es_cadena_valida(adn):
    """
    (str)-> boolean

    >>> cadena_valida("ACT")
    True
    >>> cadena_valida("XYZ")
    False
    >>> cadena_valida("TSG")
    False

    :param adn: String La cadena ingresada a evaluar
    :return: retorna Boolean TRUE si la cadena es valida o FLASE si es incorrecta
    """


def es_base(caracter):
    """
    (string) -> bool

    >>>es_base("A")
    True
    >>>es_base("x")
    False
    >>>es_base("0")
    False
    
    Valida si un caracter ingresado corresponde o no a una base 

    :param caracter: string Caracter ingresado sobre el cual se requiere identificar si corresponde o no a una base
    :return: retorna boolean TRUE si es una base o False si no lo es
    """


def es_subcadena(adn1, adn2):
    pass


def reparar_dano(adn, base):
    """
    (string, string) -> string

    Repara una cadena de adn de tiene caracteres que no son base reemplazandolos con la base ingresada

    :param adn: string cadena de adn ingresa para que se repare el daño
    :param base: string base ingresada con la que se reemplazan los caracteres de una cadena de adn considerados como daño
    :return: retorna string cadena con daños reparados 
    """
    pass


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

