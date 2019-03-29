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