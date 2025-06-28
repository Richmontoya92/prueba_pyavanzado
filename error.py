class LargoExcedidoException(Exception):
    """
    Excepción personalizada que se lanza cuando una cadena excede su longitud máxima permitida.
    En este contexto, se usa para el nombre de la campaña si excede los 250 caracteres.
    """
    def __init__(self, message="El largo del nombre de la campaña excede el límite permitido (250 caracteres)."):
        self.message = message
        super().__init__(self.message)

class SubTipoInvalidoException(Exception):
    """
    Excepción personalizada que se lanza cuando el subtipo de un anuncio no es válido
    para el tipo de instancia actual.
    """
    def __init__(self, message="El subtipo ingresado no es válido para este tipo de anuncio."):
        self.message = message
        super().__init__(self.message)