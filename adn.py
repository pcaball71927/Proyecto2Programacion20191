def obtener_complemento(base):
    # retorna caracter
    pass


def generar_cadena_complementaria(adn):
    if not es_cadena_valida(adn):
        Exception("La cadena de ADN ingresada no es valida")
    result = ""
    for caracter in adn:
        complemento = obtener_complemento(caracter)
        result = result + complemento
    return result


def calcular_correspondencia(adn1, adn2):
    # retorna num
    pass


def corresponden(adn1, adn2):
    cadena_complementaria = generar_cadena_complementaria(adn1)
    if adn2 == cadena_complementaria:
        return True
    else:
        return False


def es_cadena_valida(adn):
    pass


def es_base(caracter):

    if caracter in ["A","T","C","G"]:
        return True
    else:
        return False


def es_subcadena(adn1, adn2):
    pass


def reparar_dano(adn, base):
    if not es_base(base):
        Exception("La base ingresada para reparar dano no es una base")
    reparado = ""
    for caracter in adn:
        if es_base(caracter):
            reparado = reparado + caracter
        else:
            reparado = reparado + base
    return reparado



def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    lista_complementos = []
    for adn in lista_adn:
        complemento_adn = generar_cadena_complementaria(adn)
        lista_complementos.append(complemento_adn)
    return lista_complementos


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

