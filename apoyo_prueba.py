from anuncio import Video, Display, Social

# Diccionario que contiene los formatos y subtipos disponibles para los anuncios.
# Esta información se extrae directamente de los atributos de clase de Video, Display y Social.
FORMATOS_ANUNCIOS = {
    Video.FORMATO: {"SUB_TIPOS": Video.SUB_TIPOS},
    Display.FORMATO: {"SUB_TIPOS": Display.SUB_TIPOS},
    Social.FORMATO: {"SUB_TIPOS": Social.SUB_TIPOS}
}