from abc import ABC, abstractmethod
from error import SubTipoInvalidoException # Importa la excepción personalizada

class Anuncio(ABC):
    """
    Clase abstracta base para todos los tipos de anuncios.
    Define atributos comunes y métodos abstractos que deben ser implementados por las subclases.
    """
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str):
        # Inicializa el ancho del anuncio. Si el valor es <= 0, se asigna 1. 
        self.__ancho = 0
        self.ancho = ancho
        # Inicializa el alto del anuncio. Si el valor es <= 0, se asigna 1. 
        self.__alto = 0
        self.alto = alto
        # URL del archivo multimedia (imagen, video, etc.) del anuncio. 
        self.__url_archivo = url_archivo
        # URL de destino al hacer clic en el anuncio. 
        self.__url_clic = url_clic
        # Atributo para el subtipo del anuncio, se establecerá en las subclases concretas. 
        self.__sub_tipo = None

    @property
    def ancho(self):
        """Getter para el atributo ancho."""
        return self.__ancho

    @ancho.setter
    def ancho(self, value):
        """
        Setter para el atributo ancho. 
        Asigna el valor si es mayor a cero, de lo contrario asigna 1. 
        """
        self.__ancho = value if value > 0 else 1

    @property
    def alto(self):
        """Getter para el atributo alto."""
        return self.__alto

    @alto.setter
    def alto(self, value):
        """
        Setter para el atributo alto. 
        Asigna el valor si es mayor a cero, de lo contrario asigna 1. 
        """
        self.__alto = value if value > 0 else 1

    @property
    def url_archivo(self):
        """Getter para el atributo url_archivo."""
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        """
        Setter para el atributo url_archivo con lógica básica de asignación. 
        """
        self.__url_archivo = value

    @property
    def url_clic(self):
        """Getter para el atributo url_clic."""
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, value):
        """
        Setter para el atributo url_clic con lógica básica de asignación. 
        """
        self.__url_clic = value

    @property
    def sub_tipo(self):
        """Getter para el atributo sub_tipo."""
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        """
        Setter para el atributo sub_tipo. 
        Valida que el subtipo ingresado esté dentro de los permitidos (SUB_TIPOS de la clase). 
        Lanza SubTipoInvalidoException si no es válido. 
        """
        # Se asume que cada subclase concreta definirá su propia tupla SUB_TIPOS
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoException()
        self.__sub_tipo = value

    @staticmethod
    def mostrar_formatos(anuncios_data: dict):
        """
        Método estático que muestra en pantalla los formatos y sus subtipos asociados disponibles
        para crear anuncios. 
        Utiliza la información de los atributos de clase (FORMATO y SUB_TIPOS) de las clases de anuncio. 
        """
        for formato, data in anuncios_data.items():
            print(f"FORMATO {formato}:")
            print("==========")
            for subtipo in data['SUB_TIPOS']:
                print(f"- {subtipo}")

    @abstractmethod
    def comprimir_anuncio(self):
        """
        Método abstracto para comprimir el anuncio. Debe ser implementado por las subclases. 
        """
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        """
        Método abstracto para redimensionar el anuncio. Debe ser implementado por las subclases. 
        """
        pass

class Video(Anuncio):
    """
    Clase concreta para anuncios de tipo Video. Hereda de Anuncio. 
    """
    FORMATO = "Video" # Atributo de clase para el formato del anuncio. 
    SUB_TIPOS = ("instream", "outstream") # Subtipos permitidos para videos. 

    def __init__(self, url_archivo: str, url_clic: str, duracion: int):
        # Llama al constructor de la clase padre. Para Video, ancho y alto son fijos en 1. 
        super().__init__(1, 1, url_archivo, url_clic)
        # Inicializa la duración. Si el valor es <= 0, se asigna 5. 
        self.__duracion = 0
        self.duracion = duracion
        # Establece el subtipo inicial del video al primer elemento de SUB_TIPOS
        self.sub_tipo = self.SUB_TIPOS[0] # Usa el setter para validar al inicio

    @property
    def ancho(self):
        """Getter para el atributo ancho. No modificable para Video."""
        return self._Anuncio__ancho # Accede al atributo privado de la clase padre

    @ancho.setter
    def ancho(self, value):
        """
        Setter para el atributo ancho. No permite modificación, siempre se asigna 1. 
        """
        self._Anuncio__ancho = 1

    @property
    def alto(self):
        """Getter para el atributo alto. No modificable para Video."""
        return self._Anuncio__alto # Accede al atributo privado de la clase padre

    @alto.setter
    def alto(self, value):
        """
        Setter para el atributo alto. No permite modificación, siempre se asigna 1. 
        """
        self._Anuncio__alto = 1

    @property
    def duracion(self):
        """Getter para el atributo duracion."""
        return self.__duracion

    @duracion.setter
    def duracion(self, value):
        """
        Setter para el atributo duracion.
        Asigna el valor si es mayor a cero, de lo contrario asigna 5. 
        """
        self.__duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        """
        Implementación del método abstracto para comprimir anuncios de video. 
        Muestra el mensaje específico. 
        """
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        Implementación del método abstracto para redimensionar anuncios de video. 
        Muestra el mensaje específico. 
        """
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    """
    Clase concreta para anuncios de tipo Display (imágenes). Hereda de Anuncio. 
    """
    FORMATO = "Display" # Atributo de clase para el formato del anuncio. 
    SUB_TIPOS = ("tradicional", "native") # Subtipos permitidos para display. 

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str):
        # Llama al constructor de la clase padre. 
        super().__init__(ancho, alto, url_archivo, url_clic)
        # Establece el subtipo inicial del display al primer elemento de SUB_TIPOS
        self.sub_tipo = self.SUB_TIPOS[0] # Usa el setter para validar al inicio

    def comprimir_anuncio(self):
        """
        Implementación del método abstracto para comprimir anuncios display. 
        Muestra el mensaje específico. 
        """
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        Implementación del método abstracto para redimensionar anuncios display. 
        Muestra el mensaje específico. 
        """
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    """
    Clase concreta para anuncios de tipo Social (redes sociales). Hereda de Anuncio. 
    """
    FORMATO = "Social" # Atributo de clase para el formato del anuncio. 
    SUB_TIPOS = ("facebook", "linkedin") # Subtipos permitidos para redes sociales. 

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str):
        # Llama al constructor de la clase padre. [cite: 46]
        super().__init__(ancho, alto, url_archivo, url_clic)
        # Establece el subtipo inicial del social al primer elemento de SUB_TIPOS
        self.sub_tipo = self.SUB_TIPOS[0] # Usa el setter para validar al inicio

    def comprimir_anuncio(self):
        """
        Implementación del método abstracto para comprimir anuncios de redes sociales. 
        Muestra el mensaje específico. [cite: 26]
        """
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        Implementación del método abstracto para redimensionar anuncios de redes sociales. 
        Muestra el mensaje específico. [cite: 28]
        """
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")