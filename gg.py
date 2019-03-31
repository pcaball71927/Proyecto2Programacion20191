bases = ["A","T","C","G"]
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
def complemento_base(base):
   complento = ""
   if (base == "A"):
     complento = complento + "T"
   elif (base == "T"):
     complento = complento + "A"
   elif (base == "C"):
     complento = complento + "G"
   else:
     complento = complento + "C"
   return complento