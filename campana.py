from anuncio import Video, Display, Social # Importa las clases de anuncio para instanciarlas
from error import LargoExcedidoException   # Importa la excepción personalizada
from datetime import date                  # Para el tipo de datos fecha

class Campana:
    """
    Clase que representa una campaña publicitaria, que contiene un listado de anuncios.
    """
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios_data: list):
        # Inicializa el nombre de la campaña. 
        self.__nombre = "" # Se inicializa para que el setter pueda validarlo.
        self.nombre = nombre # Usa el setter para aplicar la regla de validación de longitud.

        # Fecha de inicio de la campaña. 
        self.__fecha_inicio = fecha_inicio
        # Fecha de término de la campaña. 
        self.__fecha_termino = fecha_termino

        # Lista para almacenar las instancias de Anuncio. Composición 1..* con Anuncio. 
        self.__anuncios = []
        # Crea las instancias de Anuncio a partir de los datos proporcionados. 
        self._crear_anuncios(anuncios_data)

    @property
    def nombre(self):
        """Getter para el atributo nombre."""
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        """
        Setter para el atributo nombre. 
        Valida que el nuevo nombre no supere los 250 caracteres. 
        Lanza LargoExcedidoException si excede el límite. 
        """
        if len(value) > 250:
            raise LargoExcedidoException()
        self.__nombre = value

    @property
    def fecha_inicio(self):
        """Getter para el atributo fecha_inicio."""
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value: date):
        """
        Setter para el atributo fecha_inicio con lógica básica de asignación. 
        """
        self.__fecha_inicio = value

    @property
    def fecha_termino(self):
        """Getter para el atributo fecha_termino."""
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, value: date):
        """
        Setter para el atributo fecha_termino con lógica básica de asignación. 
        """
        self.__fecha_termino = value

    @property
    def anuncios(self):
        """
        Getter para el atributo anuncios. No se solicita crear su setter en esta etapa. 
        """
        return self.__anuncios

    def _crear_anuncios(self, anuncios_data: list):
        """
        Método privado para instanciar anuncios y agregarlos a la lista '__anuncios'. 
        Espera una lista de diccionarios, donde cada diccionario contiene la información
        necesaria para crear un tipo específico de Anuncio. 
        """
        for data in anuncios_data:
            tipo = data.get("tipo")
            ancho = data.get("ancho", 0) # Valor por defecto para ancho
            alto = data.get("alto", 0)   # Valor por defecto para alto
            url_archivo = data.get("url_archivo", "")
            url_clic = data.get("url_clic", "")

            if tipo == "Video":
                duracion = data.get("duracion", 0) # Valor por defecto para duracion
                anuncio = Video(url_archivo, url_clic, duracion)
            elif tipo == "Display":
                anuncio = Display(ancho, alto, url_archivo, url_clic)
            elif tipo == "Social":
                anuncio = Social(ancho, alto, url_archivo, url_clic)
            else:
                print(f"Advertencia: Tipo de anuncio desconocido '{tipo}'. Este anuncio no será creado.")
                continue
            self.__anuncios.append(anuncio)

    def __str__(self):
        """
        Método sobrecargado para retornar una cadena de texto que informe el nombre de la campaña
        y la cantidad de anuncios por cada tipo (Video, Display, Social). 
        """
        conteo_anuncios = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self.__anuncios:
            if isinstance(anuncio, Video):
                conteo_anuncios["Video"] += 1
            elif isinstance(anuncio, Display):
                conteo_anuncios["Display"] += 1
            elif isinstance(anuncio, Social):
                conteo_anuncios["Social"] += 1

        # Construye la parte de la cadena que lista los anuncios por tipo
        partes_anuncios = []
        if conteo_anuncios["Video"] > 0:
            partes_anuncios.append(f"{conteo_anuncios['Video']} Video")
        if conteo_anuncios["Display"] > 0:
            partes_anuncios.append(f"{conteo_anuncios['Display']} Display")
        if conteo_anuncios["Social"] > 0:
            partes_anuncios.append(f"{conteo_anuncios['Social']} Social")

        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {', '.join(partes_anuncios)}"