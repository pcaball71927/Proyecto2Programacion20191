def obtener_complemento(base):
    if not es_base(base):
        Exception("No es una base")
    if base == "A":
        return "T"
    Elif base == "T":
        return "A"
    Elif base == "C":
        return "G"
    Elif base == "G":
        return "C"    


def generar_cadena_complementaria(adn):
    if not es_cadena_valida(adn):
        Exception("La cadena de ADN ingresada no es valida")
    result = ""
    for caracter in adn:
        complemento = obtener_complemento(caracter)
        result = result + complemento
    return result


def calcular_correspondencia(adn1, adn2):
    cadena_1 = adn1
    cadena_2 = adn2
    ubicacion = 0
    porcentaje = 0

    if len(cadena_1) == len(cadena_2):
        for 1 in cadena_1
            if corresponden(1, cadena_2[ubicacion]):
                porcentaje += 1
                ubicacion += 1
        return porcentaje * 100 / len(cadena_1)
    return 0.0
                
            
def corresponden(adn1, adn2):
    cadena_complementaria = generar_cadena_complementaria(adn1)
    if adn2 == cadena_complementaria:
        return True
    else:
        return False


def es_cadena_valida(adn):
    for caracter in adn:
        if not es_base():
            return False
    return True    
        
    
def es_base(caracter):
    if caracter in ["A","T","C","G"]:
        return True
    else:
        return False


def es_subcadena(adn1, adn2):
    if adn2 in adn1:
        return True
    else:
        return False


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
    longitud_cadena_grupos=Len(adn)//n
    resultado_seccion = []
    for grupo in range(n):
        resultado_grupo = ""
        longitud_cadena_grupo = longitud_cadena_grupos
        if grupo == n-1 and len(adn) % n != 0:
            longitud_cadena_grupo = longitud_cadena_grupos + len(adn)%n
        for caracter in range(longitud_cadena_grupo):
            indice_caracter_adn = grupo * longitud_cadena_grupos + caracter
            resultado_grupo = resultado_grupo + adn[indice_caracter_adn]
        resultado_seccion.append(resultado_grupo)
    return resultado_seccion
            

def obtener_complementos(lista_adn):
    lista_complementos = []
    for adn in lista_adn:
        complemento_adn = generar_cadena_complementaria(adn)
        lista_complementos.append(complemento_adn)
    return lista_complementos


def unir_cadena(lista_adn):
    resultado_cadena = ""
    for cadena in lista_adn:
        for caracter in cadena:
            resultado_cadenas=resultado_cadenas+caracter
    return resultado_cadenas

    
def complementar_cadenas(lista_adn):
    lista_complementos = obtener_complementos(lista_adn)
    cadena_complementos = unir_cadena(lista_complementos)
    return cadena_complementos

